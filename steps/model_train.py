import logging
import pandas as pd
from zenml import steps

@steps
def train_model(df:pd.DataFrame)->pd.DataFrame:
    pass