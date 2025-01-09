CREATE TABLE webhook_payloads (
    id SERIAL PRIMARY KEY, -- Auto-incrementing ID for unique identification
    event_type VARCHAR(255) NOT NULL, -- Type of the webhook event
    payload JSON NOT NULL, -- Webhook payload data stored as JSON
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the webhook is received
);
