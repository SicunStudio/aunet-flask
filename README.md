# aunet-flask
Official website of AU hust, powered by AU SicunStudio
# 前台注意：
1. - [aunet/templates](/aunet/templates/) - 模板文件夹
    - [aunet/static](/aunet/static/) - 资源文件夹

    模块：
    - `Admin` - 后台
    - `Design` - 设计委任系统
    - `Grage` - 评分系统
    - `Home` - 主页
    - `HR` - HR系统
    - `Material` - 物资系统
    - `Tpl` - 跳转页面及异常页面
    - `Public` - 公用文件
2. html文件避免出现大写(大写在SAE可能会出现未知错误)

# 后台注意：
1. 各模块使用蓝图结合
2. 上传文件路径aunet/templates/Uploads
3. 公共view,model,form可以写在aunet/models,aunet/views,aunet/forms

# 配置指南
1. 配置config.py文件中的数据库参数
2. 迁移数据库,运行
    1. python manage.py db init
    2. python manage.py db migrate
    3. python manage.py db upgrade
3. 建立“超管”角色，并且添加用户
    1. python manage.py CreateSuperRole 建立“超管”角色
    2. python manage.py CreateSuperUser -n name -p password -e email,其中-n -p -e参数可省略，建立一个名为name,密码为password，邮箱为email的超级管理员
    
    



