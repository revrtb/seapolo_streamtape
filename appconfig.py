
class Config():
    TESTING = False
    SECRET_KEY = '\x01\xc8$\x97\xd9\x1a\x13\xd9\x6eE\xabS\xc8\x17\xa4\xc3\x14\xe8Re\x94\x8cKR'


class ProductionConfig(Config):
    DEBUG = False
    MAIL_SERVER = "smtp.zoho.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'support@seapolo.com'
    MAIL_PASS = ''
    RECAPTCHA_PUBLIC_KEY=''
    RECAPTCHA_PRIVATE_KEY=''
    RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOMAIN = 'https://www.seapolo.com/'

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = "smtp.zoho.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'support@seapolo.com'
    MAIL_PASS = ''
    RECAPTCHA_PUBLIC_KEY=''
    RECAPTCHA_PRIVATE_KEY=''
    RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOMAIN = 'http://127.0.0.1:8051/'

class MailData():
	FROM = 'support@seapolo.com'
	TO = ['support@seapolo.com']

class Domain():
    DOMAIN = ""
    ZAP_DOMAIN = ""
    TARGET_DOMAIN = ""
   
