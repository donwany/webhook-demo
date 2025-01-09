from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route to receive the webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    print("Server started ....")
    # Parse the JSON payload
    data = request.json

    # Example: Log the event type and payload
    event_type = request.headers.get('X-GitHub-Event', 'Unknown')
    print(f"Received event: {event_type}")
    print(f"Payload: {data}")

    # Respond to GitHub to acknowledge receipt
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)
