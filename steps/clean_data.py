import logging
import pandas as pd
from zenml import steps

@steps
def clean_df(df:pd.DataFrame)->pd.DataFrame:
    pass