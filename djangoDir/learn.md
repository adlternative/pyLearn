
每当需要修改 “ 学习笔记 ” 管理的数据时,都采取如下三个步骤:修改 models.py ;对 learning_logs 调用 makemigrations ;让 Django 迁移项目。
修改 models.py 
python3 manage.py makemigrations learning_logs 
python3 manage.py migrate
再在admin.py中注册模型

新app则需要在project的　INSTALLED_APPS添加新项目再进行makemigrations和迁移项目
