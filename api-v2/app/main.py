import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import aporia
import pandas as pd
import uuid


app = FastAPI(debug=False)


            
###### Initiate Aporia ######
aporia.init(token=XXXXXXXXXXXXXXX", 
            environment="local-dev", 
            verbose=True)


apr_model_version = "sandbox-version"
apr_model_type = "binary"
apr_features_schema = {
    "X1": "numeric",
    "X2": "numeric",
    "X3": "numeric",
    "X4": "numeric",
    "X5": "numeric",
    "X6": "numeric",
    "X7": "numeric",
    "X8": "numeric",
    "X9": "numeric",
    "X10": "numeric",
    "X11": "numeric",
    "X12": "numeric",
    "X13": "numeric",
    "X14": "numeric",
    "X15": "numeric",
    "X16": "numeric",
    "X17": "numeric",
    "X18": "numeric",
    "X19": "numeric",
    "X20": "numeric",
    "X21": "numeric",
    "X22": "numeric",
    "X23": "numeric",
    "X24": "numeric",
    "X25": "numeric",
    "X26": "numeric",
    "X27": "numeric",
    "X28": "numeric",
    "X29": "numeric",
    "X30": "numeric",
    "X31": "numeric",
    "X32": "numeric",
    "X33": "numeric",
    "X34": "numeric",
    "X35": "numeric",
    "X36": "numeric",
    "X37": "numeric",
  
}






apr_predictions_schema = {
    "Retraso": "numeric",
}


apr_model = aporia.create_model_version(
    model_id="scl-aeropuerto",
    model_version=apr_model_version,
    model_type=apr_model_type,
    features=apr_features_schema,
    predictions=apr_predictions_schema
)


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
    
    list_1 = prediction.tolist()
    colums_name=[]
    for i in apr_features_schema.keys():
       
        colums_name.append(i)

  
  #  id_feature_column_name = 'pred_1337'
    apr_features_df = pd.DataFrame(data.X).T
 
    apr_features_df.columns=colums_name
    apr_prediction_df = pd.DataFrame(list_1).T
    apr_prediction_df.columns=["Y"]
    apr_model = aporia.Model(
    model_id="scl-aeropuerto",
    model_version=apr_model_version)



    apr_model.log_prediction(
             id=str(uuid.uuid4()),
            features=apr_features_df.to_dict('records')[0],
            predictions=apr_prediction_df.to_dict('records')[0]
        )

    apr_model.flush()




    return {'y_pred': list_1[0]}

#if __name__ == '__main__':
 #   print(4)
  #  uvicorn.run(app, host='0.0.0.0', workers=5)
