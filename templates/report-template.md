# Report Template

## Backend
- Hosted backend URL (HTTPS): `<ADD_URL_HERE>`
- Backend repository URL: `<ADD_REPO_URL_HERE>`

## Frontend
- Hosted frontend URL (HTTPS): `<ADD_URL_HERE>`
- Frontend repository URL: `<ADD_REPO_URL_HERE>`

## Reflection: Deployment (GitHub -> CSC Rahti)
I learned how to connect GitHub pushes to automatic builds in Rahti by configuring a BuildConfig webhook. I also learned to expose the service via an HTTPS route and to verify deployment from build logs and route status.

## Reflection: Docker
I created a Dockerfile and docker-compose setup to run the backend locally in a reproducible way. Environment variables made configuration clearer, especially for debug mode and host binding. The biggest benefit was getting the same runtime behavior regardless of local machine setup.

## Notes on HTTPS integration
The frontend now calls backend over HTTPS only, which avoids browser mixed-content blocks and better matches production deployment.
