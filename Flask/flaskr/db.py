from flask_sqlalchemy  import SQLAlchemy
import sshtunnel
#https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
#pip install mysqlclient-1.4.2-cp37-cp37m-win32.whl

db = None
tunnel = None

def DBStart(app):
	tunnel = sshtunnel.SSHTunnelForwarder(
		('ssh.pythonanywhere.com'), ssh_username="flimsyware",ssh_password="flimsythefish",
		remote_bind_address=('flimsyware.mysql.pythonanywhere-services.com',3306)
	)
	tunnel.start()
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flimsyware:flimsydatabase@127.0.0.1:{}/flimsyware$default'.format(tunnel.local_bind_port)
	db = SQLAlchemy(app)


def Query():
	return db.engine.execute("SELECT * FROM University WHERE Name = \"Akron\";")