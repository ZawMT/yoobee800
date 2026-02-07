
# Testing LLM (Python + Docker)

Simple CLI app to try out Google Gemini LLM

## Quickstart

```bash
# 1) Build the image
docker build -t test_llm .

# 2) Run the app (interactive)
docker run -it --rm --name test_llm_app test_llm CV_FILENAME --key GOOGLE_AI_STUDIO_API_KEY 
  
CV_FILENAME: The name of the CV / Resume file (e.g. MyCV.txt)   
GOOGLE_AI_STUDIO_API_KEY: The API key which can be viewed at https://aistudio.google.com/api-keys (Account must be created)