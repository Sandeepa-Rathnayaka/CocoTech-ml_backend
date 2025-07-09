import pandas as pd
from src.models.model_registry import model_registry

class CopraService:
    def predict_drying_time(self, data: dict) -> dict:
        
        # Retrieve the pre-trained drying time model from the model registry
        components = model_registry.get_copra_components()
        model = components['drying_time_model']

        input_data = pd.DataFrame({
            'Initial Moisture Level (%)': [data['moistureLevel']],
            'Temperature (°C)': [data['temperature']],
            'Humidity (%)': [data['humidity']]
        })

        prediction = model.predict(input_data)[0]

        return {
            'drying_time': float(prediction),
            'input_features': data
        }

    def predict_oil_yield(self, data: dict) -> dict:
        components = model_registry.get_copra_components()
        model = components['oil_yield_model']

         # Convert input data to pandas DataFrame format expected by the model
        input_data = pd.DataFrame({
            'Initial Moisture Level (%)': [data['moistureLevel']],
            'Temperature (°C)': [data['temperature']],
            'Humidity (%)': [data['humidity']],
            'Drying Time (hrs)': [data['dryingTime']]
        })

        prediction = model.predict(input_data)[0]

        return {
            'oil_yield': float(prediction),
            'input_features': data
        }