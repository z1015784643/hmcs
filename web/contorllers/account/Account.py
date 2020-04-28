from flask import Blueprint,request,redirect,jsonify

from application import db
from common.libs.Helper import ops_render,getCurrentDate
from common.models.User import User
from common.libs.UrlManager import UrlManager
from common.user.UserService import UserService
from common.models.User import db
import json


router_account = Blueprint("account_page",__name__)

@router_account.route('/index')
def index():
    resp_data={}
    req = request.values
    query = User.query
    if 'status' in req and int(req['status']) >-1:
        query = User.query.filter(User.status == int(req['status']))
    list = query.all()
    resp_data['list'] = list
    resp_data['status'] = {
        '1':'正常',
        '0':'删除',
    }
    return ops_render('account/index.html',resp_data)

@router_account.route('/info')
def info():
    resp_data = {}
    req = request.args
    uid = int(req.get('id',0))
    reback_url = UrlManager.buildUrl('/account/index')
    if uid<1:
        return redirect(reback_url)
    info = User.query.filter_by(uid=uid).first()
    if not info:
        return redirect(reback_url)
    resp_data['info'] = info
    return ops_render('account/info.html',resp_data)

@router_account.route('/set',methods=['GET','POST'])
def set():
    if request.method == 'GET':
        resp_data = {}
        req = request.args
        uid = int(req.get('id',0))
        info = None
        if uid:
            info = User.query.filter_by(uid=uid).first()
        resp_data['info'] = info
        return ops_render('account/set.html',resp_data)
    # post请求
    resp={
        'code':200,
        'msg':'操作成功',
        'data':{}
    }
    req = request.values
    id = req['id'] if 'id' in req else 0
    nickname = req['nickname'] if 'nickname' in req else ''
    mobile = req['mobile'] if 'mobile' in req else ''
    email = req['email'] if 'email' in req else ''
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    print('新增的用户信息',nickname,mobile,email,login_name,login_pwd)

    if nickname is None or len(nickname)<1:
        resp['code'] = 0
        resp['msg'] = '请输入正确的昵称'
        return jsonify(resp)
    if mobile is None or len(mobile)<1:
        resp['code'] = 0
        resp['msg'] = '请输入正确的手机号'
        return jsonify(resp)
    if email is None or len(email)<1:
        resp['code'] = 0
        resp['msg'] = '请输入正确的邮箱'
        return jsonify(resp)
    if login_name is None or len(login_name)<1:
        resp['code'] = 0
        resp['msg'] = '请输入正确的登录名称'
        return jsonify(resp)
    if login_pwd is None or len(login_pwd)<6:
        resp['code'] = 0
        resp['msg'] = '请输入正确的密码'
        return jsonify(resp)

    is_exsits = User.query.filter(User.login_name == login_name).first()
    if is_exsits:
        resp['code'] = 0
        resp['msg'] = '该用户已存在'
        return jsonify(resp)
    

    user_info = User.query.filter_by(uid = id).first()
    if user_info:
        model_user = user_info
    else:
        model_user = User()
        model_user.created_time = getCurrentDate()
        model_user.login_salt = UserService.generateSalt()
        
    
    model_user.nickname = nickname
    model_user.mobile = mobile
    model_user.email = email
    model_user.login_name = login_name
    # if user_info.id == User.uid:
    #     resp['code'] = 0
    #     resp['msg'] = '该用户不可修改'
    #     return jsonify(resp)
    model_user.login_pwd = UserService.genertePwd(login_pwd,model_user.login_salt)
    # if login_pwd != default_pwd

    model_user.updated_time = getCurrentDate()
    db.session.add(model_user)
    db.session.commit()

    return jsonify(resp)



@router_account.route('removeOrRecover',methods=['GET','POST'])
def removeOrRecover():
    resp_data={
        'code':1,
        'msg':'操作成功',
        'data':{}
    }
    req = request.values
    id = req['id'] if 'id' in req else 0
    acts = req['acts'] if 'acts' in req else ''

    if acts not in ['remove','recover']:
        resp['code'] = 0
        resp['msg'] = '操作有误'
        return jsonify(resp)

    if id:
        user_info = User.query.filter_by(uid=id).first()
        if not user_info:
            resp['code'] = 0
            resp['msg'] = '账户不存在'
            return jsonify(resp)
        if user_info and user_info.uid == 1:
            resp['code'] = 0
            resp['msg'] = '该用户不可删除'
            return jsonify(resp)
        if acts == 'remove':
            user_info.status = 0
            user_info.updated_time = getCurrentDate()
            db.session.commit()
        elif acts == 'recover':
            user_info.status = 1
            user_info.updated_time = getCurrentDate()
            db.session.commit()
        
        
    return jsonify(resp_data)