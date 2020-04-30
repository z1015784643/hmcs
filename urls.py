from application import app
from web.contorllers.user.User import router_user
from web.contorllers.static import route_static
from web.contorllers.index import route_index
from web.contorllers.account.Account import router_account
from web.contorllers.goods.Goods import router_goods
from web.contorllers.member.Member import router_member
from web.contorllers.upload.Upload import router_upload

# 拦截路由
from web.interceptos.AuthInterceptor import *


# 蓝图路由
app.register_blueprint(router_user,url_prefix="/user")
app.register_blueprint(route_static,url_prefix='/static')
app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(router_account,url_prefix='/account')
app.register_blueprint(router_goods,url_prefix="/goods")
app.register_blueprint(router_member,url_prefix='/member')
app.register_blueprint(router_upload,url_prefix='/upload')