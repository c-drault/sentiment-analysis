from flask import *
app = Flask(__name__)
import sys
import joblib


model = joblib.load("saved_model")
vectorizer = joblib.load("saved_vectorizer")

def sentiment_analysis(sentence):
    X_new = vectorizer.transform(sentence)
    result = model.predict(X_new)[0]
    if result > 0:
        print("Hmmmm... your sentence is positive")
    if result < 0:
        print("Hmmmm... your sentence is negative")
    if result == 0:
        print("Hmmmm... your sentence is neutral")

    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['phrase'])
        sentence_requested = request.form['phrase']
        #Request the ML app
        sentence = []
        sentence.append(sentence_requested)
        sentiment_analysis(sentence)
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
     app.run(debug=True,host='127.0.0.1')
