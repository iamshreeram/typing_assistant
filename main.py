import time
from string import Template
import ollama
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
from colorama import init, Fore, Style
 
# Initialize colorama for cross-platform colored output
init()
 
controller = Controller()

# Configuration (could be moved to a separate config file)
OLLAMA_MODEL = "gemma2"
SYSTEM_PROMPT = """You are an AI assistant designed to help with text correction and improvement.
Your task is to process the given text according to the specific instructions provided.
IMPORTANT: Return only the corrected or improved text. Do not include any explanations or additional text in your response."""
 
# Model parameters
TEMPERATURE = 0.1
TOP_P = 0.3
 
FIX_PROMPT_TEMPLATE = Template(
"""Fix all typos and casing and punctuation in this text, but preserve all new line characters:
$text"""
)
 
IMPROVE_PROMPT_TEMPLATE = Template(
"""Improve the wording of this text to make it more clear, concise, and eloquent, while preserving the original meaning and all new line characters:
$text"""
)
 
def colored_print(color, message):
    print(f"{color}{Style.BRIGHT}{message}{Style.RESET_ALL}")
 
def process_text(text, template):
    colored_print(Fore.CYAN, f"Sending text to model: {text[:50]}...")  # Print only the first 50 characters
    prompt = template.substitute(text=text)
    try:
        response = ollama.generate(
            model=OLLAMA_MODEL,
            prompt=prompt,
            system=SYSTEM_PROMPT,
            options={"temperature": TEMPERATURE,"top_p": TOP_P}
        )
        processed_text = response['response'].strip()
        colored_print(Fore.CYAN, f"Model returned processed text: {processed_text[:50]}...")
        return processed_text
    except Exception as e:
        colored_print(Fore.RED, f"Error in process_text: {str(e)}")
        return None
 
def modify_selection(template):
    colored_print(Fore.CYAN, "Triggered text modification.")
    original_clipboard = pyperclip.paste()

    try:
        # Copy selection to clipboard
        with controller.pressed(Key.cmd):
            controller.tap('c')
        time.sleep(0.1)
 
        text = pyperclip.paste()
        if not text or text == original_clipboard:
            colored_print(Fore.CYAN, "No text selected or clipboard unchanged.")
            return
 
        modified_text = process_text(text, template)
        if not modified_text:
            return
 
        # Paste the modified string
        pyperclip.copy(modified_text)
        time.sleep(0.1)
        with controller.pressed(Key.cmd):
            controller.tap('v')
        colored_print(Fore.CYAN, "Replaced text with modified version.")
 
    except Exception as e:
        colored_print(Fore.RED, f"Error in modify_selection: {str(e)}")
    finally:
        # Restore original clipboard content
        time.sleep(0.1)
        pyperclip.copy(original_clipboard)
 
def on_cmd_option():
    modify_selection(FIX_PROMPT_TEMPLATE)
 
def on_cmd_shift_i():
    modify_selection(IMPROVE_PROMPT_TEMPLATE)
 
colored_print(Fore.CYAN, "AI powered typing assistant is running in the background.")
colored_print(Fore.CYAN, "Press Command+Option to fix the selected text.")
colored_print(Fore.CYAN, "Press Command+Shift+I to improve the wording of the selected text.")

try:
    with keyboard.GlobalHotKeys({
        '<cmd>+<alt>': on_cmd_option,
        '<cmd>+<shift>+i': on_cmd_shift_i
    }) as h:
        h.join()
except Exception as e:
    colored_print(Fore.RED, f"Error in keyboard listener: {str(e)}")

