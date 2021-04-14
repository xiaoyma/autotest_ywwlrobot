
from flask import Flask
from Framwork.taskSDK import taskSDK
from ywyrobot.taskCmd import CMD

#创建一个app
app = Flask(__name__)

#在应用中注册taskSDK蓝图对象
app.register_blueprint(taskSDK)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)