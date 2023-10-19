import pickle

with open("../hw/hw5/dv.bin", 'rb') as file:
    dv = pickle.load(file)

with open("../hw/hw5/model1.bin", 'rb') as file:
    model = pickle.load(file)

print(model.predict_proba(dv.transform({"job": "retired", "duration": 445, "poutcome": "success"})))