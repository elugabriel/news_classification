from flask import Flask, render_template, url_for, flash, redirect, request
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

app = Flask(__name__)

cv = pickle.load(open("countvectorizer.pkl", "rb"))
classifier = pickle.load(open("model.pkl", "rb"))



@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
   
    cv = pickle.load(open("countvectorizer.pkl", "rb"))
    #cv = CountVectorizer(max_features = 5000)
    classifier = pickle.load(open("model.pkl", "rb"))
    word = request.form["news"]
   
    y_pred1 = cv.transform([word])
    yy = classifier.predict(y_pred1)
    result = ""
    if yy == [0]:
        result = "Business News"
    elif yy == [1]:
        result = "Politics News"
    elif yy == [2]:
        result = "Tech News"
    elif yy == [3]:
        result = "Sports News"
    elif yy == [1]:
        result = "Entertainment News"
    return render_template('result.html', prediction=result)
   



if __name__ == '__main__':
    app.run(debug=True)