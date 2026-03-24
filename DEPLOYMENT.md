# Django Backend Deployment on Appwrite

This guide explains how to deploy your Django backend to Appwrite.

## Prerequisites

- Appwrite CLI installed (`npm install -g appwrite-cli`)
- Appwrite account and project created
- Python 3.11+ installed

## Setup Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and update the values:

```bash
cp .env.example .env
```

Update the following variables:

- `SECRET_KEY`: Generate a new Django secret key
- `ALLOWED_HOSTS`: Add your production domain(s)
- `CORS_ALLOWED_ORIGINS`: Add your frontend domain(s)
- `DATABASE_URL`: (Optional) Add your database connection string

### 3. Update Appwrite Configuration

Edit `appwrite.json` and replace `[YOUR_PROJECT_ID]` with your actual Appwrite project ID.

### 4. Login to Appwrite CLI

```bash
appwrite login
```

### 5. Initialize Appwrite Project

```bash
appwrite init project
```

Select your existing project when prompted.

### 6. Deploy Function

```bash
cd backend/project
appwrite deploy function
```

### 7. Set Environment Variables in Appwrite

In your Appwrite Console:

1. Go to Functions → django-backend
2. Navigate to Settings → Environment Variables
3. Add all variables from your `.env` file

### 8. Test the Deployment

Once deployed, you can access your Django API through the Appwrite function URL.

## Local Development

For local development, run:

```bash
python manage.py runserver
```

## Database Migration

To run migrations in production:

1. Use Appwrite Console to execute commands
2. Or use a database migration tool
3. For SQLite, you'll need to include the database file in your deployment

## Static Files

Static files are handled by WhiteNoise middleware and will be served directly by the Django application.

## Troubleshooting

### Function Timeout

If your function times out, increase the timeout in `appwrite.json`:

```json
"timeout": 30
```

### Database Connection Issues

Ensure your `DATABASE_URL` is correctly formatted and the database is accessible from Appwrite.

### CORS Errors

Update `CORS_ALLOWED_ORIGINS` in your environment variables to include your frontend domain.

## Important Notes

- SQLite is not recommended for production. Consider using PostgreSQL or MySQL.
- Make sure to set `DEBUG=False` in production.
- Keep your `SECRET_KEY` secure and never commit it to version control.
- The current setup uses Appwrite Functions. For better performance, consider using Appwrite Cloud Functions with a traditional server deployment.

## Alternative Deployment Options

For better performance and scalability, consider:

1. Deploying Django as a standalone service on platforms like Railway, Render, or DigitalOcean
2. Using Appwrite only for authentication and storage
3. Connecting your Django backend to Appwrite's APIs

## Support

For issues specific to Appwrite deployment, consult the [Appwrite Documentation](https://appwrite.io/docs).
