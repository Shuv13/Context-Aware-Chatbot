# Nora – Multilingual AI Chatbot

Nora is a multilingual, context-aware chatbot built with the Groq API, LangChain, and Streamlit. It supports coherent multi-turn conversations in English, Hindi, and Bengali, with real-time context memory and a user-friendly web interface.

## ✨ Features

- **🌍 Multilingual Support**: Seamlessly chat in English, Hindi, and Bengali.
- **💬 Context Awareness**: Retains conversation history using LangChain's buffer memory.
- **⚡ Powered by Groq**: Leverages Groq's LLMs for fast and efficient inference.
- **🖥️ Web Interface**: Built with Streamlit for intuitive and easy interaction.
- **🔑 Secure Key Handling**: Input your Groq API key securely via the sidebar.
- **🔄 Model Switching**: Choose from available Groq models at runtime.

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/nora-chatbot.git
   cd nora-chatbot
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is not available, install manually:
   ```bash
   pip install groq streamlit langchain langchain-core langchain-groq transformers sentencepiece torch
   ```

## ▶️ Running the App

Run the following command to start the app:
```bash
streamlit run app.py
```

Once the app starts, open the browser link provided by Streamlit (usually `http://localhost:8501`).

## 🛠️ Usage

1. Enter your Groq API key in the Streamlit sidebar.
2. Select a supported Groq model (avoid deprecated models).
3. Start chatting in English, Hindi, or Bengali.
4. The chatbot retains recent context for more coherent and relevant replies.

## ✅ Supported Models

Check Groq’s documentation for the latest active models. Example models include:

- `gemma-7b-it`
- `gemma2-9b-it`
- `llama3-70b-8192`
- `llama3-8b-8192`
- `mixtral-8x7b-32768`

**Note**: Avoid deprecated models like `llama-3.1-70b-versatile`.

## 🧪 Testing

Ensure the following features work as expected:

- Context memory persists across multiple conversation turns.
- Language switching (English, Hindi, Bengali) functions correctly.
- Streamlit interface renders and updates properly.
- Groq API returns expected responses for valid inputs.
- Error handling works for missing/invalid API keys and deprecated models.

## 📄 License

This project is licensed under the MIT License.