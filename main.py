"""
Appwrite Function Entry Point
This file serves as the entry point for Appwrite Functions deployment
"""
import os
import sys
from pathlib import Path

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line

# Create Django WSGI application
application = WSGIHandler()

def main(context):
    """
    Main function for Appwrite Function
    
    Args:
        context: Appwrite function context
        
    Returns:
        Response object
    """
    try:
        # Get request details from context
        method = context.req.method
        path = context.req.path
        headers = context.req.headers
        body = context.req.body
        
        # Create a WSGI-compatible environment
        environ = {
            'REQUEST_METHOD': method,
            'PATH_INFO': path,
            'SERVER_NAME': 'appwrite',
            'SERVER_PORT': '443',
            'wsgi.url_scheme': 'https',
            'CONTENT_LENGTH': str(len(body)) if body else '0',
            'CONTENT_TYPE': headers.get('content-type', ''),
            'HTTP_HOST': headers.get('host', 'appwrite'),
        }
        
        # Add all headers to environ
        for key, value in headers.items():
            key = 'HTTP_' + key.upper().replace('-', '_')
            environ[key] = value
        
        # Handle the request
        response = application(environ, lambda *args: None)
        
        return context.res.json({
            'success': True,
            'response': response
        })
        
    except Exception as e:
        context.log(f"Error: {str(e)}")
        return context.res.json({
            'success': False,
            'error': str(e)
        }, 500)
