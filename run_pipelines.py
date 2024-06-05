from pipelines.training_pipeline import train_pipeline
import os

if __name__ == '__main__':
    print(os.listdir())
    train_pipeline(data_path="./data/olist_customers_dataset.csv")