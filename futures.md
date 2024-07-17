
## Future Scope
1. The binary should be easily installable on Mac using `brew install`.
2. After installation, the user should initiate the system check.
3. The system check will verify the following:
   1. Is Ollama installed on the system?
   2. Does Ollama have gemma2 or allow users to choose the model for Ollama to run with?
   3. Is Input monitoring accessible?
   4. Is iTerm accessibility checked?
   5. Once the system check is completed, a message will be displayed in the terminal indicating the status of each check.
4. If all statuses are satisfactory, the `tyassist` will prompt to run `tyassist start --background` or `tyassist start`.
5. Upon running the app in the background, the specified shortcut key can be pressed to rephrase the string and copy it to the clipboard.
6. Convert it to **RUST**