
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

创建新项目



## 生成数据库管理文件

    makemigrations
    
## 生成数据表

    migrate
    
    
##设计模型
    #创建用户模块
    startapp users
    
##设计user表