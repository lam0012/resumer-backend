# Vercel Deployment Guide for Resumer Backend

This guide will help you deploy your FastAPI backend to Vercel.

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Account**: Your code should be in a GitHub repository
3. **Environment Variables**: You'll need your API keys

## Step-by-Step Deployment

### 1. Prepare Your Repository

Make sure your code is pushed to a GitHub repository. The following files should be in your repository root:

- `main.py` (your FastAPI app)
- `requirements.txt` (Python dependencies)
- `vercel.json` (Vercel configuration)
- `api/index.py` (Vercel handler)
- `resume_templates/` (your template files)
- `output_template/` (template files)
- All other Python modules

### 2. Set Up Vercel Project

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "New Project"
3. Import your GitHub repository
4. Vercel will automatically detect it's a Python project

### 3. Configure Environment Variables

In your Vercel dashboard:

1. Go to your project settings
2. Navigate to "Environment Variables"
3. Add the following variables:

```
GEMINI_API_KEY=your_actual_gemini_api_key
SECRET_KEY=your_secure_secret_key_here
ENVIRONMENT=production
```

**Important**: 
- Replace `your_actual_gemini_api_key` with your real Google Gemini API key
- Replace `your_secure_secret_key_here` with a strong, random secret key
- Make sure to set these for "Production", "Preview", and "Development" environments

### 4. Deploy

1. Click "Deploy" in Vercel
2. Wait for the deployment to complete
3. Your API will be available at `https://your-project-name.vercel.app`

### 5. Test Your Deployment

Test your API endpoints:

- **Health Check**: `GET https://your-project-name.vercel.app/`
- **Sign In**: `POST https://your-project-name.vercel.app/signin`
- **Templates**: `GET https://your-project-name.vercel.app/templates`

## Important Notes

### File Storage Limitations

Vercel has limitations for serverless functions:
- **Temporary files**: Files created during request processing are temporary
- **No persistent storage**: The `output/` directory won't persist between requests
- **File downloads**: Generated PDFs will only be available during the request

### Recommended Changes for Production

1. **Use external storage** (AWS S3, Google Cloud Storage) for generated files
2. **Implement file cleanup** to avoid storage issues
3. **Consider using a database** for user management instead of JSON files

### CORS Configuration

Update your CORS settings in `main.py` for production:

```python
allowed_origins = [
    "https://your-frontend-domain.com",
    "https://www.your-frontend-domain.com"
]
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all your Python files are in the repository
2. **Missing Dependencies**: Check that `requirements.txt` includes all packages
3. **Environment Variables**: Ensure all required variables are set in Vercel
4. **File Path Issues**: Use relative paths and ensure files exist

### Debugging

1. Check Vercel function logs in the dashboard
2. Use `print()` statements for debugging (they'll appear in logs)
3. Test locally with `vercel dev` before deploying

## Alternative: Hybrid Approach

If you need persistent file storage, consider:

1. **Backend on Vercel**: For API endpoints
2. **File Storage**: Use AWS S3 or similar for generated files
3. **Database**: Use a cloud database for user data

## Next Steps

1. Set up your frontend to point to the new Vercel URL
2. Update CORS settings for your frontend domain
3. Monitor the Vercel dashboard for any issues
4. Consider implementing the recommended changes for production use

## Support

- Vercel Documentation: [vercel.com/docs](https://vercel.com/docs)
- FastAPI Documentation: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- Python on Vercel: [vercel.com/docs/functions/serverless-functions/runtimes/python](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
