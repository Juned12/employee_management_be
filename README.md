# employee_management_be

Django JWT Authentication base authorization and authentication backend application for employee management platform

All endpoints can be seen at /api/docs

Install dependencies:
* sudo apt update
* sudo apt-get install mysql-server
* sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev

## Requirements

* python3 3.6
* PIP
* python3 virtual environment to track PIP dependencies:
  * python3 -m venv env
  * . env/bin/activate
  * pip3 install -r requirements.txt
* Mysql


## Prepare database

In Mysql terminal:
```sql
CREATE DATABASE '[db_name]';
CREATE USER '[user_name]'@'%' IDENTIFIED WITH mysql_native_password BY '[password]';
GRANT ALL ON [db_name].* TO '[user_name]'@'%';
FLUSH PRIVILEGES;
```

Rename \settings\config.sample.json to config.json with appropriate values
Create a folder named logs in the project root directory 

* sudo service mysql restart

* python3 manage.py migrate
* python3 manage.py runserver

