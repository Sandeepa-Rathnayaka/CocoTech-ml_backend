class ResponseFormatter:
    @staticmethod
    def get_water_level_range(category: int) -> str:
        ranges = {
            0: "0L (None)",
            1: "50-100L (High)",
            2: "30-50L (Moderate)",
            3: "10-30L (Low)"
        }
        return ranges.get(category, "Unknown")

    @staticmethod
    def format_prediction_response(prediction_result: dict) -> dict:
        probabilities = prediction_result['probabilities']
        return {
            'prediction': prediction_result['prediction'],
            'waterNeedRange': ResponseFormatter.get_water_level_range(
                prediction_result['prediction']
            ),
            'probabilities': {
                'noWater': float(probabilities[0]),
                'highWater': float(probabilities[1]),
                'moderateWater': float(probabilities[2]),
                'lowWater': float(probabilities[3])
            },
            'inputFeatures': prediction_result['input_features']
        }
        
    @staticmethod
    def format_drying_time_response(prediction_result: dict) -> dict:
        return {
            'dryingTime': round(prediction_result['drying_time'], 2),
            'unit': 'hours',
            'inputFeatures': prediction_result['input_features']
        }

    @staticmethod
    def format_oil_yield_response(prediction_result: dict) -> dict:
        return {
            'oilYield': round(prediction_result['oil_yield'], 2),
            'unit': 'kg',
            'inputFeatures': prediction_result['input_features']
        }