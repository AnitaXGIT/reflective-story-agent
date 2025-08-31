"""
Simple Flask server for handling file downloads
Runs alongside Gradio to serve exported articles
"""

import os
import threading
from flask import Flask, send_file, abort
from werkzeug.utils import secure_filename

class FileServer:
    def __init__(self, download_folder="downloads", port=5001):
        self.download_folder = download_folder
        self.port = port
        self.app = Flask(__name__)
        self.setup_routes()
        
        # Create downloads folder if it doesn't exist
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
    
    def setup_routes(self):
        """Set up Flask routes for file downloads"""
        
        @self.app.route('/download/<filename>')
        def download_file(filename):
            """Serve file for download with proper headers"""
            try:
                # Secure the filename to prevent directory traversal
                safe_filename = secure_filename(filename)
                file_path = os.path.join(self.download_folder, safe_filename)
                
                # Check if file exists
                if not os.path.exists(file_path):
                    abort(404)
                
                # Determine the correct mimetype and attachment name
                if filename.endswith('.pdf'):
                    mimetype = 'application/pdf'
                elif filename.endswith('.txt'):
                    mimetype = 'text/plain'
                else:
                    mimetype = 'application/octet-stream'
                
                # Send file with download headers
                return send_file(
                    file_path,
                    as_attachment=True,
                    download_name=filename,
                    mimetype=mimetype
                )
                
            except Exception as e:
                print(f"Error serving file {filename}: {str(e)}")
                abort(500)
        
        @self.app.route('/health')
        def health_check():
            """Simple health check endpoint"""
            return {"status": "running", "download_folder": self.download_folder}
    
    def start_server(self):
        """Start the Flask server in a separate thread"""
        def run_server():
            self.app.run(host='127.0.0.1', port=self.port, debug=False, use_reloader=False)
        
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        print(f"File server started on http://127.0.0.1:{self.port}")
        return server_thread

# Global file server instance
file_server = FileServer()