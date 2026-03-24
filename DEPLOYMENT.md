# React Frontend Deployment on Appwrite

This guide explains how to deploy your React frontend to Appwrite or other hosting platforms.

## Prerequisites

- Node.js 16+ installed
- npm or yarn package manager
- Appwrite account (optional, for Appwrite hosting)

## Local Development Setup

### 1. Install Dependencies

```bash
cd frontend/my-app
npm install
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Update the variables:

- `REACT_APP_API_URL`: Your backend API URL (default: http://127.0.0.1:8000)
- `REACT_APP_APPWRITE_PROJECT_ID`: Your Appwrite project ID (if using Appwrite services)

### 3. Start Development Server

```bash
npm start
```

The app will run on http://localhost:3000

## Update API Calls to Use Environment Variables

To use the centralized API configuration, update your components to import from `config/api.js`:

```javascript
import { API_ENDPOINTS } from "../config/api";

// Instead of: fetch('http://127.0.0.1:8000/api/products/')
// Use: fetch(API_ENDPOINTS.products)
```

## Production Build

### 1. Build the Application

```bash
npm run build
```

This creates an optimized production build in the `build/` directory.

### 2. Test Production Build Locally

```bash
npm install -g serve
serve -s build
```

## Deployment Options

### Option 1: Vercel (Recommended for React)

1. Install Vercel CLI:

```bash
npm install -g vercel
```

2. Deploy:

```bash
vercel
```

3. Set environment variables in Vercel dashboard:
   - `REACT_APP_API_URL`: Your production backend URL
   - `REACT_APP_APPWRITE_PROJECT_ID`: Your Appwrite project ID

### Option 2: Netlify

1. Install Netlify CLI:

```bash
npm install -g netlify-cli
```

2. Deploy:

```bash
netlify deploy --prod
```

3. Set environment variables in Netlify dashboard

### Option 3: Appwrite Storage (Static Hosting)

Appwrite doesn't provide traditional web hosting, but you can:

1. Build the app: `npm run build`
2. Upload the `build/` folder contents to Appwrite Storage
3. Configure a CDN or use another hosting service

**Note**: For React apps with routing, you need a server that supports SPA routing. Consider using Vercel or Netlify instead.

### Option 4: AWS S3 + CloudFront

1. Build the app
2. Upload to S3 bucket
3. Configure CloudFront for CDN
4. Set up routing for SPA

### Option 5: GitHub Pages

1. Install gh-pages:

```bash
npm install --save-dev gh-pages
```

2. Add to `package.json`:

```json
"homepage": "https://yourusername.github.io/your-repo",
"scripts": {
  "predeploy": "npm run build",
  "deploy": "gh-pages -d build"
}
```

3. Deploy:

```bash
npm run deploy
```

## Environment Variables for Production

Update `.env` for production:

```env
REACT_APP_API_URL=https://your-backend-domain.com
REACT_APP_APPWRITE_ENDPOINT=https://cloud.appwrite.io/v1
REACT_APP_APPWRITE_PROJECT_ID=your-project-id
REACT_APP_ENV=production
```

## CORS Configuration

Ensure your Django backend allows requests from your frontend domain. Update the backend's `.env`:

```env
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
```

## Proxy Configuration

The current `package.json` has a proxy set to `http://127.0.0.1:8000/`. This works for local development but won't be used in production. The environment variable `REACT_APP_API_URL` will be used instead.

## Troubleshooting

### API Connection Issues

- Verify `REACT_APP_API_URL` is set correctly
- Check CORS settings on the backend
- Ensure the backend is accessible from your deployment

### Environment Variables Not Working

- All React environment variables must start with `REACT_APP_`
- Restart the development server after changing `.env`
- Rebuild the app for production after changing variables

### Routing Issues (404 on Refresh)

- Configure your hosting provider to redirect all requests to `index.html`
- For Netlify, create a `_redirects` file in `public/`:
  ```
  /*    /index.html   200
  ```
- For Vercel, create `vercel.json`:
  ```json
  {
    "rewrites": [{ "source": "/(.*)", "destination": "/" }]
  }
  ```

## Performance Optimization

- Enable gzip compression on your hosting
- Use CDN for static assets
- Optimize images before building
- Enable caching headers
- Consider code splitting for large apps

## Recommended Stack

For best results with your Django + React setup:

1. **Backend**: Deploy Django on Railway, Render, or DigitalOcean
2. **Frontend**: Deploy React on Vercel or Netlify
3. **Database**: Use PostgreSQL on the same platform as Django
4. **Storage**: Use Appwrite Storage or AWS S3 for media files

## Support

- [Vercel Documentation](https://vercel.com/docs)
- [Netlify Documentation](https://docs.netlify.com/)
- [Create React App Deployment](https://create-react-app.dev/docs/deployment/)
