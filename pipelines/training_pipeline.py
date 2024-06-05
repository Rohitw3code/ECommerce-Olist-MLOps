from zenml import pipeline
from steps.ingest_data import ingest_data
from steps.clean_data import clean_data
from steps.model_train import train_model
from steps.evaluate import evaluation
import pandas as pd

@pipeline(enable_cache=True)
def train_pipeline(data_path:str):
    df = ingest_data()
    x_train, x_test, y_train, y_test = clean_data(df)
    model = train_model(x_train, x_test, y_train, y_test)
    mse, rmse = evaluation(model, x_test, y_test)

    # df = ingest_df(data_path)
    # clean_df(df)
    # train_model(df)
    # evaluate_model(df)
