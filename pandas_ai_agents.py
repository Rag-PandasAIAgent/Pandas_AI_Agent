from dotenv import load_dotenv
load_dotenv()

import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd
from charset_normalizer import from_path
import gradio as gr

# Load API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file.")

# Initialize the ChatGroq client
llm = ChatGroq(model_name="llama3-70b-8192", api_key=api_key)


# Define the function to detect encoding
def detect_file_encoding(file_path):
    result = from_path(file_path).best()
    return result.encoding

# Define the function to process the file and chat with it
def chat_with_file(file, query, chat_history):
    try:
        # Determine file type and load accordingly
        if file.name.endswith('.csv'):
            try:
                # Attempt to load the file with UTF-8 encoding
                df = pd.read_csv(file.name)
            except UnicodeDecodeError:
                # If UTF-8 fails, detect and use the actual encoding
                encoding = detect_file_encoding(file.name)
                df = pd.read_csv(file.name, encoding=encoding)

        elif file.name.endswith('.xls') or file.name.endswith('.xlsx'):
            df = pd.read_excel(file.name)
        else:
            return [{"role": "system", "content": "Unsupported file format. Please upload a CSV or Excel file."}], chat_history

        # Create a Pandas dataframe agent
        agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)
        
        # Query the agent
        result = agent.invoke(query)
        response = result['output']

        # Append to chat history
        chat_history.append({"role": "user", "content": query})
        chat_history.append({"role": "assistant", "content": response})
        return chat_history
    except Exception as e:
        error_message = f"Error: {e}"
        chat_history.append({"role": "assistant", "content": error_message})
        return chat_history

# Build Gradio interface
with gr.Blocks() as ui:
    gr.Markdown("### Chat with Your Data Using a ChatGPT-Like Interface")

    chat_history = gr.State([])  # Initialize chat history

    with gr.Row():
        with gr.Column(scale=4):
            file_input = gr.File(label="Upload your CSV or Excel file")
        with gr.Column(scale=8):
            gr.Markdown("#### Chat History")
            chat_log = gr.Chatbot(label="Chat History", type="messages")

    with gr.Row():
        query_input = gr.Textbox(placeholder="Type your question here...", label=None, lines=1)
        chat_button = gr.Button("Send", variant="primary")

    # Set button action
    chat_button.click(
        chat_with_file, 
        inputs=[file_input, query_input, chat_history], 
        outputs=[chat_log]
    )

# Launch the Gradio app
ui.launch()
