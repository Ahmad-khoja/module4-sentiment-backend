# Sentiment Backend + Deployment Task

This repository contains a sentiment analysis backend in Python with Docker support and deployment instructions for CSC Rahti.

## 1) Backend Run (local Python)

```bash
cd backend
cp .env.example .env
pip install -r requirements.txt
python app.py
```

Backend endpoints:
- `GET /health`
- `POST /analyze`

Example request:

```bash
curl -X POST http://localhost:8000/analyze \\
  -H "Content-Type: application/json" \\
  -d '{"text":"I really like this course"}'
```

## 2) Docker Run (required in assignment)

```bash
cp backend/.env.example backend/.env
docker compose up --build
```

Test:

```bash
curl http://localhost:8000/health
```

Stop:

```bash
docker compose down
```

## 3) Required env variables

At least two are used:
- `DEBUG` (true/false)
- `HOST_IP` (default `0.0.0.0`)

Also used:
- `PORT`
- `FRONTEND_ORIGIN`

## 4) GitHub -> CSC Rahti webhook pipeline

1. Push this code to GitHub.
2. Login to Rahti/OpenShift (`oc login ...`).
3. Create resources:

```bash
oc apply -f rahti-openshift.yaml
```

4. Get webhook URL from build config:

```bash
oc describe bc/sentiment-backend
```

Look for GitHub webhook URL.

5. In GitHub repo:
- Settings -> Webhooks -> Add webhook
- Payload URL = URL from build config
- Content type = `application/json`
- Secret = same value as `CHANGE_ME_WEBHOOK_SECRET`
- Events: Just the push event

6. Push to `main`, verify build starts in Rahti.
7. Get route:

```bash
oc get route sentiment-backend
```

Use the `https://...` route URL in frontend.

## 5) Frontend integration (Module 3)

Use `frontend-integration-example/sentimentApi.js` and configure env:

```bash
VITE_SENTIMENT_API_URL=https://your-rahti-backend-url
```

Important: use HTTPS backend URL in frontend to avoid mixed-content issues.

## 6) Report links checklist

Add these links to your report:
- Backend hosted HTTPS URL
- Backend GitHub repository URL
- Modified frontend hosted HTTPS URL
- Modified frontend GitHub repository URL

You can use `docs/report-template.md` as a base.
