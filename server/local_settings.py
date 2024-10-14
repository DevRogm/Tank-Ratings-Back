# =================================
# DATA BASE
# =================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "tank_ratings_db",
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# =================================
# WORLD OF TANKS - API
# =================================