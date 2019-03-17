from flask import Flask, render_template
from flask_bootstrap import Bootstrap
#https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
#pip install mysqlclient-1.4.2-cp37-cp37m-win32.whl
from flask_sqlalchemy  import SQLAlchemy
import sshtunnel

app = Flask(__name__)

tunnel = sshtunnel.SSHTunnelForwarder(
	('ssh.pythonanywhere.com'), ssh_username="flimsyware",ssh_password="flimsythefish",
	remote_bind_address=('flimsyware.mysql.pythonanywhere-services.com',3306)
)
tunnel.start()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flimsyware:flimsydatabase@127.0.0.1:{}/flimsyware$default'.format(tunnel.local_bind_port)

db = SQLAlchemy(app)
Bootstrap(app)

results =db.engine.execute("SELECT * FROM University")
#db.session.session_factory.close_all()
@app.route('/')
def Index():
	temp = render_template('/user/index.html')
	for result in results:
		temp = temp + result[1] + " "
	return temp

if __name__ == '__main__':
	app.run(debug = True)