# Pandas AI Agent
This project provides a user-friendly interface for querying and interacting with tabular data (CSV or Excel files) using AI. It leverages large language models and the Pandas library to interpret data queries and provide meaningful insights in a conversational manner.

# Features
Chat with Data: Upload a CSV or Excel file and interact with it like chatting with an assistant.
Intelligent Querying: Uses advanced AI models to interpret and execute queries on the data.
Encoding Detection: Automatically detects file encodings to handle various CSV formats.
Support for Dangerous Code: Allows complex operations on data using Python code.
Gradio Interface: Offers a clean and simple web-based UI for interaction.
Getting Started
## 1. Prerequisites
Ensure you have the following installed:

Python 3.8+
Pip (Python Package Installer)
## 2. Clone the Repository
git clone https://github.com/Rag-PandasAIAgent/Pandas_AI_Agent.git

cd Pandas_AI_Agent
## 3. Install Dependencies
Install required Python libraries:

pip install -r requirements.txt
## 4. Set Up Environment Variables
Create a .env file in the root directory and add:
GROQ_API_KEY=your_api_key_here
+ Note: Replace your_api_key_here with your actual API key.
+ Refer to the sample.env file for more details.

# Usage
## 1. Start the Application
Launch the Gradio interface:
python pandas_ai_agents.py
## 2. Interact with Your Data
Upload a CSV or Excel file.
Type your queries in the input box (e.g., "What is the average value in column A?").
View responses in the chat history.

# Project Structure
Pandas_AI_Agent/

* pandas_ai_agents.py  # Main script for the application
* requirements.txt     # Python dependencies
* .env                 # Environment variables (not included in the repository)
* sample.env           # Template for environment variables
* .gitignore           # Files to ignore in version control
* LICENSE              # License file
* README.md            # Project documentation

# Requirements
The project relies on the following Python libraries:

python-dotenv
groq
langchain-groq
langchain-experimental
pandas
charset-normalizer
gradio

You can install them using:
pip install -r requirements.txt

# Technologies Used
Pandas: Data manipulation library.

LangChain: Framework for integrating LLMs with tools.

Gradio: Framework for building web interfaces.

Charset-Normalizer: Detects encoding for CSV files.

Python-dotenv: Manages environment variables.

# Contributing
Contributions are welcome! Here's how you can help:

Fork this repository.

Create a new branch.

Commit your changes.

Submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments
Special thanks to the developers of LangChain, Pandas, and Gradio for their incredible tools.
Inspired by the need for smarter and simpler ways to interact with data.

# Contact
For questions or feedback, feel free to contact [swarimabdussamad@gmail.com].
