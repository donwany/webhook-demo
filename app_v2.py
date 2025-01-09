from flask import Flask, request, jsonify
import psycopg2
import json

# Initialize Flask app
app = Flask(__name__)

# Database connection details
DB_HOST = "localhost"
DB_NAME = "webhook_db"
DB_USER = "your_user"
DB_PASSWORD = "your_password"

# Connect to the database
def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Parse the webhook payload
    payload = request.json
    event_type = request.headers.get("X-Event-Type", "unknown")

    # Store data into the database
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO webhook_payloads (event_type, payload)
            VALUES (%s, %s)
            """,
            (event_type, json.dumps(payload))
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"Error storing webhook data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
