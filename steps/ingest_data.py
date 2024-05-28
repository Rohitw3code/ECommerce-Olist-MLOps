import logging
import pandas as pd
from zenml import steps

class IngestData:
    """
    Ingestion the data from the data_path
    """
    def __init__(self,data_path:str) -> None:
        self.data_path = data_path
    
    def get_data(self):
        logging.info(f'Ingestion data from {self.data_path}')
        return pd.read_csv(self.data_path)
    

@steps
def ingest_df(data_path: str) -> pd.DataFrame:
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        print(f"Error ingesting data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
