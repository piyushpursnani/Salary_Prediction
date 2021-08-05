from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('hiring_model.pkl')


@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/predict', methods=['POST'])
def predict():

    exp=request.form.get('experience')
    score=request.form.get('test_score')
    interview_score=request.form.get('interview_score')

    pred = model.predict(([[int(exp), int(score), int(interview_score)]]))

    output = round(pred[0] , 2)


    
    return render_template('base.html', prediction_text = f"employee salary will be $ {output}")


if __name__=='__main__':
    app.run(debug =True)