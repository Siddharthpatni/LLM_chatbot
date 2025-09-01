# LLM Chatbot

A modern chatbot application built with Flask, React, and HuggingFace Transformers.

## Features

- 🤖 AI-powered conversational interface using DialoGPT
- ⚡ Real-time chat interface with React
- 🎨 Modern UI with Tailwind CSS
- 🐳 Docker support for easy deployment
- 🔧 RESTful API with Flask

## Tech Stack

- **Backend**: Flask, HuggingFace Transformers, PyTorch
- **Frontend**: React, Vite, Tailwind CSS
- **AI Model**: Microsoft DialoGPT
- **Deployment**: Docker, Docker Compose

## Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker (optional)

### Installation

1. Clone the repository:
\`\`\`bash
git clone https://github.com/yourusername/LLM-Chatbot.git
cd LLM-Chatbot
\`\`\`

2. Set up the backend:
\`\`\`bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
\`\`\`

3. Set up the frontend:
\`\`\`bash
cd frontend
npm install
npm run dev
\`\`\`

4. Open http://localhost:3000 in your browser

### Using Docker

\`\`\`bash
docker-compose up --build
\`\`\`

## API Endpoints

- `POST /chat` - Send a message to the chatbot
  - Request: `{"message": "Hello"}`
  - Response: `{"response": "Hi there!", "status": "success"}`

- `GET /health` - Health check endpoint

## Project Structure

\`\`\`
LLM-Chatbot/
├── backend/           # Flask API
├── frontend/          # React UI
├── docker-compose.yml # Docker configuration
└── README.md         # Documentation
\`\`\`

## Performance on M1 Mac

This project is optimized for Apple Silicon (M1/M2) Macs:
- Uses MPS (Metal Performance Shaders) for GPU acceleration
- Efficient model loading with HuggingFace
- Optimized Docker builds for ARM64

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Acknowledgments

- HuggingFace for the Transformers library
- Microsoft for DialoGPT model
- React and Vite communities