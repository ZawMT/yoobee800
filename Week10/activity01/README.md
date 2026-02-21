
# Testing LLM (Python + Docker)

Simple CLI app to try out Google Gemini LLM

## Quickstart

```bash
# 1) Build the image
docker build -t test_llm .

# 2) Put the CV file inside the folder "cv_files"

# 3) Create an environment file called ".env" and set the values for the following variables:
# GEMINI_API_KEY=API_KEY_FROM_https://aistudio.google.com/api-keys
# CV_FOLDER=cv_files

# 4) Run the app (interactive)
docker run -it --rm --name test_llm_app --env-file .env -v /cv_files:/app/cv_files test_llm CV_FILENAME  
  
CV_FILENAME: The name of the CV / Resume file (e.g. MyCV.txt) from the folder "cv_files"   