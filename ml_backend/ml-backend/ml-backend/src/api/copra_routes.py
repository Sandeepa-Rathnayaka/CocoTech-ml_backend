from flask import Blueprint, request, jsonify
from src.services.copra_service import CopraService
from src.utils.response_formatter import ResponseFormatter

copra_bp = Blueprint('copra', __name__)
copra_service = CopraService()

@copra_bp.route('/predict-drying-time', methods=['POST'])
def predict_drying_time():
    try:
        data = request.get_json()
        prediction_result = copra_service.predict_drying_time(data)
        formatted_response = ResponseFormatter.format_drying_time_response(
            prediction_result
        )
        return jsonify(formatted_response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@copra_bp.route('/predict-oil-yield', methods=['POST'])
def predict_oil_yield():
    try:
        data = request.get_json()
        prediction_result = copra_service.predict_oil_yield(data)
        formatted_response = ResponseFormatter.format_oil_yield_response(
            prediction_result
        )
        return jsonify(formatted_response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500