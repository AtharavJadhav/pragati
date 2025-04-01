# News Article Chatbot

A minimalist chatbot application specialized in news articles, built with FastAPI backend and React frontend. The chatbot uses OpenAI's API to provide informative responses about news topics.

## Features

- Clean, minimalist user interface
- Light and dark mode support
- News article specialization
- Real-time chat interface
- Responsive design for mobile and desktop

## Prerequisites

- Node.js (v14+)
- Python (v3.8+)
- OpenAI API key

## Setup Instructions

### Backend Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/news-article-chatbot.git
cd news-article-chatbot/backend
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory:
```
OPENAI_API_KEY=your_openai_api_key_here
```

5. Replace `your_openai_api_key_here` with your actual OpenAI API key
   - You can get an API key from [OpenAI's platform](https://platform.openai.com/account/api-keys)
   - Keep your API key secure and never commit it to version control

6. Start the backend server:
```bash
uvicorn main:app --reload
```

The backend will be running at http://localhost:8000.

### Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
```bash
cd news-article-chatbot/frontend
```

2. Install the required dependencies:
```bash
npm install
```

3. Start the frontend development server:
```bash
npm start
```

The frontend will be running at http://localhost:3000.

## Usage

1. Once both the backend and frontend are running, open your browser and navigate to http://localhost:3000
2. You'll see the chat interface with a welcome message
3. Type your news-related questions in the input field and press "Send"
4. Toggle between light and dark mode using the sun/moon icon in the top-right corner

## Troubleshooting

- If you encounter errors with the OpenAI API:
  - Make sure your API key is correctly set in the `.env` file
  - Verify that your OpenAI account has available credits
  - Check that you're using a supported model (the default is gpt-3.5-turbo)

- If the frontend can't connect to the backend:
  - Ensure the backend server is running at http://localhost:8000
  - Check for CORS issues in the browser console (the backend is configured to allow requests from all origins in development)

## License

[MIT License](LICENSE)
