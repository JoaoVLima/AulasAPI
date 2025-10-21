# AulasAPI


```bash
# Clone this repository
$ git clone https://github.com/JoaoVLima/AulasAPI.git

# Go into the repository
$ cd AulasAPI

# Create a venv (Virtual Enviroment)
$ python3 -m venv venv

# Activate the venv
$ source venv/bin/activate  # (Unix)
$ .\venv\Scripts\activate   # (Windows)
    
# Install dependencies
$ pip install -r requirements.txt

# Generate a new Django Secret Key
$ python3 generate_secrets.py
    
# Generate a new Django Models and the sqlite database
$ python3 manage.py makemigrations
$ python3 manage.py migrate

# Run the app
$ python3 manage.py runserver


python3 manage.py compilemessages
django-admin makemessages -a
django-admin makemessages -l pt_BR
django-admin makemessages -l en

```

