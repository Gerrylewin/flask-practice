from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Add this new route
    @app.route('/')
    def home():
        return "Hello, World!"
    
    return app