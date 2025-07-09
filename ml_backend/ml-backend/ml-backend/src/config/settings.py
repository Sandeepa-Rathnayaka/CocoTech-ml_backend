import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Base paths
    BASE_DIR = Path(__file__).parent.parent.parent
    MODEL_PATH = os.getenv('MODEL_PATH', 'src/models/trained_models')
    
    # Server settings
    PORT = int(os.getenv('PORT', 5000))
    DEBUG = os.getenv('FLASK_ENV') == 'development'
    
    # Model settings
    IRRIGATION_MODEL_PATH = os.path.join(MODEL_PATH, 'irrigation')
    COPRA_MODEL_PATH = os.path.join(MODEL_PATH, 'copra')
    
    # API settings
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')

settings = Settings()