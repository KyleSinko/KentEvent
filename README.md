# KentEvent

Install Git
<br>
https://git-scm.com/downloads
<br>
<br>
Install Python with custom installation, make sure you have pip selected
<br>
https://www.python.org/downloads/
<br>
<br>
Install pipenv
<br>
In your terminal: 
<br>
  pip install pipenv
<br>
<br>
Install Flask
<br>
In your terminal: 
<br>
  pip install flask
<br>
<br>
If you do not have a text editor you have/like, install Visual Studio Code at:
https://code.visualstudio.com/
<br>
Visual Studio Code also has a built in console if you use the keyboard shortcut 'ctrl + `'
<br>
<br>
fork the repo
<br>
In the top right of your page, click on the fork button. 
<br>
If you don't know what forking means read this: 
<br>
https://help.github.com/en/articles/fork-a-repo
<br>
<br>
clone the repo
<br>
On the the page of your forked repo click on the green button that says "Clone or download". 
<br>
Copy the link in the menu that pops up.
<br>
Open up your terminal and go to the folder you want to clone this project.
<br>
<br>
Run the command:
<br>
git clone 
<br>
This link is the link you copied from the "Clone or download" button
<br>
<br>
You should also clone the main repo so you can view the main project in it's current state.
<br>
<br>
In your terminal: 
<br>
Go into the project folder you just cloned
<br>
cd KentEvent
<br>
<br>
Create a remote of the repo you forked from
<br>
git remote add upstream 
<br>
Pushing/Pulling
Add all files before you commit
<br>
git add *
<br>
<br>
Commit your added files
<br>
git commit -m"message about changes"
<br>
<br>
Push your commits to the repo from your fork
<br>
git push upstream master
<br>
<br>
Always test the project in your own fork before pushing into the main repo. 
Always push from your fork and never from the main repo
<br>
<br>
Pull the current version of the main repo into your fork
<br>
git pull upstream master
<br>
<br>
Pull the current version of the main repo into your clone of the main repo
<br>
git pull
<br>
<br>
Installing packages
<br>
pipenv install
<br>
<br>
# Set environments
Windows PowerShell:
<br>
$env:FLASK_APP = "flaskr"
<br>
$env:FLASK_ENV = "development"
<br>
<br>
Mac Terminal/Linux: 
<br>
export FLASK_APP=flaskr
<br>
export FLASK_ENV=development
<br>
<br>
Install packages: 
pipenv install
<br>
<br>
Start your pipenv virtual environment
<br>

pipenv shell
<br>
<br>
# Start the project
flask run
