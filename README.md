# House Prices Prediction API

**Ames Housing Dataset** can be found on Kaggle [here](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)

* GCP Project: My First Project
* AI Platform Notebook: `house-prices-regression`
* Dataset: `gs://laxmi-prajapat-sandbox/house-prices-regression/data`
* Model: `gs://laxmi-prajapat-sandbox/house-prices-regression/model`
* Artifacts: `gs://laxmi-prajapat-sandbox/house-prices-regression/artifacts`
* Service account: `house-price-regression@tribal-datum-263010.iam.gserviceaccount.com`

## Prerequisites

* Python 3.7
* Google Cloud SDK

## Model

Keras model was trained in `house-prices-regression.ipynb` notebook using Functional API.

## Local

Create virtual environment:
```
virtualenv -p python3.7 house-env
source house-env/bin/activate
pip install -r requirements.txt
```

Enable service account:
```
export GOOGLE_APPLICATION_CREDENTIALS=key.json
```

Run Flask application on http://127.0.0.1:5000/:
```
python api.py
```

Send request:
```
bash test-api.sh
```

Example request - see `request.json`:
```
{
  "houseId": 2884
}
```

Example response:
```
{
  "houseId": 2884,
  "price": "135557.97",
  "timestamp": "2020-04-25 20:13:34"
}
```

## App Engine

**The folder structure `app-engine/` is as follows:**

The files that must be present -
* `app.yaml` - configuration file
* `main.py` - application
* `requirements.txt` - dependencies

Other files -
* `deploy-app.sh` - deploy application to App Engine
* `.gcloudignore` - files to ignore when deploying application
* `test-app-engine-api.sh` - send example request

Deploy application to App Engine:
```
bash deploy-app.sh
```

Send example request:
```
bash test-app-engine-api.sh
```

## Cloud Run

Enable Cloud Build and Cloud Run APIs.

**The folder structure `cloud-run/` is as follows:**

The files that must be present -
* `.dockerignore` - files to ignore when creating Docker image
* `Dockerfile` - specify Docker image
* `main.py` - application
* `requirements.txt` - dependencies

Other files -
* `deploy-container.sh` - build image and deploy
* `test-cloud-run-api.sh` - send example request

Create image and deploy to Cloud Run:
```
bash deploy-container.sh
```

Send example request:
```
bash test-cloud-run-api.sh
```
