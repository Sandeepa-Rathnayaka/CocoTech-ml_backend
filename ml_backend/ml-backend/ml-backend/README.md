# AgriML API

![AgriML Banner](https://via.placeholder.com/800x200?text=AgriML+API)

A machine learning backend API for agricultural predictions focusing on irrigation optimization and copra processing.

## 📋 Overview

AgriML API is a Flask-based machine learning service that provides intelligent predictions for two key agricultural processes:

1. **Irrigation Management** - Optimize water usage based on environmental conditions and soil characteristics
2. **Copra Processing** - Predict drying times and oil yields for coconut processing

This API serves as a backend for agricultural management systems, IoT devices, and mobile applications to enable data-driven decision making in farming and processing operations.

## ✨ Features

### Irrigation Prediction
- **Smart Water Recommendations** - Predicts optimal irrigation levels (None, Low, Moderate, High)
- **Probability Analysis** - Provides confidence scores for each recommendation category
- **Multi-factor Analysis** - Considers soil type, moisture at different depths, weather conditions, and plant characteristics

### Copra Processing
- **Drying Time Prediction** - Estimates required drying time based on moisture, temperature, and humidity
- **Oil Yield Prediction** - Forecasts expected oil yield from coconut processing
- **Process Optimization** - Helps operators optimize processing parameters

### System Features
- **Health Monitoring** - Endpoint to verify system and model health
- **Error Handling** - Robust error handling with meaningful messages
- **Structured Responses** - Consistent, well-formatted JSON responses

## 🏗️ Architecture

### System Architecture
```
                                    ┌─────────────────┐
                                    │                 │
                 ┌─────────────────►│  Irrigation     │
                 │                  │  Service        │
┌───────────┐    │                  │                 │
│           │    │                  └─────────────────┘
│           │    │                            │
│  API      │    │                            ▼
│  Routes   │────┤                  ┌─────────────────┐
│           │    │                  │  Model          │
│           │    │                  │  Registry       │
└───────────┘    │                  │                 │
                 │                  └─────────────────┘
                 │                            ▲
                 │                            │
                 │                  ┌─────────────────┐
                 │                  │                 │
                 └─────────────────►│  Copra          │
                                    │  Service        │
                                    │                 │
                                    └─────────────────┘
```

### Code Organization

```
src/
├── api/
│   ├── __init__.py
│   ├── irrigation_routes.py
│   ├── copra_routes.py
│   └── health_routes.py
├── models/
│   ├── __init__.py
│   ├── model_registry.py
│   └── trained_models/
│       ├── irrigation/
│       │   ├── best_model.pkl
│       │   ├── scaler.pkl
│       │   └── soil_type_mapping.pkl
│       └── copra/
│           ├── best_drying_time_model.pkl
│           └── best_oil_yield_predictor.pkl
├── services/
│   ├── __init__.py
│   ├── irrigation_service.py
│   └── copra_service.py
├── utils/
│   ├── __init__.py
│   ├── error_handler.py
│   └── response_formatter.py
├── settings.py
└── app.py
```

### Design Patterns

- **Blueprint Pattern** - API routes are organized into Flask Blueprints for modularity
- **Singleton Pattern** - Model Registry ensures models are loaded only once
- **Service Layer Pattern** - Business logic is encapsulated in service classes
- **Repository Pattern** - Centralized model access through the registry
- **Factory Pattern** - Standardized response formatting

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Scikit-learn
- Pandas
- Flask

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/agriml-api.git
cd agriml-api
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set environment variables (optional)
```bash
export FLASK_ENV=development
export PORT=5000
export MODEL_PATH=src/models/trained_models
```

5. Run the application
```bash
python src/app.py
```

## 🔄 API Endpoints

### Irrigation API

#### Predict Water Needs
```
POST /api/irrigation/predict
```

**Request Body:**
```json
{
  "soilType": "clay",
  "soilMoisture10cm": 15.2,
  "soilMoisture20cm": 18.5,
  "soilMoisture30cm": 20.1,
  "plantAge": 3.5,
  "temperature": 32.5,
  "humidity": 65,
  "rainfall": 2.3
}
```

**Response:**
```json
{
  "prediction": 2,
  "waterNeedRange": "30-50L (Moderate)",
  "probabilities": {
    "noWater": 0.05,
    "highWater": 0.15,
    "moderateWater": 0.7,
    "lowWater": 0.1
  },
  "inputFeatures": {
    "soilType": "clay",
    "soilMoisture10cm": 15.2,
    "soilMoisture20cm": 18.5,
    "soilMoisture30cm": 20.1,
    "plantAge": 3.5,
    "temperature": 32.5,
    "humidity": 65,
    "rainfall": 2.3
  }
}
```

### Copra API

#### Predict Drying Time
```
POST /api/copra/predict-drying-time
```

**Request Body:**
```json
{
  "moistureLevel": 45.2,
  "temperature": 35.0,
  "humidity": 60.5
}
```

**Response:**
```json
{
  "dryingTime": 24.5,
  "unit": "hours",
  "inputFeatures": {
    "moistureLevel": 45.2,
    "temperature": 35.0,
    "humidity": 60.5
  }
}
```

#### Predict Oil Yield
```
POST /api/copra/predict-oil-yield
```

**Request Body:**
```json
{
  "moistureLevel": 12.5,
  "temperature": 30.0,
  "humidity": 55.0,
  "dryingTime": 24.0
}
```

**Response:**
```json
{
  "oilYield": 3.25,
  "unit": "kg",
  "inputFeatures": {
    "moistureLevel": 12.5,
    "temperature": 30.0,
    "humidity": 55.0,
    "dryingTime": 24.0
  }
}
```

### Health API

#### Check System Health
```
GET /api/health/health
```

**Response:**
```json
{
  "status": "healthy",
  "models_loaded": true,
  "copra": true
}
```

## 🧠 Machine Learning Models

### Irrigation Model
- **Type**: Classification model (likely Random Forest or Gradient Boosting)
- **Features**:
  - Soil Type (categorical)
  - Soil Moisture at 10, 20, and 30 cm depths
  - Plant Age
  - Temperature
  - Humidity
  - Rainfall
- **Outputs**: Water need category (0-3)
  - 0: No water needed
  - 1: High water needed (50-100L)
  - 2: Moderate water needed (30-50L)
  - 3: Low water needed (10-30L)

### Copra Models
- **Drying Time Model**:
  - **Type**: Regression model
  - **Features**: Initial moisture level, temperature, humidity
  - **Output**: Estimated drying time in hours
  
- **Oil Yield Model**:
  - **Type**: Regression model
  - **Features**: Moisture level, temperature, humidity, drying time
  - **Output**: Estimated oil yield in kg

## 🔍 Error Handling

The API includes a robust error handling system with standardized error responses:

```json
{
  "error": "Invalid input: Soil moisture values must be between 0 and 100",
  "status_code": 400
}
```

## 🧪 Testing

To run the tests:

```bash
pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Scikit-learn team for machine learning tools
- Flask team for the web framework
- Agricultural research partners for domain expertise

## 📞 Contact

For support or inquiries, please contact [sadeepalakshan0804@gmail.com,sandeeparathnayaka20@gmail.com](mailto:your-email@example.com)