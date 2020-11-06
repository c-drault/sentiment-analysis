from flask import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['phrase'])
        #Request the ML app
        return redirect(url_for('index'))
    return render_template('index.html')
