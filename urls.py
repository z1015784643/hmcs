from application import app
from web.contorllers.user.User import router_user
from web.contorllers.static import route_static
from web.contorllers.index import route_index
from web.contorllers.account.Account import router_account

# 拦截路由
from web.interceptos.AuthInterceptor import *


# 蓝图路由
app.register_blueprint(router_user,url_prefix="/user")
app.register_blueprint(route_static,url_prefix='/static')
app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(router_account,url_prefix='/account')