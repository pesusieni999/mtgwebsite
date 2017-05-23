# MtG web application for play club
This is personal project and for personal usage.

## Host
* Heroku (planned)

## Implementation technologies
* Django
* HTML
* JavaScript
* CSS
* JQuery
* PostgreSQL

## Current features
* Registration
* Login/Logout
* Create/Edit/Delete games.
* Create/Edit/Delete sign-ups to games.

## Planned features (ideas)
* List played formats.
* Banned cards list.
* Club rules.
* Discussion about bans/unbans.
* Votes (bans/unbans/formats/etc) *UNDER WORK.*
* Trade lists
* Comparing trade lists
* Keeping track of club purchases and booster usage
* Customizable randomizer (Random commanders, cards, etc.)

## Contribution
### Participate in development, do the following:
1. Pull the repository to your local environment.
2. Install at least Python 3.5.3 or newer.
3. Install pip for said Python version.
4. Install requirements for PostgreSQL
5. Create PostgreSQL database.
6. Create virtual environment that uses python 3.
7. Activate the virtual environment.
8. Install requirements found in requirements.txt
9. Create migrations for the application.
10. Run migrations for the application.
11. Start the server.
12. Request application secret key from me.
13. Add the application secret key to the settings.py found inside website-folder.

```shell
# These guides are for Ubuntu, other machines you will find guides on the Internet.

# 1. Pulling repository
git clone git@github.com:pesusieni999/mtgwebsite.git

# 2. Installing Python
Should be preinstalled in Ubuntu OS. For other OS see Python website.

# 3. Installing pip for Python3
Should be preinstalled in Ubuntu OS. For other OS see documentation on the Web.

# 4. Installing requirements for PostgreSQL
sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib

# 5. Creating PostgreSQL
sudo su - postgres
psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
exit

# 6. Creating virtual environment.
virtualenv -p /usr/bin/python3 venv

# 7. Activating the virtual environment
source venv/bin/activate

# 8. Installing requirements
pip install -r requirements.txt

# 9. Creating migrations
./manage.py makemigrations mtgapp

# 10. Running migrations
./manage.py migrate

# 11. Starting server
./manage.py runserver
```
