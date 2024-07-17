# AI Typing Assistant

(**Credit** : pietro schirano)

This project implements an AI-powered typing assistant that can fix typos, casing, punctuation, and improve the wording of text to make it more clear and concise. The program listens for specific keyboard shortcuts and processes the selected text based on predefined templates using the Ollama AI model.


## Setup Instructions

1. Install the required Python packages by running `pip install -r requirements.txt`.
2. In macOS, it's important to give permission for accessibility and input monitoring to the terminal. You can find these settings under _Privacy & Security -> Input monitoring / Accessibility -> iTerm_.
3. Make sure to have the `ollama` library installed. Instructions can be found [here](https://ollama.ai/docs/sdk/python).
4. Run the `main.py` file in your Python environment.

## Usage

1. The AI assistant runs in the background and listens for keyboard shortcuts.
2. Press `Command+Option` to fix the selected text.
3. Press `Command+Shift+I` to improve the wording of the selected text. 


<p>
  <video src="https://github.com/user-attachments/assets/f778aa75-76e7-4d85-8cdc-fe0ec69cf808" width="800" height="300" controls>
    Your browser does not support the video tag.
  </video>
</p>



## Features

- Automatic text correction for typos, casing, and punctuation.
- Text improvement to enhance clarity, conciseness, and eloquence.
- Ability to preserve new line characters in the processed text.

## Configuration

- `OLLAMA_MODEL`: Specifies the Ollama AI model to be used for text processing.
- `SYSTEM_PROMPT`: System prompt provided to the AI assistant for processing instructions.
- `TEMPERATURE`: Temperature parameter for the AI model.
- `TOP_P`: Top p parameter for the AI model.

## Error Handling

The program includes error handling for exceptions that may occur during text processing and keyboard listener.

Feel free to explore and customize the code to suit your specific text correction and improvement requirements.

