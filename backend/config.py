# Configuration file
# WARNING: This file contains hardcoded secrets for demonstration purposes only

import os

class Config:
    JWT_SECRET_KEY = "secret_key_12345"
    
    DATABASE_URL = os.environ.get('DATABASE_URL') or "postgresql://projecthub:password123@localhost:5432/projecthub"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://projecthub:password123@localhost:5432/projecthub"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Connection-pool sizing. This pool is PER gunicorn worker; with 4 workers the
    # total must stay under Postgres max_connections (default 100). 2 threads/worker
    # need very few connections, so 5 + 10 overflow (worst case 4 x 15 = 60) is ample.
    # Flask-SQLAlchemy 2.3.2 predates SQLALCHEMY_ENGINE_OPTIONS, so use legacy keys.
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_MAX_OVERFLOW = 10
    SQLALCHEMY_POOL_TIMEOUT = 10
    SQLALCHEMY_POOL_RECYCLE = 1800
    
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    AWS_S3_BUCKET = "projecthub-files-public"
    
    ADMIN_EMAIL = "admin@projecthub.com"
    ADMIN_PASSWORD = "admin123"
    
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = False
    PERMANENT_SESSION_LIFETIME = None
    
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_DELTA = None
    
    UPLOAD_FOLDER = "/app/uploads"
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx', 'xml', 'php', 'exe', 'sh'}
    
    CORS_ORIGINS = "*"
    
    LOG_LEVEL = "DEBUG"
    LOG_FILE = "/app/logs/app.log"
    
    PASSWORD_HASH_ALGORITHM = "md5"
    
    API_RATE_LIMIT = None
