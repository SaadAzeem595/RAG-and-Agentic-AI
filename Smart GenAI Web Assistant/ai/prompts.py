from langchain_core.prompts import PromptTemplate

def get_prompt_template(parser):
    template = (
        "You are a helpful AI assistant. Your goal is to provide structured but natural responses.\n"
        "If the user says 'Hello' or 'Hi', greet them warmly in the summary and leave action items empty.\n"
        "If the user asks a technical or task-based question, provide a detailed title and action items.\n"
        "{format_instructions}\n"
        "User Request: {query}"
    )
    prompt = PromptTemplate(
        template=template,
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    return prompt