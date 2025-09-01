import re

class TextProcessor:
    def preprocess(self, text):
        """Clean and preprocess input text"""
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Limit length
        if len(text) > 500:
            text = text[:500]
        
        return text
    
    def postprocess(self, text):
        """Clean up generated text"""
        # Remove repetitive patterns
        text = re.sub(r'(.)\1{3,}', r'\1\1', text)
        
        # Ensure proper ending
        if text and not text[-1] in '.!?':
            text += '.'
        
        return text