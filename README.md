
# ZenML and MLflow Integration

This project demonstrates how to set up ZenML with MLflow as the experiment tracker and model deployer.

## Prerequisites

- Ubuntu
- Python 3.12
- `venv` for managing virtual environments

## Setup Instructions

### Step 1: Create a Virtual Environment

First, create and activate a virtual environment:

```bash
python3.12 -m venv zenml_env
source zenml_env/bin/activate


pip install zenml['server']
zenml init
zenml down
zenml up
python run_pipelines.py


zenml integration install mlflow -y
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
zenml model-deployer register mlflow_tracker --flavor=mlflow
zenml stack register mlflow_stack -a default -o default -d mlflow -e mlflow_tracker --set

from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri

uri = get_tracking_uri()
print(uri)

mlflow ui --backend-store-uri "<tracking_uri>"
mlflow ui --backend-store-uri "/home/rohit/.config/zenml/local_stores/efbcf4eb-1b57-4f7f-ad0c-fcba66eed705/mlruns"

To deploy the pipeline
python run_deployment.py --config predict
