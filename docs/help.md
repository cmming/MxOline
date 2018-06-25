
mkvirtualenv --python=/usr/local/python3.5.3/bin/python venv_name
mkvirtualenv --python=D:/python/py276/python venv_name
#进入
workon virtualPythonname
#退出
deactivate
#删除
rmvirtualenv virtualPythonname

创建虚拟环境

安装django mysqlclient pillow

Django              1.9    
django-crispy-forms 1.7.2  
django-formtools    2.1    
httplib2            0.9.2  
mysqlclient         1.3.12 
Pillow              5.1.0  
pip                 10.0.1 
setuptools          39.2.0 
wheel               0.31.1 


创建新项目



## 生成数据库管理文件

    makemigrations
    
## 生成数据表

    migrate
    
    
##设计模型
    #创建用户模块
    startapp users
    
##设计user表