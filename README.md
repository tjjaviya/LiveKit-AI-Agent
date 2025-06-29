# LiveKit AI Hospital Call Centre

A real-time AI-powered hospital assistant built with LiveKit Agents 1.0 and React. The AI agent provides medical consultation, appointment booking, and health information through voice conversations.

## 🏥 Features

- **Real-time Voice AI**: Powered by OpenAI's Realtime API
- **Medical Assistance**: Appointment booking, consultations, prescriptions
- **Responsive Frontend**: Modern hospital-themed React interface
- **Live Audio/Video**: Built on LiveKit infrastructure

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- LiveKit server running
- OpenAI API key

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv ai

# Activate virtual environment
# Windows:
ai\Scripts\activate
# macOS/Linux:
source ai/bin/activate

# Install dependencies
pip install -r requirements.txt


# Run the AI agent
python agent.py

# In another terminal, run the token server
python server.py
```

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### 3. Run Everything

1. **Start LiveKit server** (follow LiveKit docs)
2. **Run AI Agent**: `python backend/agent.py`
3. **Run Token Server**: `python backend/server.py`
4. **Run Frontend**: `npm run dev` (in frontend directory)
5. **Open**: http://localhost:5173

## 🎯 Usage

1. Open the web app
2. Click "Talk to Doctor" 
3. Allow microphone access
4. Start speaking with the AI hospital assistant
5. Ask about appointments, medical questions, or health records

## 📁 Project Structure

```
├── backend/
│   ├── agent.py          # LiveKit AI agent
│   ├── server.py         # JWT token server
│   ├── api.py           # Medical API functions
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx      # Main React app
│   │   └── components/  # UI components
│   └── package.json
└── README.md
```

## 🔧 Environment Variables

**Backend (.env):**
```env
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
OPENAI_API_KEY=your_openai_api_key
```

**Frontend (.env):**
```env
VITE_LIVEKIT_URL=ws://localhost:7880
```

## 🏗️ Built With

- **Backend**: LiveKit Agents 1.0, OpenAI Realtime API, Flask
- **Frontend**: React, Vite, LiveKit React SDK
- **AI**: OpenAI GPT-4 Realtime Preview
