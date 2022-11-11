import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

import pandas as pd
import uuid


app = FastAPI(debug=False)




with open("pickle_model.pkl", 'rb') as file:
        clf = pickle.load(file)
        print(clf)

class FeatureDataInstance(BaseModel):
    """Define JSON data schema for prediction requests."""
    X: list


@app.post('/api/v1/', status_code=200)
async def predict(data: FeatureDataInstance):
    """Generate predictions for data sent to the /api/v1/ route."""
   
  #  print(data.X)
    prediction = clf.predict([data.X])
    
   # print(prediction)
    # print(prediction)
    
    list_1 = prediction.tolist()
    

    return {'y_pred': list_1[0]}

#if __name__ == '__main__':
 #   print(4)
  #  uvicorn.run(app, host='0.0.0.0', workers=5)
