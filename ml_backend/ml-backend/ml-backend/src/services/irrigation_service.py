import pandas as pd
from src.models.model_registry import model_registry

class IrrigationService:
    @staticmethod
    def predict(data: dict) -> dict:
        components = model_registry.get_irrigation_components()
        model = components['model']
        scaler = components['scaler']
        soil_mapping = components['mapping']

        # Prepare input data
        input_data = pd.DataFrame({
            'Soil Type': [soil_mapping[data['soilType']]],
            'Soil Moisture (10 cm) (%)': [data['soilMoisture10cm']],
            'Soil Moisture (20 cm) (%)': [data['soilMoisture20cm']],
            'Soil Moisture (30 cm) (%)': [data['soilMoisture30cm']],
            'Plant Age (years)': [data['plantAge']],
            'Temperature (°C)': [data['temperature']],
            'Humidity (%)': [data['humidity']],
            'Rainfall (mm)': [data['rainfall']]
        })

        # Scale and predict
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        probabilities = model.predict_proba(input_scaled)[0]

        return {
            'prediction': int(prediction),
            'probabilities': probabilities.tolist(),
            'input_features': data
        }