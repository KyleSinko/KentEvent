# KentEvent

Install Git
https://git-scm.com/downloads
<br>
Install Python with custom installation, make sure you have pip selected
https://www.python.org/downloads/
<br>
Install pipenv
In your terminal: 
pip install pipenv
<br>
Install Flask
In your terminal: 
pip install flask
<br>
If you do not have a text editor you have/like, install Visual Studio Code at:
https://code.visualstudio.com/
Visual Studio Code also has a built in console if you use the keyboard shortcut 'ctrl + `'
<br>
fork the repo
In the top right of your page, click on the fork button. 
If you don't know what forking means read this: 
https://help.github.com/en/articles/fork-a-repo
<br>
clone the repo
On the the page of your forked repo click on the green button that says "Clone or download". 
Copy the link in the menu that pops up.
Open up your terminal and go to the folder you want to clone this project.
<br>
Run the command:
git clone 
This link is the link you copied from the "Clone or download" button
<br>
You should also clone the main repo so you can view the main project in it's current state.
<br>
In your terminal: 
Go into the project folder you just cloned
cd branch
<br>
Create a remote of the repo you forked from
git remote add upstream 
Pushing/Pulling
Add all files before you commit
git add *
<br>
Add indivual files before you commit
git add yes.py
git add yes.py no.py
<br>
Commit your added files
git commit -m"message about changes"
<br>
Push your commits to the repo from your fork
git push upstream master
<br>
Always test the project in your own fork before pushing into the main repo
Always push from your fork and never from the main repo
<br>
Pull the current version of the main repo into your fork
git pull upstream master
<br>
Pull the current version of the main repo into your clone of the main repo
git pull
<br>
Installing packages
pipenv install
<br>
Always pull before you commit
Start
In your terminal: 
<br>
# Set environments
Windows PowerShell:
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
<br>
Mac Terminal/Linux: 
export FLASK_APP=flaskr
export FLASK_ENV=development
<br>
Install packages
pipenv install
<br>
Start your pipenv virtual environment
pipenv shell
<br>
Initialize the database
flask init-db
<br>
# Start the project
flask run
