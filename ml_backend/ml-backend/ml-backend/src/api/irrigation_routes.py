from flask import Blueprint, request, jsonify
from src.services.irrigation_service import IrrigationService
from src.utils.response_formatter import ResponseFormatter

irrigation_bp = Blueprint('irrigation', __name__)
irrigation_service = IrrigationService()

@irrigation_bp.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        prediction_result = irrigation_service.predict(data)
        formatted_response = ResponseFormatter.format_prediction_response(
            prediction_result
        )
        return jsonify(formatted_response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500