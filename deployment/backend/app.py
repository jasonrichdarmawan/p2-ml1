import joblib
from keras.models import load_model
from tensorflow_addons.metrics import F1Score
import pandas as pd

from flask import Flask, request, jsonify
import numpy as np

# Load the sequential improved model
with open('./models/preprocessor.pkl', 'rb') as file_1:
    prep = joblib.load(file_1)
    
model = load_model(
    filepath='./models/seq_imp.h5',
    custom_objects={
        'Addons>F1Score': F1Score(num_classes=1, average='macro', threshold=0.3)
    }
)

# Database simulation
db = pd.read_csv('./db/WA_Fn-UseC_-Telco-Customer-Churn.csv')
    
# App Initialization
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    args = request.json
    
    customerID = args.get('customerID')
    
    # guard clause
    if customerID == None or type(customerID) != list:
        return "Bad Request", 400
    
    data = db.loc[db['customerID'].isin(customerID)]
    
    X_final = prep.transform(X=data)
    
    y_pred_proba = model.predict(x=X_final)
    
    y_pred = np.where(y_pred_proba >= 0.3, 'Yes', 'No')
    
    return jsonify(
        Churn = y_pred.reshape(-1,).tolist(),
        customerID = customerID
    )

# when the appy is deploy, the __name__ is app instead of __main__
if __name__ == '__main__':
    # host='0.0.0.0' to have have the server available externally as well.
    # make sure to remove parameter port when deploying.
    app.run(host='0.0.0.0', port=5002)