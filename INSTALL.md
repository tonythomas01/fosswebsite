## Development Environment
Its super easy to set up our development environment

## Collect Pre-requisites
Install `python-pip` and `virtualenvwrapper` 
```bash
sudo apt-get install python-pip
sudo pip install virtualenvwrapper
```
## Get the files
```bash
git clone https://seshagiriprabhu@bitbucket.org/fosswebsite/fosswebsite.git
```
## Setup development environment
First, some initialization steps. Most of this only needs to be done 
one time. You will want to add the command to source 
`/usr/local/bin/virtualenvwrapper.sh` to your shell startup file 
(`.bashrc` or `.zshrc`) changing the path to `virtualenvwrapper.sh` 
depending on where it was installed by `pip`.
```bash
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
```
Lets create a virtual environment for our project
```bash
mkvirtualenv foss
workon foss
```
## Install requirements
```
All the requirements are mentioned in the file `requirements.txt`.
```bash
pip install -r requirements.txt
```
## Local settings
Copy the `local-settings.py` from `conffiles` to `fossWebsite` directory.
```bash
cp conffiles\local-settings.py fossWebsite\local_settings.py
```
## Setup database
In the development phase, we use sqlite3.db. We need to create a folder
named `db` in-order to store our temporary db file.
```bash
mkdir db && touch db/db.db
```
```bash
python manage.py syncdb
```
```bash
python manage.py collectstatic
```
## Run server
```bash
python manage.py runserver
```
