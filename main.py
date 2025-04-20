import os
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
import openai
from pathlib import Path

window = tk.Tk()
window.title("OpenAI Prompt Interface")
window.geometry("600x400")

frame = tk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Label(frame, text="Enter your prompt:").pack(anchor="w")
prompt_entry = tk.Entry(frame, width=70)
prompt_entry.pack(fill=tk.X, pady=(0, 10))

tk.Label(frame, text="Response:").pack(anchor="w")
output_text = scrolledtext.ScrolledText(frame, height=15, wrap=tk.WORD)
output_text.pack(fill=tk.BOTH, expand=True)

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def get_completion():
    prompt = prompt_entry.get()
    output_text.delete("1.0", tk.END)
    if not prompt:
        output_text.insert(tk.END, "Please enter a prompt.")
        return
    if not openai.api_key:
        output_text.insert(tk.END, "API key is not set. Check your .env file.")
        return
    try:
        output_text.insert(tk.END, "Loading...")
        window.update()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        text = response.choices[0].message.content.strip()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, text)
    except Exception as e:
        output_text.insert(tk.END, f"Error: {str(e)}")

prompt_entry.bind("<Return>", lambda event: get_completion())
submit_button = tk.Button(frame, text="Submit", command=get_completion)
submit_button.pack(pady=(0, 10))

window.mainloop()
