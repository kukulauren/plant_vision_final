import pickle

with open('/Users/khinmyatnoe/PycharmProjects/finalproject/app/RF.pkl', 'rb') as file:
    model = pickle.load(file)
def predict(features):
    prediction = model.predict(features)
    return prediction