from  application import app,manager
from flask_script import Server
import sys
import urls

# 配置 runserver 指令
manager.add_command('runserver',Server(host='localhost',port=app.config['SERVER_PORT'],use_debugger=True,use_reloader=True))
def main():
    manager.run()

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
