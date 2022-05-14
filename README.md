# LoanHunt
c2c loan lending web app
LoanHunter web app:
BY:
-shivam
-Rushabh

FrameWork:Django
DB:SQLite
Instructions:
Fork:https://github.com/shivamgopchade/LoanHunt
code and type in terminal
python manage.py runserver
This will run app at 8000 port.

NOTE:
You can update userprofile, but avoid updating profile picture. Currently Heroku dont support static file storage
(https://help.heroku.com/K1PPS2WM/why-are-my-file-uploads-missing-deleted-from-the-application) and needs AWS/FireBase/SQL integration.
Though image is saved in media, future login will raise error which may not allow you to login again!!

LIVE:https://loanhunter.herokuapp.com/
