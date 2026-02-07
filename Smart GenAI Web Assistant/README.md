# Smart GenAI Web Assistant

A modular Flask-based web application that leverages **IBM watsonx.ai** and **LangChain** to generate structured, actionable AI responses.

## 🚀 Features
- **Structured Output**: Uses LangChain's `JsonOutputParser` to ensure AI responses are always in a valid JSON format.
- **Enterprise AI**: Integrated with IBM's **Granite-3-8b-instruct** model.
- **Modern UI**: A clean, responsive chat interface with real-time loading indicators.
- **Modular Architecture**: Separated concerns for Prompt Engineering, Model Inference, and Response Parsing.

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **AI Orchestration**: LangChain, Pydantic
- **Model**: watsonx.ai (IBM Granite)
- **Frontend**: HTML5, CSS3 (Flexbox), JavaScript (Async/Fetch)

## 📋 Prerequisites
- Python 3.10+
- IBM Cloud Account (watsonx.ai project)
- API Key and Project ID

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/genai-flask-app.git](https://github.com/YOUR_USERNAME/genai-flask-app.git)
   cd genai-flask-app
