# GPT Terminal Chat (CLI)

A simple and lightweight terminal-based chat application using OpenAI's GPT-3.5-turbo or GPT-4 API.

# Features

- Chat with GPT directly from your terminal.
- Plain text responses only—no HTML, markdown, or emojis.
- Syntax-highlighted code and command outputs using the Rich library.
- Conversation history persists during the session.
- Type `exit` to quit the chat.

# Installation

1. Make sure you have Python 3.7 or higher installed.
2. Set your OpenAI API key as an environment variable `OPENAI_API_KEY` or directly in the script.
3. Install dependencies: 

pip3 install openai
pip3 install rich

Usage: python3 gpt-cli.py

Why Terminal Chat?

Pros:

   - Lightweight and fast: No browser or heavy UI needed.

   - Lower resource consumption: Uses less CPU and RAM than web-based UIs.

   - Readable code and command outputs: Syntax highlighting makes code blocks easy to read.

   - Privacy and security: Entirely runs in your terminal with no web trackers or unnecessary visuals.

Cons:

   - No graphical interface: No buttons, drag-and-drop, or visual enhancements.

   - Less user-friendly for beginners: Not as intuitive as a GUI.

   - No file upload or multimedia support: Text-only chat.

   - Requires manual API key configuration.

# License

This project is licensed under the MIT License - see the [LICENSE.txt](./LICENSE.txt) file for details.
