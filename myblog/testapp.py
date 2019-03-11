from flask import Flask, render_template
import markdown
import yaml
from myblog.extensions import bootstrap
from myblog.forms import UploadForm

app = Flask(__name__)
app.secret_key = 'secret string'
bootstrap.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    return render_template('admin/new_post2.html', form=form)


if __name__ == "__main__":

    app.run(host='127.0.0.1', port=8080, debug=True)
