# aunet-flask
Official website of AU hust, powered by AU SicunStudio
#前台注意：
##模板文件夹aunet/templates，资源文件夹aunet/static.
其中不同模块放在不同文件夹下，Admin后台，Design设计，Grage评分系统，Home主页，HR：hr系统
Maertial物资系统，Tpl跳转页面及异常页面.更细划分可参照社团网AUNET
##html文件避免出现大写(大写在SAE可能会出现未知错误)

#后台注意：
##各模块使用蓝图结合
##上传文件路径aunet/templates/Uploads
##公共view,model,form可以写在aunet/models,aunet/views,aunet/forms
