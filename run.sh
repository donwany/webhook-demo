#!/bin/bash

curl -X POST \
-H "Content-Type: application/json" \
-H "X-Event-Type: test-event" \
-d '{"message": "Hello, webhook!"}' http://localhost:5000/webhook
