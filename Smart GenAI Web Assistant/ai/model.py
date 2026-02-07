import os
from ibm_watsonx_ai.foundation_models import ModelInference

def get_model(model_id="ibm/granite-3-8b-instruct"):
    """
    Initializes the model using a supported model_id and environment variables.
    """
    
    credentials = {
        "url": "https://us-south.ml.cloud.ibm.com",
        "apikey": os.getenv("WATSONX_API_KEY"),
        "token": os.getenv("WATSONX_TOKEN")
    }
    
    project_id = os.getenv("WATSONX_PROJECT_ID")

    params = {
        "max_new_tokens": 512,
        "temperature": 0.7
    }

    # Using ModelInference as recommended by the deprecation warning
    model = ModelInference(
        model_id=model_id,
        params=params,
        credentials=credentials,
        project_id=project_id
    )
    return model