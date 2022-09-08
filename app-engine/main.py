from datetime import datetime
import pickle
from io import BytesIO
from google.cloud import storage

from flask import Flask, jsonify, request, abort

PORT = 8080
GCS_BUCKET = 'laxmi-prajapat-sandbox'
PREDICTIONS = 'house-prices-regression/predictions.pkl'

storage_client = storage.Client()

def pickle_load(filename):
    """Load pickle file.
    """
    with open(filename, 'rb') as fr:
        return pickle.load(fr)

def download_blob(client, bucket_name, blob_name):
    """Download GCS object in memory.
    """
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    content = blob.download_as_string()
    return pickle.load(BytesIO(content))

print('Loading predictions...')
predictions = download_blob(storage_client, GCS_BUCKET, PREDICTIONS)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST'])
def prices():
    try:
        if request.method != 'POST':
            abort(405)

        r = request.get_json()
        id = r.get('houseId')
        t = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

        if not id:
            abort(400)

        payload = {
            'houseId': id,
            'price': str(predictions.get(id)),
            'timestamp': t
        }
        return jsonify(payload)

    except Exception:
        abort(500, 'Unable to return house price predictions.')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=PORT, debug=True)
