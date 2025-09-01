from flask import Flask, request, jsonify
from flask_cors import CORS
from model.model_loader import ModelLoader
from utils.text_processor import TextProcessor
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize model
model_loader = ModelLoader()
text_processor = TextProcessor()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Process input
        processed_input = text_processor.preprocess(user_message)
        
        # Generate response
        response = model_loader.generate_response(processed_input)
        
        return jsonify({
            "response": response,
            "status": "success"
        }), 200
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)