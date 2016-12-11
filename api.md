
##1. 注意
由于学校服务器不支持PUT 和DELETE操作，所以PUT 和DELETE并入POST ,请求时以
requestMethod:POST/PUT/DELETE作为区分
##2.错误信息汇总:
    status 400，已存在(比如：用户名，角色名，节点名称，新闻属性和标签唯一，重复时返回此错误)

    status 404 Not founded
    status 401 Unauthorized
##3.用户模块
GET  /api/User/Users

    [{
    id:int                  
    userName:str,
    loginTime:,（上一次登陆时间）
    loginIp:str,(上一次登陆ip)
    status:bool(该用户状态True正常，false被禁),
    email:str,
    nodes:[
    {   id:int,             
        nodeName:str,
        status:bool,
        level:int
    }]
    roles:[{                是roles不是role
    id:int ,                
    roleName:str,
    status:bool,
    }
    ]

    }
    ]


POST /api/User/Users

    {
    userName:str,
    passWord:str
    email:str
    roleName:list(str)        注意是list
    }

GET /api/User/Users/id

    {
    int: int   ,               新添加的，其实也可以不要，因为与路由的id一致,格式统一一下加上吧
     userName:str,
    loginTime:,（上一次登陆时间）
    loginIp:str,(上一次登陆ip)
    status:bool(该用户状态True正常，false被禁),
    email:str,
    nodes:[
    {    id:int,                
         nodeName:str,
        status:bool,
        level:int
    }]
    roles:[{                    是roles不是role
    id:int ,                    
    roleName:str,
    status:bool,
    }
    ]
    }

PUT /api/User/Users/id

    {
    userName:str,
    passWord:str
    email:str
    roleName:list(str)             注意是list 
    status:bool,


    } optional

DELETE /api/User/Users/id

GET /api/User/CurrentUser           

    {
        和 Get/api/User/Users/id 返回的数据一样
    }

GET /api/User/Nodes

    [
    {
    id: int             
    nodeName:str,
    status:bool,
    level:int
    }
    ]

GET /api/User/Nodes/id

    {
    id: int             
    nodeName:str,
    status:bool,
    level:int
    }
PUT /api/User/Nodes/id

    {
    status :bool
    } optional

GET /api/User/Roles

    [{
    id:int,             
    roleName:str,
    status:bool,
    nodes:[
        {
        id:int,          
         nodeName:str,
        status:bool,
        level:int
    }
    ]
    }]

POST /api/User/Roles(新建一角色)

    {
    roleName:str
    nodeName:list(要添加的节点名)
    }

GET /api/User/Roles/id

    {
    id:int ,             
     roleName:str,
    status:bool,
    nodes:[
        {
        id: int,        
         nodeName:str,
        status:bool,
        level:int
    }
    ]
    }
PUT /api/User/Roles/id

    {
    roleName:list(str),             注意是list
    status:bool,
    nodeName:list
    }
    optional

DELETE /api/User/Roles/id


##4.搜索模块

GET /api/Search/News?category=&tags=&start=&end=&sort

    {
        和 GET/api/News/News返回的数据格式一样
    }注:tags可以多个,start-end为搜索的时间范围,为时间戳  sort=latest/oldest 反向或正向排序



##5. html

GET /api/modules/fp:path

##6. News

GET /api/News/News/id application/json
    
    ->

    [
        {
            id: int,
            author: str,
            category: str,
            tags: [str],
            postTime: UTC timestamp seconds,
            title: str,
            outline: str,
            editable: boolean,
        }
    ]

POST /api/News/News application/json
    
    {
        category: str,
        tags: [str],
        title: str,
        detail: str,
    }

    -> 

    HTTP state code

    200 success


GET /api/News/News/id:str

    
    ->

    {
        id: int,
        category: str,
        tags: [str],
        postTime: UTC timestamp seconds,
        title: str,
        outline: str,
        editable: boolean,

        detail: str
    }

    or

    404

PUT /api/News/News/id:str
    
    {
        category: str,
        tags: [str],
        title: str,
        outline: str,
        editable: boolean,

        detail: str
    }

    # optional keys

    ->

    HTTP state code

    200 OK


DELETE /api/News/News/id:str

    ->

    200 OK
    500 Not Authorized

    # slideshow

GET /api/News/SliderShow

    ->

    [
        {
            id: int,
            postTime: UTC timestamp sec,
            title: str,
            imgUrl: str,               
            outline: str,
            editable: bool,
            link: str,
        }
    ]

POST /api/News/SliderShow

    {
        title: str,
        imgUrl: str,               
        outline: str,
        link: str,
    }

PUT /api/News/SliderShow/id:str

    {
        title: str,
        imgUrl: str,                
        outline: str,
        link: str,
        #editable: bool,
    }

    #optional keys

DELETE /api/News/SliderShow/id:str

    ->

    200 OK

GET /api/News/Tags

    [{
        id:int,
        name:str
    }]
POST /api/News/Tags

    {
        name:str
    }
GET /api/News/Tags/id

     {
        id:int,
        name:str
    }
PUT /api/News/Tags/id

    {
        name：str
    }
DELETE /api/News/Tags/id

GET /api/News/Categorys

    [{
        id:int,
        name:str
    }]
POST /api/News/Categorys

    {
        name:str
    }
GET /api/News/Categorys/id

     {
        id:int,
        name:str
    }
PUT /api/News/Categorys/id

    {
        name
    }

DELETE /api/News/Categorys/id
