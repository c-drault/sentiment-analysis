from flask import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['phrase'])
        #Request the ML app


        #result is the value of the sentiment
        result = "Lorem ipsum"
        return redirect(url_for('index', result=result))
    result = request.args.get('result')
    if result is None:
    	return render_template('index.html')
    return render_template('index.html', result=result)
