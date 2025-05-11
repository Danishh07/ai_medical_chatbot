
# CalmSphere 🧘‍♀️

Your AI-powered mental health companion
## 🌟 About the Project
CalmSphere is an AI-powered chatbot designed to provide a safe and supportive space for mental well-being.
Whether you're feeling overwhelmed, anxious, or simply need a moment of clarity, CalmSphere is here to listen, guide, and offer helpful insights.

## 📂 Project Structure
```bash
ai-medical-chatbot/
├── backend/
│   ├── main.py              # FastAPI backend
│   ├── chat_engine.py   # AI logic
│   └── data/                  # Ignored data files (chat logs, etc.)
├── frontend/
│   ├── index.html       # Main HTML page
│   ├── style.css           # Styling
│   └── chatbot.js        # Chatbot frontend logic
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 How to Run Locally
1.) Clone the repository ~

    git clone https://github.com/your-username/ai-medical-chatbot.git

2.) Set up the backend ~

• Install dependencies :

    pip install -r requirements.txt

• Start the FastAPI server :

    uvicorn backend.main:app --reload

3.) Open the frontend ~

• Simply open **frontend/index.html** in your browser.

• Make sure the backend is running on http://127.0.0.1:8000/chat.

## 🛠 Tech Stack
• **Frontend** : HTML, CSS, JavaScript

• **Backend** : Python, FastAPI

• **AI Model** : LLM-based completion API

##  ✨ Features

• Friendly, AI-driven conversations

• Focused entirely on mental and physical well-being

• Clean, mobile-responsive chat interface

• Smart session handling for users


## 📋 Improvements
• Add user authentication

• Store anonymous chat history securely

• Connect to a more powerful LLM (like Hugging Face models)
## 🤝 Contributing
Contributions, ideas, and suggestions are welcome!

Feel free to open an issue or submit a pull request.
