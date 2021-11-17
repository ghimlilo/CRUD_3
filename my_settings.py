SECRET_KEY = 'django-insecure-3s@-)kqhp3(1ij%nsqtc(9b96#ig8-uy0o1%*16#=o9-ii(eih'

DATABASES = {
 'default': {
     'ENGINE': 'django.db.backends.mysql',
     'NAME': 'CRUD_3',  	# mysql database 생성시 작성한 이름
     'USER': 'root',
     'PASSWORD': 'rkskekfk13A!',	# mysql database 생성시 작성한 패스워드
     'HOST': '127.0.0.1',
     'PORT': '3306',
     'OPTIONS': {'charset': 'utf8mb4'}
 }
}