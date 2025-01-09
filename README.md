### webhook-demo
A demo of how to use github webhooks to fire events

### Start
```bash
pip install flask

python app.py

ngrok http 5000

https://2565-2600-1700-59e0-9df0-8f85-79ed-6300-6992.ngrok-free.app/webhook
```
### Payload
```json
{
  "ref": "refs/heads/main",
  "before": "abc123...",
  "after": "def456...",
  "repository": {
    "id": 123456789,
    "name": "example-repo",
    "full_name": "your-username/example-repo",
    "url": "https://github.com/your-username/example-repo"
  },
  "pusher": {
    "name": "your-username",
    "email": "you@example.com"
  },
  "commits": [
    {
      "id": "def456...",
      "message": "Commit message",
      "timestamp": "2025-01-01T12:00:00Z",
      "author": {
        "name": "your-username",
        "email": "you@example.com"
      }
    }
  ]
}

```