from application import app
from web.contorllers.user.User import router_user
from web.contorllers.static import route_static

app.register_blueprint(router_user,url_prefix="/user")
app.register_blueprint(route_static,url_prefix='/static')