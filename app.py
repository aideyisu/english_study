from flask import Flask, render_template, request, redirect
from write_words import write_new_words
from get_words import get_lines
from main import output_today_exercise
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  


@app.route("/excrcise")
def excrcise():
    output_today_exercise()
    return redirect("/")


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
    return render_template("up_load.html", numbers=[1,2,3,4], lines = get_lines())    


@app.route("/wrong_book_check", methods=["GET", "POST"])
def wrong_book_check():
    return render_template("wrong_book_check.html")


@app.route("/wrong_book_add", methods=["GET", "POST"])
def wrong_book_add():
    return render_template("wrong_book_add.html")        


app.run(debug = True, host = '0.0.0.0', port = 5000)