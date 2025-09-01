import axios from 'axios'

const API_URL = '/api'

export const sendMessage = async (message) => {
  try {
    const response = await axios.post(`${API_URL}/chat`, {
      message: message
    })
    return response.data.response
  } catch (error) {
    console.error('API Error:', error)
    throw error
  }
}