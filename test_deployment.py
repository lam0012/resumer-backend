#!/usr/bin/env python3
"""
Test script to debug deployment issues
Run this locally to test your backend before deploying
"""

import requests
import json
import os
from pathlib import Path

# Configuration
BASE_URL = "https://resume-build-backend.onrender.com"  # Replace with your Render URL
LOCAL_URL = "http://localhost:8090"  # For local testing

def test_endpoints(base_url):
    print(f"Testing endpoints at: {base_url}")
    print("=" * 50)
    
    # Test health check
    try:
        response = requests.get(f"{base_url}/")
        print(f"✅ Health check: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"❌ Health check failed: {e}")
    
    # Test login (you'll need valid credentials)
    try:
        login_data = {
            "username": "your_username",  # Replace with actual username
            "password": "your_password"   # Replace with actual password
        }
        response = requests.post(f"{base_url}/signin", json=login_data)
        if response.status_code == 200:
            token = response.json()["token"]
            headers = {"Authorization": f"Bearer {token}"}
            print(f"✅ Login successful")
            
            # Test debug files endpoint
            try:
                response = requests.get(f"{base_url}/debug/files", headers=headers)
                print(f"✅ Debug files: {response.status_code} - {response.json()}")
            except Exception as e:
                print(f"❌ Debug files failed: {e}")
                
            # Test templates endpoint
            try:
                response = requests.get(f"{base_url}/templates", headers=headers)
                print(f"✅ Templates: {response.status_code} - {response.json()}")
            except Exception as e:
                print(f"❌ Templates failed: {e}")
                
        else:
            print(f"❌ Login failed: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"❌ Login test failed: {e}")

def test_pdf_download(base_url, filename):
    """Test PDF download endpoint"""
    print(f"\nTesting PDF download: {filename}")
    try:
        response = requests.get(f"{base_url}/download/resume/{filename}")
        print(f"PDF Download: {response.status_code}")
        if response.status_code == 200:
            print(f"✅ PDF downloaded successfully ({len(response.content)} bytes)")
        else:
            print(f"❌ PDF download failed: {response.text}")
    except Exception as e:
        print(f"❌ PDF download test failed: {e}")

if __name__ == "__main__":
    print("🔍 Testing Backend Deployment")
    print("=" * 50)
    
    # Test your deployed backend
    test_endpoints(BASE_URL)
    
    # Test PDF download (replace with actual filename)
    test_pdf_download(BASE_URL, "a-sebastian_resume.pdf")
    
    print("\n" + "=" * 50)
    print("📝 Instructions:")
    print("1. Update BASE_URL with your actual Render URL")
    print("2. Update login credentials in the script")
    print("3. Run: python test_deployment.py")
    print("4. Check the output for any errors")
