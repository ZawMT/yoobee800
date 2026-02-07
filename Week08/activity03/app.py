
import os
import argparse
from google import genai


class CVAnalyzer:  # The class to handle CV ingestion and AI-driven critique
    # Connstructor
    def __init__(self, api_key: str, model_name: str = "gemini-2.5-flash"):
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name
        self.system_instruction = (
            "Hello, I am a professional Career Coach. Submit your CV for "
            "clarity, impact, and keyword optimization. I will provide actionable "
            "bullet points for improvement."
        )

    # Reads the content of the text file
    def load_file(self, file_path: str) -> str:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return f"Error: The file at {file_path} was not found."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    # Sends CV text to Gemini and returns suggestions
    def get_suggestions(self, cv_text: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_name,
            config={'system_instruction': self.system_instruction},
            contents=f"Here is my CV text:\n\n{cv_text}"
        )
        return response.text


class CLIHandler:  # The class to handle Command Line Arguments and user interaction
    @staticmethod
    def run():
        parser = argparse.ArgumentParser(
            description="Gemini-powered CV Critique Tool")
        parser.add_argument("file", help="Path to your CV text file")
        parser.add_argument("--key", help="Your Gemini API Key", required=True)

        args = parser.parse_args()

        # Initialize the analyzer
        analyzer = CVAnalyzer(api_key=args.key)

        print(f"--- Loading {args.file} ---")
        content = analyzer.load_file(args.file)

        if content.startswith("Error"):
            print(content)
        else:
            print("--- Analyzing with Gemini... ---")
            suggestions = analyzer.get_suggestions(content)
            print("\n" + "="*20 + " SUGGESTIONS " + "="*20)
            print(suggestions)


if __name__ == "__main__":
    CLIHandler.run()
