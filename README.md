LLM Question Answering Chatbot is a command-line based Large Language Model project built using Python and Hugging Face Transformers with Google’s FLAN-T5 Large model. This chatbot allows users to ask natural language questions and receive clear, accurate, and deterministic answers directly in the terminal. The project uses the text2text-generation pipeline and an instruction-based prompt format to improve answer quality. Random sampling is disabled to ensure consistent outputs, and a repetition penalty is applied to avoid redundant text. The chatbot runs in a continuous loop and exits gracefully when the user types “exit”.

The model used in this project is google/flan-t5-large, which is an instruction-tuned transformer model suitable for question answering, reasoning, summarization, and conversational tasks. This makes the project ideal for learning Large Language Models (LLMs), Natural Language Processing (NLP), and modern AI workflows.

Project structure includes a main Python file (app.py) that contains the chatbot logic, a README.md for documentation, and optional files like requirements.txt and .gitignore. To run this project, Python 3.9 or above is required along with pip.

To get started, first clone the repository using:
git clone https://github.com/alisaleem1284/HERE-I-HAVE-CREATED-THE-LLM-QUESTION-ANSWER-MODEL-WITH-MEACHINE-LEARING.git
Then move into the project directory and create a virtual environment using:
python -m venv .venv
Activate the virtual environment on Windows using:
.venv\Scripts\Activate.ps1
or on Linux/Mac using:
source .venv/bin/activate

After activating the environment, install the required dependencies:
pip install transformers torch sentencepiece

Once installation is complete, run the chatbot using:
python app.py

After running the script, the terminal will display a message indicating that the chatbot is ready. Users can type any question, and the model will generate a response. Typing “exit” will stop the program and close the chatbot politely.

Internally, the program takes user input, formats it into an instruction-style prompt, sends it to the FLAN-T5 model, and prints the generated response in the terminal. Key parameters include max_new_tokens to control response length, do_sample set to false for deterministic output, and repetition_penalty to reduce repeated phrases.

This project can be extended in the future by adding a Streamlit or Flask web interface, chat history, GPU acceleration, logging, or multi-turn conversation support. It is suitable as a learning project, portfolio showcase, academic experiment, or interview-ready demonstration of LLM usage.

Author: Ali Saleem
GitHub: https://github.com/alisaleem1284
LinkedIn: https://www.linkedin.com/in/ali-saleem-24b26b398/

License: MIT License. This project is free to use, modify, and distribute.
