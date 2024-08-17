import os

# Configuration for the application

# OpenAI API key (you should set this as an environment variable for security)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-qxVa5ALfuVLWuAgd1iY3nj665ZNj8ydDx066oVww-NT3BlbkFJu79P6vj3dForylyPqtYz8fyeYH7kdD1H325MB_e34A")

# Function to validate if API key is present
def check_config():
    if not OPENAI_API_KEY or OPENAI_API_KEY == "your-default-api-key":
        raise ValueError("Please set the OPENAI_API_KEY in your environment or config.py file")

# Call this function at the start of your application to ensure everything is configured
check_config()
