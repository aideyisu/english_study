from exercise import get_datetime
from get_words import get_lines


from flask import Flask, request
from flask_mail import Mail, Message
from threading import Thread


app = Flask(__name__)
app.config['MAIL_DEBUG'] = True             # 开启debug，便于调试看信息
app.config['MAIL_SUPPRESS_SEND'] = False    # 发送邮件，为True则不发送
app.config['MAIL_SERVER'] = ''   # 邮箱服务器
app.config['MAIL_PORT'] = 111               # 端口
app.config['MAIL_USE_SSL'] = True           # 重要，qq邮箱需要使用SSL
app.config['MAIL_USE_TLS'] = False          # 不需要使用TLS
app.config['MAIL_USERNAME'] = ''  # 填邮箱
app.config['MAIL_PASSWORD'] = ''      # 填授权码
app.config['MAIL_DEFAULT_SENDER'] = ''  # 填邮箱，默认发送者
mail = Mail(app)


# 异步发送邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


@app.route('/')
def index():
    msg = Message(subject=f'英语每日默写_{get_datetime()}_第{get_lines()}天',
                  sender="",  # 需要使用默认发送者则不用填
                  recipients=[''])
    # 邮件内容会以文本和html两种格式呈现，而你能看到哪种格式取决于你的邮件客户端。
    # msg.body = 'sended by flask-email'
    # body属性没有也行=。=
    # msg.html = '<b>测试Flask发送邮件<b>'
    msg.html = '<b>请查收今日单词<b>'
    with app.open_resource(f'de.xls') as fp:
        msg.attach(f'de.xls', "excel/xls", fp.read())
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return '<h1>邮件发送成功</h1>'


if __name__ == '__main__':
    app.run()