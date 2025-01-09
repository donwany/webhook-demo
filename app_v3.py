from flask import Flask, request, jsonify
from pymongo import MongoClient
import datetime

# Initialize Flask app
app = Flask(__name__)

# MongoDB connection details
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "webhook_db"
COLLECTION_NAME = "webhook_payloads"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Parse the webhook payload
    payload = request.json
    event_type = request.headers.get("X-Event-Type", "unknown")

    # Prepare the data to insert into MongoDB
    webhook_data = {
        "event_type": event_type,
        "payload": payload,
        "received_at": datetime.datetime.utcnow()
    }

    # Insert data into MongoDB
    try:
        collection.insert_one(webhook_data)
        return jsonify({"status": "success", "message": "Webhook data stored"}), 200
    except Exception as e:
        print(f"Error storing webhook data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
