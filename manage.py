from  application import app,manage
from flask_script import Server
import sys

# 配置 runserver 指令
manage.add_command('runserver',Server(host='localhost',port="5000",use_debugger=True,use_reloader=True))
def main():
    manage.run()

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
