# LoanHunt
c2c loan lending web app<br/>
LoanHunter web app:<br/>
BY:<br />
-shivam<br/>
-Rushabh<br/>
<br/>
FrameWork:Django<br/>
DB:SQLite <br/>
Instructions:<br/>
Fork:https://github.com/shivamgopchade/LoanHunt <br/>
code and type in terminal <br/>
python manage.py runserver <br/>
This will run app at 8000 port. <br/>
<br/>
NOTE:<br/>
You can update userprofile, but avoid updating profile picture. Currently Heroku dont support static file storage
(https://help.heroku.com/K1PPS2WM/why-are-my-file-uploads-missing-deleted-from-the-application) and needs AWS/FireBase/SQL integration.
Though image is saved in media, future login will raise error which may not allow you to login again!!
<br/>
LIVE:https://loanhunter.herokuapp.com/
