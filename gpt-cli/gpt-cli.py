import openai
import os
from rich.console import Console
from rich.syntax import Syntax

openai.api_key = "YOUR_API_KEY_HERE"

console = Console()

messages = [
    {"role": "system", "content": "You are an AI assistant running in a terminal. Only return plain text answers. No HTML, no markdown, no emojis."}
]

print("\n\033[1;32mGPT Terminal Chat (to log out type 'exit')\033[0m")

while True:
    user_input = input("\n\033[1;36m>\033[0m ")
    if user_input.strip().lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response.choices[0].message.content.strip()

        if "```" in reply:
            parts = reply.split("```")
            console.print(parts[0])
            for i in range(1, len(parts), 2):
                code = parts[i + 0]
                lang = "bash" if code.startswith("bash\n") else "python"
                code = code.replace("bash\n", "").replace("python\n", "")
                syntax = Syntax(code, lang, theme="monokai", line_numbers=False)
                console.print(syntax)
                if i + 1 < len(parts):
                    console.print(parts[i + 1])
        else:
            console.print(reply)

        messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
