import hashlib,base64,random,string,json

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


# 生成16位的字符串，包含字母和数字
# string.ascii_letters  所有的大小写字母
# string.digits  0-9 数字
    @staticmethod
    def generateSalt(length=16):
        keyList = [random.choice(( string.ascii_letters + string.digits )) for i in range(length)]

        return ("".join(keyList))

