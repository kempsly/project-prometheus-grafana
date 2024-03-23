import os
from loan_pred_model.config import config 
# # from loan_pred_model import config 

 
    
with open(os.path.join(config.PACKAGE_ROOT,'VERSION')) as v_file:
    __version__ = v_file.read().strip()

# __version__ = "0.0.6"
