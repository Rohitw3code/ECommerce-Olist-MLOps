from zenml import pipeline
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluate import evaluate_model
import pandas as pd

@pipeline
def train_pipeline(data_path:str):
    df = ingest_df(data_path)
    clean_df(df)
    train_model(df)
    evaluate_model(df)