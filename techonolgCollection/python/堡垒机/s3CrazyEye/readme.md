django ==1.10.8

使用前的步骤
1.同步数据库
  2个命令如下：
   python manage.py makemigrations 
   python manage.py migrations



2.因为使用自己写的crm替代了django原来的后台管理，
  所以必须自己建立后台管理员账号
  命令如下：
  python manage.py createsuperuser
  一步步往下填就行

3.启动命令:
  python manage.py runserver
  