
from .. import api

# from .resources.news import 
from .resources.users import Users,User1,UserNodes,UserRole,UserSpecNodes,Node1,NodeSpec,Role1,RoleSpec
from .resources.news import SilderShow1,SliderShowSpec,CharmAssociation1,CharmAssociationSpec,News1,NewsSpec
from .resources.news import NewsSpecDetail,Notice1,NoticeSpec,NoticeSpecDetail,AdvanceNotice1,AdvanceNoticeSpec,AdvanceNoticeSpecDetail
from .resources.search import SearchAdvanceNotice,SearchNotice,SearchNews



#User 模块
api.add_resource(Users, '/dashboard/User/Users')
api.add_resource(User1,"/dashboard/User/Users/<string:id>")
api.add_resource(UserRole,"/dashboard/User/Users/<string:id>/Role")
api.add_resource(UserNodes,"/dashboard/User/Users/<string:id>/Nodes")
api.add_resource(UserSpecNodes,"/dashboard/User/Users/<string:userId>/Nodes/<string:nodeId>")
api.add_resource(Node1,"/dashboard/User/Nodes")
api.add_resource(NodeSpec,"/dashboard/User/Nodes/<string:id>")
api.add_resource(Role1,"/dashboard/User/Role")
api.add_resource(RoleSpec,"/dashboard/User/Role/<string:id>")


#News 模块

api.add_resource(SilderShow1,"/dashboard/News/SilderShow")
api.add_resource(SliderShowSpec,"/dashboard/News/SilderShow/<string:id>")
api.add_resource(CharmAssociation1,"/dashboard/News/CharmAssociation")
api.add_resource(CharmAssociationSpec,"/dashboard/News/CharmAssociation/<string:id>")
api.add_resource(News1,"/dashboard/News/News/News")
api.add_resource(NewsSpec,"/dashboard/News/News/News/<string:id>")
api.add_resource(NewsSpecDetail,"/dashboard/News/News/News/<string:id>/Detail")
api.add_resource(Notice1,"/dashboard/News/News/Notice")
api.add_resource(NoticeSpec,"/dashboard/News/News/Notice/<string:id>")
api.add_resource(NoticeSpecDetail,"/dashboard/News/News/Notice/<string:id>/Detail")
api.add_resource(AdvanceNotice1,"/dashboard/News/News/AdvanceNotice")
api.add_resource(AdvanceNoticeSpec,"/dashboard/News/News/AdvanceNotice/<string:id>")
api.add_resource(AdvanceNoticeSpecDetail,"/dashboard/News/News/AdvanceNotice/<string:id>/Detail")


#Search 模块

api.add_resource(SearchNews,"/dashboard/Search/News")
api.add_resource(SearchNotice,"/dashboard/Search/Notice")
api.add_resource(SearchAdvanceNotice,"/dashboard/Search/AdvanceNotice")