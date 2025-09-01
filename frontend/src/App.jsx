import React from 'react'
import ChatInterface from './components/ChatInterface'

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-100 to-gray-200 flex items-center justify-center">
      <div className="w-full max-w-3xl p-6">
        <h1 className="text-4xl font-extrabold text-center mb-6 text-gray-800 tracking-tight">
          🤖 LLM Chatbot
        </h1>
        <ChatInterface />
      </div>
    </div>
  )
}

export default App
