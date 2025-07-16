from flask import Flask, request, render_template
from model import model

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        hours = float(request.form['hours'])
        prediction = model.predict([[hours]])[0]
        return render_template('index.html', prediction_text=f"Predicted Score = {prediction:.2f}")
    except:
        return render_template('index.html', prediction_text="Invalid input.")

if __name__ == '__main__':
    app.run(debug=True)
