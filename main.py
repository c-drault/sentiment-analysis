from flask import Flask, session, redirect, url_for, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['phrase'])
        #Request the ML app
        return redirect(url_for('index'))
    return '''
        <form method="POST">
            <input type="text" name="phrase">
            <input type="submit" value="Valider">
        </form>
    '''
