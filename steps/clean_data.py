import logging
import pandas as pd
from model.data_cleaning import DataCleaning,DataDivideStrategy,DataPreprocessStrategy
from zenml import step
from typing_extensions import Annotated
from typing import Tuple

@step
def clean_df(df:pd.DataFrame)->Tuple[
    Annotated[pd.DataFrame,'X_train'],
    Annotated[pd.DataFrame,'X_test'],
    Annotated[pd.DataFrame,'y_train'],
    Annotated[pd.DataFrame,'y_test']
]:
    """Data cleaning class which preprocesses the data and divides it into train and test data.

    Args:
        data: pd.DataFrame
    """

    try:
        data_cleaning = DataCleaning(df,DataPreprocessStrategy())
        preprocessed_data = data_cleaning.handle_data()

        divide_data = DataCleaning(preprocessed_data,DataDivideStrategy())
        x_train,x_test,y_train,y_test = divide_data.handle_data()
        return x_train,x_test,y_train,y_test
    except Exception as e:
        logging.error(e)
        return e
