"""
Sample application to try out LLM
"""

import os
import sys
import argparse
from google import genai  # pylint: disable=no-name-in-module


class CVAnalyzer:
    """The class to handle CV ingestion and AI-driven critique generation."""

    def __init__(self, api_key: str, model_name: str = "gemini-2.5-flash"):
        """Constructor"""
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name
        self.system_instruction = (
            "You are a professional Executive Career Coach. "
            "The user will provide their CV text. You must analyze it immediately. "
            "Do not ask for more information. Provide suggest 3 high-impact improvements."
        )

    def load_file(self, file_path: str) -> str:
        """Reads the content of the text file and returns it."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return f"Error: The file at {file_path} was not found."

    def get_suggestions(self, cv_text: str) -> str:
        """Sends CV text to Gemini and returns suggestions"""

        response = self.client.models.generate_content(
            model=self.model_name,
            config={'system_instruction': self.system_instruction},
            contents=f"Here is my CV text:\n\n{cv_text}"
        )
        return response.text

    @staticmethod
    def run():
        """Callinng Gemini LLM"""
        parser = argparse.ArgumentParser(
            description="Gemini-powered CV Critique Tool")
        parser.add_argument("file", help="Path to your CV text file")

        args = parser.parse_args()

        # Read API Key
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            print("Error: GEMINI_API_KEY not found in environment.")
            print("Please ensure your .env file is loaded or the -e flag is used.")
            sys.exit(1)

        # Initialize the analyzer
        analyzer = CVAnalyzer(api_key=api_key)

        # Read CV Folder
        cv_folder = os.getenv("CV_FOLDER", "")

        print(f"--- Loading {args.file} ---")
        file_path = os.path.join(cv_folder, args.file)
        content = analyzer.load_file(file_path)

        if content.startswith("Error"):
            print(content)
        else:
            print("--- Analyzing with Gemini... ---")
            suggestions = analyzer.get_suggestions(content)
            print("\n" + "="*20 + " SUGGESTIONS " + "="*20)
            print(suggestions)


if __name__ == "__main__":
    CVAnalyzer.run()
