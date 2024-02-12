# Django multi database example
<p align="center">
  <img style="width: 60%;" src="./static/image/intro.gif">
</p>
Support Group - <a href="https://t.me/+Ng1axYLNyBAyYTRi">Telegram</a> <br/>

## Installation
* 1 - clone repo
   - ```git clone git@github.com:Muhammadali-Akbarov/dj_multi_db.git```
* 2 - create a virtual environment and activate
  - ```pip3 install virtualenv```
  - ```virtualenv venv```
  - ```source venv/bin/activate```
* 3 - cd into project "cd dj_multi_db"
* 4 - Install dependencies
  - ```pip3 install -r requirements.txt```
* 5 - Up databased dependencies
  -  ```make psql.up```
  -  ```make mysql.up```
  - ```make migrate.psql```
  -  ```make migrate.mysql```
* 6 - Run
  - ```make run.local```
