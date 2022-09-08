PROJECT=tribal-datum-263010

# build container image using Cloud Build
gcloud builds submit --tag gcr.io/$PROJECT/house-price-api

# deploy container image to Cloud Run
gcloud run deploy --image gcr.io/$PROJECT/house-price-api \
  --platform managed \
  --region europe-west1 \
  --port 8080 \
  --allow-unauthenticated
