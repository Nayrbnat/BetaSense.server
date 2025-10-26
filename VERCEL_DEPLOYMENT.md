# Vercel Deployment Guide for BetaSense Server

## Files Created/Modified for Vercel Deployment

### 1. `api/requirements.txt`
- Contains all Python dependencies needed for the serverless function
- Removed `pip` which Vercel doesn't support
- Includes all necessary packages from your original requirements.txt

### 2. `runtime.txt`
- Specifies Python 3.11 for Vercel to use

### 3. `vercel.json`
- Updated with proper configuration
- Set `maxLambdaSize` to 15mb to accommodate all dependencies
- Added PYTHONPATH environment variable

### 4. `api/index.py`
- Enhanced path handling for better module resolution
- Added `lifespan="off"` to Mangum handler (recommended for serverless)
- Improved error handling

### 5. `betasense/src/auth/clients.py`
- Updated to only load .env file if it exists (for local dev)
- Added proper error messages when environment variables are missing
- Vercel uses its own environment variable system

## Required Environment Variables in Vercel

You MUST set these in your Vercel project dashboard:

1. **OPENAI_API_KEY** - Your OpenAI API key
2. **SUPABASE_DATABASE_URL** - Your Supabase database connection string (format: `postgresql+asyncpg://user:password@host:port/database`)
3. **NEWSDATA_API_KEY** - Your NewsData.io API key

### How to Set Environment Variables in Vercel:

1. Go to your project in Vercel dashboard
2. Click on "Settings"
3. Click on "Environment Variables"
4. Add each variable with its value
5. Make sure to select the appropriate environments (Production, Preview, Development)

## Deployment Steps

1. **Commit all changes:**
   ```bash
   git add .
   git commit -m "Configure for Vercel deployment"
   git push
   ```

2. **Vercel will automatically deploy** if you have GitHub integration enabled

3. **Or deploy manually:**
   ```bash
   vercel --prod
   ```

## Testing Your Deployment

Once deployed, test your API:

### Health Check:
```bash
curl https://your-project.vercel.app/
```

Expected response:
```json
{
  "message": "BetaSense API is running",
  "status": "ok",
  "endpoints": {
    "chat": {
      "path": "/chat",
      "method": "POST",
      "description": "Chat endpoint for BetaSense agent",
      "required_fields": ["session_id", "user_input", "password"]
    }
  }
}
```

### Chat Endpoint:
```bash
curl -X POST https://your-project.vercel.app/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "test-session-123",
    "user_input": "Hello",
    "password": "yourmumgay"
  }'
```

## Common Issues and Solutions

### Issue: 500 Internal Server Error
- **Cause**: Missing environment variables
- **Solution**: Ensure all environment variables are set in Vercel dashboard

### Issue: Module Import Errors
- **Cause**: Dependencies not installed
- **Solution**: Check that `api/requirements.txt` exists and redeploy

### Issue: Database Connection Errors
- **Cause**: Invalid SUPABASE_DATABASE_URL
- **Solution**: Verify the connection string format and credentials

### Issue: Cold Start Timeout
- **Cause**: Lambda taking too long to initialize
- **Solution**: Consider using Vercel's Edge Runtime or optimizing imports

## Vercel Limitations to Keep in Mind

1. **Function Timeout**: 10 seconds for Hobby plan, 60 seconds for Pro
2. **Function Size**: 50MB limit (we set 15MB in config)
3. **Memory**: 1024MB for Hobby plan
4. **Cold Starts**: First request after idle period may be slower

## Local Testing

To test locally before deploying:

```bash
# Install Vercel CLI
npm i -g vercel

# Run local development server
vercel dev
```

This will simulate the Vercel environment locally.

## Monitoring

After deployment, monitor your function:
- Go to Vercel Dashboard → Your Project → Deployments
- Click on a deployment to see build logs
- Check Runtime Logs for errors during execution
- Use the Vercel Analytics for performance metrics
