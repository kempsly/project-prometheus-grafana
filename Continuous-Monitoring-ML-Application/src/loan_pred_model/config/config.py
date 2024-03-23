import pathlib
import os
import loan_pred_model
# from . import loan_pred_model



# current_directory = os.path.dirname(os.path.realpath(__file__))
# PACKAGE_ROOT = os.path.dirname(current_directory)
PACKAGE_ROOT = pathlib.Path(loan_pred_model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent


DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = 'train.csv'

TEST_FILE = 'test.csv'

MODEL_NAME = 'loan_classfication.pkl'

SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, "trained_models")

TARGET = 'Loan_Status'

#Features that have been kept in other to train the model
FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']

# Numerical features
NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

# Categorical features 
CAT_FEATURES = ['Gender',
 'Married',
 'Dependents',
 'Education',
 'Self_Employed',
 'Credit_History',
 'Property_Area']

# Feature to encode - it is same as Categorical features
FEATURES_TO_ENCODE = ['Gender',
 'Married',
 'Dependents',
 'Education',
 'Self_Employed',
 'Credit_History',
 'Property_Area']

FEATURE_TO_MODIFY = ['ApplicantIncome']
FEATURE_TO_ADD = 'CoapplicantIncome'

DROP_FEATURES = ['CoapplicantIncome']

# Feature that need to be transformed by taking their log
LOG_FEATURES = ['ApplicantIncome', 'LoanAmount']
