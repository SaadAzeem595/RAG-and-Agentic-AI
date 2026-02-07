from flask import Flask, render_template, request, jsonify
from ai.model import get_model
from ai.parser import get_json_parser
from ai.prompts import get_prompt_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_ai():
    user_query = request.json.get("query")
    
    model = get_model()
    parser = get_json_parser()
    prompt_template = get_prompt_template(parser)
    
    # 1. Prepare the prompt
    formatted_prompt = prompt_template.format(query=user_query)
    
    # 2. Get response from WatsonX
    # Note: Use generate_text() for the ibm-watsonx-ai library
    raw_response = model.generate_text(prompt=formatted_prompt)
    
    try:
        # 3. Attempt to parse the structured JSON
        structured_data = parser.parse(raw_response)
        return jsonify(structured_data)
    except Exception as e:
        # Fallback: if parsing fails, send the raw text so the UI still shows SOMETHING
        return jsonify({
            "title": "AI Response",
            "summary": raw_response,
            "action_items": ["Error parsing structured output"]
        })
if __name__ == '__main__':
    app.run(debug=True, port=5000)