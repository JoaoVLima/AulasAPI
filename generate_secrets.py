from pathlib import Path
from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()

fp = open('django_secrets.py', 'w')
fp.write(f"DJANGO_KEY = '{secret_key}'\n")
fp.write(f"DJANGO_DEBUG = True\n")
fp.write(f"""DJANGO_DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{Path(__file__).resolve().parent}/db.sqlite3',
    }}
}}
""")
fp.close()


