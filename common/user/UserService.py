import hashlib,base64

class UserService():

    # 集合salt和MD5 生成新的密码
    @staticmethod
    def genertePwd(pwd,salt):
        m = hashlib.md5()
        str = '%s-%s'%(base64.encodebytes(pwd.encode('utf-8')),salt)
        m.update(str.encode('utf-8'))
        return m.hexdigest()

    # 对cookie中存储的信息进行加密
    @staticmethod
    def generateAuthCode(user_info = None):
        m = hashlib.md5()
        str = '%s-%s-%s-%s'%(user_info.uid,user_info.login_name,user_info.login_pwd,user_info.login_salt)
        m.update(str.encode('utf-8'))

        return m.hexdigest()
