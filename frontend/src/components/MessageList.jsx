import React, { useEffect, useRef } from 'react'

function MessageList({ messages, loading }) {
  const bottomRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, loading])

  return (
    <div className="h-[70vh] overflow-y-auto p-4 bg-gray-50 rounded-t-lg">
      {messages.map((msg, i) => (
        <div
          key={i}
          className={`flex mb-3 ${
            msg.sender === 'user' ? 'justify-end' : 'justify-start'
          }`}
        >
          <div
            className={`max-w-xs px-4 py-2 rounded-2xl shadow-sm ${
              msg.sender === 'user'
                ? 'bg-blue-500 text-white rounded-br-none'
                : 'bg-gray-200 text-gray-900 rounded-bl-none'
            }`}
          >
            {msg.text}
          </div>
        </div>
      ))}

      {loading && (
        <div className="flex justify-start mb-3">
          <div className="bg-gray-200 text-gray-700 px-4 py-2 rounded-2xl rounded-bl-none">
            <span className="animate-pulse">...</span>
          </div>
        </div>
      )}

      <div ref={bottomRef} />
    </div>
  )
}

export default MessageList
