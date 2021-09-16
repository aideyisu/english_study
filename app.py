from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from threading import Thread

from write_words import write_new_words, write_wrong_words
from get_words import get_lines, get_exercise_words, get_config
from exercise import output_today_exercise, get_datetime
app = Flask(__name__)
# ------------ prepare to send email
# TODO get email config with function
app.config['MAIL_DEBUG'] = True             # 开启debug，便于调试看信息
app.config['MAIL_SUPPRESS_SEND'] = False    # 发送邮件，为True则不发送
app.config['MAIL_SERVER'] = get_config('Email', 'MAIL_SERVER')   # 邮箱服务器
app.config['MAIL_PORT'] = get_config('Email', 'MAIL_PORT')               # 端口
app.config['MAIL_USE_SSL'] = True           # 重要，qq邮箱需要使用SSL
app.config['MAIL_USE_TLS'] = False          # 不需要使用TLS
app.config['MAIL_USERNAME'] = get_config('Email', 'USER')  # 填邮箱
app.config['MAIL_PASSWORD'] = get_config('Email', 'PW')      # 填授权码
app.config['MAIL_DEFAULT_SENDER'] = get_config('Email', 'MAIL_DEFAULT_SENDER')  # 填邮箱，默认发送者
mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")  


@app.route("/excrcise")
def excrcise():
    output_today_exercise()
    return redirect("/send_email")


@app.route("/up_load", methods=["GET", "POST"])
def up_load_today_words():
    if request.method == 'POST':
        all_post_data = request.form.to_dict()

        write_new_words(
            str(all_post_data.get('up_cn_1')),
            all_post_data.get('up_cn_2'),
            all_post_data.get('up_cn_3'),
            all_post_data.get('up_cn_4'),
            all_post_data.get('up_en_1'),
            all_post_data.get('up_en_2'),
            all_post_data.get('up_en_3'),
            all_post_data.get('up_en_4'),
            )
        return redirect("/")
    return render_template("up_load.html", numbers=[1,2,3,4], lines = get_lines())    


@app.route("/wrong_book_check", methods=["GET", "POST"])
def wrong_book_check():
    return render_template("wrong_book_check.html")


@app.route("/wrong_book_add", methods=["GET", "POST"])
def wrong_book_add():
    exercise_words = get_exercise_words(-1)
    if request.method == 'POST':
        all_post_data = request.form.to_dict()

        write_wrong_words(all_post_data, exercise_words)

        return redirect("/")

    return render_template("wrong_book_add.html", exercise_words = exercise_words, lines = len(exercise_words))        

# 异步发送邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

@app.route('/send_email')
def send_email():
    msg = Message(subject='Hello World',
                sender=get_config('Email', 'MAIL_DEFAULT_SENDER'),  # 需要使用默认发送者则不用填
                recipients=[get_config('Email', 'RECIPIENTS'), 
                            get_config('Email', 'RECIPIENTS2')]) # 主备收件人
    # 邮件内容会以文本和html两种格式呈现，而你能看到哪种格式取决于你的邮件客户端。
    msg.body = 'sended by flask-email'
    msg.html = '<b>测试Flask发送邮件<b>'
    # get_datetime
    with app.open_resource(f'{get_datetime()}.xls') as fp:
        msg.attach(f'{get_datetime()}.xls', "excel/xls", fp.read())
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return redirect("/")
 
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)