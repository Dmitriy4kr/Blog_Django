import os

os.environ['SECRET_KEY'] = '-'
os.environ['DEBUG'] = 'False'

os.environ['DB_NAME'] = 'sport_blog'
os.environ['DB_USER'] = 'postgres'
os.environ['DB_PASSWORD'] = '5093632'
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_PORT'] = '5432'

os.environ['ALLOWED_HOSTS'] = '127.0.0.1,localhost'