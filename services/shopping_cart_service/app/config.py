class DevelopmentConfig():
  DEBUG = True
  MYSQL_HOST = 'localhost'
  MYSQL_USER = 'root'
  MYSQL_PASSWORD = 'admin123.'
  MYSQL_DB = 'prueba_naowee'
  SECRET_KEY = 'clave_segura_para_jwt'

config = {
  'development': DevelopmentConfig
}