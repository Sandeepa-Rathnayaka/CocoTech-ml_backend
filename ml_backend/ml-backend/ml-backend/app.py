# from flask import Flask
# from flask_cors import CORS
# from src.api import init_app
# from dotenv import load_dotenv
# import os
# import warnings
# from sklearn.exceptions import InconsistentVersionWarning

# # Suppress specific warnings
# warnings.filterwarnings("ignore", category=InconsistentVersionWarning)
# warnings.filterwarnings("ignore", category=UserWarning)

# load_dotenv()

# def create_app():
#     app = Flask(__name__)
#     CORS(app)

#     # Initialize API routes
#     init_app(app)

#     return app

# app = create_app()

# if __name__ == '__main__':
#     port = int(os.getenv('PORT', 5000))
#     # Set host to localhost only for development
#     app.run(host='127.0.0.1', port=port, debug=True)

from flask import Flask
from flask_cors import CORS
from src.api import init_app
from dotenv import load_dotenv
import os
import warnings
from sklearn.exceptions import InconsistentVersionWarning

# Suppress specific warnings
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)
warnings.filterwarnings("ignore", category=UserWarning)

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Initialize API routes
    init_app(app)
    
    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    # Change host to '0.0.0.0' to make the app publicly accessible
    app.run(host='0.0.0.0', port=port, debug=False)