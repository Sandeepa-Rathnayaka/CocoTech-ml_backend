import joblib
from pathlib import Path
import warnings
from sklearn.exceptions import InconsistentVersionWarning

# Suppress warnings
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

class ModelRegistry:
    def __init__(self):
        self.base_path = Path("src/models/trained_models")
        self.models = {}
        self.scalers = {}
        self.mappings = {}

    def load_irrigation_model(self):
        """Load irrigation model and its dependencies"""
        try:
            irrigation_path = self.base_path / "irrigation"
            
            # Load models with error handling
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                self.models['irrigation'] = joblib.load(irrigation_path / "best_model.pkl")
                self.scalers['irrigation'] = joblib.load(irrigation_path / "scaler.pkl")
                self.mappings['irrigation'] = joblib.load(irrigation_path / "soil_type_mapping.pkl")
                
        except Exception as e:
            print(f"Error loading models: {str(e)}")
            raise

    def get_irrigation_components(self):
        """Get irrigation model components"""
        if not self.models.get('irrigation'):
            self.load_irrigation_model()
            
        return {
            'model': self.models.get('irrigation'),
            'scaler': self.scalers.get('irrigation'),
            'mapping': self.mappings.get('irrigation')
        }
        
        
    def load_copra_models(self):
        """Load copra models"""
        try:
            copra_path = self.base_path / "copra"
            
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                self.models['drying_time'] = joblib.load(copra_path / "best_drying_time_model.pkl")
                self.models['oil_yield'] = joblib.load(copra_path / "best_oil_yield_predictor.pkl")
                
        except Exception as e:
            print(f"Error loading copra models: {str(e)}")
            raise
        
    def get_copra_components(self):
        """Get copra model components"""
        if not self.models.get('drying_time'):
            self.load_copra_models()
            
        return {
            'drying_time_model': self.models.get('drying_time'),
            'oil_yield_model': self.models.get('oil_yield')
        }


model_registry = ModelRegistry()