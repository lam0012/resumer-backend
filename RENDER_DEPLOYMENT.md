# Render.com Deployment Guide for Resumer Backend

This guide will help you deploy your FastAPI backend to Render.com.

## Step-by-Step Deployment Instructions

### 1. **Configure Render Settings**

Based on your screenshot, here are the correct settings:

#### **Source Code**
- ✅ Already connected: `smile-dev49 / resume-build-backend`
- ✅ Last updated: `4m ago`

#### **Name**
- ✅ Current: `resume-build-backend` (you can keep this or change it)

#### **Language**
- ✅ Current: `Python 3` (correct)

#### **Branch**
- ✅ Current: `main` (correct)

#### **Region**
- ✅ Current: `Oregon (US West)` (good choice)

#### **Root Directory**
- Leave empty (unless your app is in a subdirectory)

#### **Build Command**
```
pip install -r requirements.txt
```

#### **Start Command** ⚠️ **FIX THIS**
Replace the current value with:
```
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

### 2. **Environment Variables**

After creating the service, you'll need to add environment variables:

1. Go to your service dashboard
2. Click on "Environment" tab
3. Add these variables:

```
GEMINI_API_KEY=your_actual_gemini_api_key
SECRET_KEY=your_secure_secret_key_here
ENVIRONMENT=production
```

### 3. **Deploy**

1. Click "Create Web Service" button
2. Wait for the build to complete (usually 2-5 minutes)
3. Your API will be available at: `https://resume-build-backend.onrender.com`

### 4. **Test Your Deployment**

Test these endpoints:
- **Health Check**: `GET https://your-app-name.onrender.com/`
- **Sign In**: `POST https://your-app-name.onrender.com/signin`
- **Templates**: `GET https://your-app-name.onrender.com/templates`

## Important Notes

### ✅ **Advantages of Render over Vercel for your app:**
- **Persistent file storage** - Generated PDFs will be saved
- **Longer request timeout** - Better for AI processing
- **More suitable for FastAPI** - Better Python support
- **File downloads work** - Users can download generated files

### 🔧 **Configuration Details:**

**Start Command Breakdown:**
- `gunicorn` - WSGI server
- `main:app` - Points to your FastAPI app in main.py
- `-w 4` - 4 worker processes
- `-k uvicorn.workers.UvicornWorker` - ASGI worker for FastAPI
- `--bind 0.0.0.0:$PORT` - Bind to Render's port

### 📁 **File Structure Requirements:**
Make sure these files are in your repository:
- `main.py` (your FastAPI app)
- `requirements.txt` (with gunicorn added)
- `resume_templates/` (template files)
- `output_template/` (template files)
- All Python modules

### 🚨 **Common Issues & Solutions:**

1. **Build Fails:**
   - Check that all dependencies are in requirements.txt
   - Ensure Python version compatibility

2. **App Won't Start:**
   - Verify the start command is correct
   - Check environment variables are set

3. **File Generation Issues:**
   - Ensure output directory exists
   - Check file permissions

### 🔄 **Auto-Deploy:**
- Render will automatically redeploy when you push to your main branch
- You can disable this in settings if needed

### 💰 **Pricing:**
- Free tier: 750 hours/month
- Paid plans start at $7/month for always-on service

## Next Steps After Deployment:

1. **Test all endpoints** to ensure everything works
2. **Update your frontend** to use the new Render URL
3. **Monitor logs** in the Render dashboard
4. **Set up custom domain** (optional)

## Support Resources:

- Render Documentation: [render.com/docs](https://render.com/docs)
- FastAPI on Render: [render.com/docs/deploy-fastapi](https://render.com/docs/deploy-fastapi)
- Gunicorn Configuration: [docs.gunicorn.org](https://docs.gunicorn.org)

Your FastAPI backend is now ready for Render deployment! 🚀
