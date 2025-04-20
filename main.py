import openai
import tkinter as tk
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()
api_key = os.getenv("key")

# Set the API key to your own api 
openai.api_key = api_key

# Function to call OpenAI's API
def get_completion():
    prompt = prompt_entry.get()
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can also use "gpt-3.5-turbo-instruct"
            prompt=prompt,
            max_tokens=100
        )
        output_text.delete("1.0", tk.END)  # Clear previous output
        output_text.insert(tk.END, response.choices[0].text.strip())
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}")

# Create the GUI
window = tk.Tk()
window.title("OpenAI Prompt Completer")

tk.Label(window, text="Enter your prompt:").pack()

prompt_entry = tk.Entry(window, width=60)
prompt_entry.pack(pady=5)

submit_button = tk.Button(window, text="Submit", command=get_completion)
submit_button.pack(pady=5)

tk.Label(window, text="Output:").pack()

output_text = tk.Text(window, height=10, width=60)
output_text.pack(pady=5)

window.mainloop()
