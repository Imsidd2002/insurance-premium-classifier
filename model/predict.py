import pickle
import pandas as pd



# import the ml model
with open('./model/model.pkl', 'rb') as f:
    model = pickle.load(f)

#given by us but in real world scenario verision is extracted from MLFlow
MODEL_VERSION = '1.0.0'


#get class labels from model(impt for matching probabilities to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input : dict):
    df = pd.DataFrame([user_input])
    
    #predict the class
    predicted_class = model.predict(df)[0]
    
    #get probabilities of all the classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)
    
    #create mapping: {classname : probabilities}
    class_probs = dict(zip(class_labels,map(lambda p: round(p,4),probabilities)))
    return {
        "predicted_category" : predicted_class,
        "confidence" : round(confidence,4),
        "class_probabilites": class_probs
    }