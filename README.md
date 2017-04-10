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
        - `base.html` - 网站头部和尾部
        -  `fixed.html` - 显示正在开发中

2. Public 模板 可通过 jinja2 提供的模板继承嵌入到新页面

# 后台注意：
1. 各模块使用**blueprint**结合
2. 上传文件路径aunet/static/Uploads
3. 公共view,model,form可以写在aunet/models.py,aunet/views.py,aunet/forms.py  
4. 模块view, model ,form 写在 aunet/模块/view.py ...
5. restful 文档 [api.md](/api.md)

# 配置指南
1. optional:[用virtualenv建一个虚拟环境](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000)
2. 安装requirements.txt中python包：pip install -r requirements.txt(里面有一些包应该用不到)
3. 配置config.py文件中的数据库参数
4. 迁移数据库,运行:
    1. python manage.py db init
    2. python manage.py db migrate
    3. python manage.py db upgrade
5. 建立“超管”角色，并且添加用户
    1. python manage.py CreateSuperRole:建立“超管”角色
    2. python manage.py CreateSuperUser -n name -p password -e email --phone phone:建立一个名为name,密码为password，邮箱为email,电话为phone的超级管理员。-n,-p,-e, --phone参数可省略，默认为admin,123456, None, None
6. 添加必要的新闻 category 和　tag: python manage.py CreateNecessaryItems
    



