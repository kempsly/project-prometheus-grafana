import os 
import pandas as pd  
import joblib 
from loan_pred_model.config import config 
# from config import config 



# function to load the data
def load_dataset(filename):
    filepath = os.path.join(config.DATAPATH, filename)
    _data = pd.read_csv(filepath)
    # _data = pd.read_csv(filepath)
    return _data 

# Performing the serialization of the model
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_path)
    print(f"Model has been saved under the name {config.MODEL_NAME}")

# Performing deserialization of the model   
def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    loaded_model = joblib.load(save_path)
    print("Model has been loaded")
    return loaded_model 
