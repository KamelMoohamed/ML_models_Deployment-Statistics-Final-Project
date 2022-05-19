import os
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template

from sentiment_analysis import SentimentAnalysis
from image_classification import ImagaeClassification


# Flask APP
app = Flask(__name__, template_folder="templetes")


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('homeclass.html')


@app.route('/image_prediction', methods=['GET', 'POST'])
def image_classification():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        imagaeClassification = ImagaeClassification()

        return imagaeClassification.predict(file_path)
    return None

@app.route('/sentiment_prediction', methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method == 'POST':
        # Get the file from post request
        text = request.form['text']
        
        sentiment = SentimentAnalysis()
        
        return sentiment.predict(text)
    return None


if __name__ == '__main__':
    app.run(debug=True) 