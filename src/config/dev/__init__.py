from src.config import Config


class Dev(Config):
	# Flask.
	DEBUG = True
	TESTING = False
	ENV = 'development'

	# Logging.
	FILENAME = ''

	# SQLAlchemy.
	SQLALCHEMY_DATABASE_URI = 'sqlite:///db/dev.db'

	# import os
	# import binascii
	# binascii.hexlify(os.urandom(128)).decode()
	JWT_SECRET_KEY = '31e40b167539305e0fed148fa4f7089b584fbf8011968fd548db340f210c1a449900c10d280da5782ff3b621a1134373bc43655574c78d4787925a4ad97956162cf4715889b19d9df18f8ae60a79d259f790bc9cace11fe6bf1b5d09fe7b93d2128e182fb084b16de04363107a0115569460587ae7ada1c32658523d13b7c4cd'

	# Host login.
	USER = 'test'
	PASSWORD = 'test'