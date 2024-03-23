import pytest
from loan_pred_model.config import config
from loan_pred_model.processing.data_handling import load_dataset
from loan_pred_model.predict import generate_predictions

# import pytest
# from config import config
# from processing.data_handling import load_dataset
# from predict import generate_predictions



# output from predict script not null
# output from predict script is str data type
# the output is Y for an example data


@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[:1]
    result = generate_predictions(single_row)
    return result

def test_single_pred_not_none(single_prediction): # output is not none
    assert single_prediction is not None

def test_single_pred_str_type(single_prediction): # data type is string
    assert isinstance(single_prediction.get('prediction')[0],str)

def test_single_pred_validate(single_prediction): # check the output is Y
    assert single_prediction.get('prediction')[0] == 'Y'


############################################################################333
# import pytest
# from ..config import config  # Importing config from the same package
# from ..processing.data_handling import load_dataset
# from ..predict import generate_predictions

# @pytest.fixture
# def single_prediction():
#     test_dataset = load_dataset(config.TEST_FILE)
#     single_row = test_dataset[:1]
#     result = generate_predictions(single_row)
#     return result

# def test_single_pred_not_none(single_prediction):
#     assert single_prediction is not None

# def test_single_pred_str_type(single_prediction):
#     assert isinstance(single_prediction.get('prediction')[0], str)

# def test_single_pred_validate(single_prediction):
#     assert single_prediction.get('prediction')[0] == 'Y'
