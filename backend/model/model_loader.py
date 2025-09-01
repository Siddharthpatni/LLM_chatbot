from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import logging

logger = logging.getLogger(__name__)

class ModelLoader:
    def __init__(self, model_name="microsoft/DialoGPT-small"):
        """Initialize with DialoGPT for conversational AI"""
        self.device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        logger.info(f"Using device: {self.device}")
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
            self.model.to(self.device)
            
            # Add padding token if not present
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
                
            logger.info(f"Model {model_name} loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise
    
    def generate_response(self, input_text, max_length=100):
        """Generate response using the model"""
        try:
            # Encode input
            inputs = self.tokenizer.encode(
                input_text, 
                return_tensors="pt",
                truncation=True,
                max_length=512
            ).to(self.device)
            
            # Generate response
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_length=max_length,
                    num_return_sequences=1,
                    temperature=0.8,
                    pad_token_id=self.tokenizer.pad_token_id,
                    do_sample=True,
                    top_p=0.9
                )
            
            # Decode response
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Remove input from response if present
            if response.startswith(input_text):
                response = response[len(input_text):].strip()
            
            return response if response else "I understand. Please tell me more."
            
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return "I apologize, but I encountered an error. Please try again."