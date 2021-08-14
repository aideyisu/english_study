from flask import Flask, render_template, request
from write_words import write_new_words
from get_words import get_lines
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    # return "<p>Hello, World!</p>"
    
    if request.method == 'POST':
        all_post_data = request.form.to_dict()

        print(
            all_post_data.get('up_cn_1'),
            all_post_data.get('up_cn_2'),
            all_post_data.get('up_cn_3'),
            all_post_data.get('up_cn_4'),
            all_post_data.get('up_en_1'),
            all_post_data.get('up_en_2'),
            all_post_data.get('up_en_3'),
            all_post_data.get('up_en_4'),
            )

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

app.run(debug = True, host = '0.0.0.0', port = 5000)