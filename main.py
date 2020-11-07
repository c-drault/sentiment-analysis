from flask import *
app = Flask(__name__)
import sys
import joblib

model = joblib.load("project/saved_model")
vectorizer = joblib.load("project/saved_vectorizer")

def sentiment_analysis(sentence):
    X_new = vectorizer.transform(sentence)
    result = model.predict(X_new)[0]
    if result > 0:
        return "positive"
    if result < 0:
        return "negative"
    if result == 0:
        return "neutral"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['phrase'])
        sentence_requested = request.form['phrase']
        sentence = []
        sentence.append(sentence_requested)
        result = sentiment_analysis(sentence)
        return redirect(url_for('index', result=result))
      
    result = request.args.get('result')
    if result is None:
        return render_template('index.html')
    return render_template('index.html', result=result)


if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0')
