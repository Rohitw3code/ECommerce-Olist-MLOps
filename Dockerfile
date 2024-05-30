# FROM ubantu

FROM python:3.9-slim


RUN apt-get update && apt-get install -y libgomp1

ADD steps steps
ADD pipelines pipelines
ADD data data
# ADD .zen .zen

COPY .gitignore .gitignore
COPY __init__.py __init__.py
COPY requirements.txt requirements.txt
COPY run_pipelines.py run_pipelines.py

RUN pip install zenml==0.58.0
RUN pip install pandas==1.3.5

RUN pip install -r requirements.txt
RUN pip install "zenml[server]"
RUN zenml init
RUN zenml connect
RUN zenml up

ENTRYPOINT [ "python","run_pipelines.py" ]

