
from flask import Flask, request, jsonify
import pickle

app = Flask("predict")

with open("dv.bin", 'rb') as file:
    dv = pickle.load(file)

with open("model1.bin", 'rb') as file:
    model = pickle.load(file)


@app.route("/predict", methods=["POST"])
def predict():

	client = request.get_json()
	
	X = dv.transform([client])
	y_pred = model.predict_proba(X)[0, 1]
	credit = y_pred >= 0.5
	
	result = {'credit_probability': float(y_pred), 'credit': bool(credit)}

	return jsonify(result)


if __name__ == "__main__":

	app.run(debug=True, host='0.0.0.0', port=9696)