import os
from dotenv import load_dotenv
from groq import Groq
import gradio as gr

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Load system prompt
try:
    with open("system_prompt.md", "r", encoding="utf-8") as f:
        SYSTEM_PROMPT = f.read()
except FileNotFoundError:
    SYSTEM_PROMPT = "You are an expert terminal command generator. Provide ONLY the command itself."

# Core logic
def get_terminal_command(user_text):
    if not user_text.strip():
        return ""
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            max_tokens=150,
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"# Error: {str(e)}"


def main():
    with gr.Blocks(
        theme=gr.themes.Soft(primary_hue="indigo"),
        css="styles.css"
    ) as demo:

        # Header
        gr.Markdown("""
        <div class="header">
            <h1 class="title-gradient">AI Terminal Command Generator</h1>
            <p class="subtitle">
            Transform natural language into precise terminal commands instantly
            </p>
        </div>
        """)

        with gr.Row():
            # Left column: Input + Generate
            with gr.Column(scale=2):
                with gr.Group(elem_classes="glass-box"):
                    text_input = gr.Textbox(
                        label="Your Request",
                        placeholder="Example: Delete all .log files in current directory",
                        lines=4
                    )
                    btn = gr.Button(
                        "Generate Command",
                        variant="primary",
                        size="lg"
                    )

            # Right column: Output + Copy
            with gr.Column(scale=2):
                with gr.Group(elem_classes="glass-box"):
                    text_output = gr.Textbox(
                        label="Generated Command",
                        lines=3,
                        interactive=False,
                        elem_id="output_box",
                        placeholder="Your command will appear here"
                    )

                    gr.HTML("""
                    <button id="copy-btn" style="
                        margin-top: 10px;
                        padding: 8px 15px;
                        border-radius: 8px;
                        background-color: #6366f1;
                        color: white;
                        border: none;
                        cursor: pointer;
                        font-weight: bold;
                    ">
                        Copy Command
                    </button>
                    <script>
                    const btn = document.getElementById('copy-btn');
                    btn.addEventListener('click', () => {
                        const text = document.querySelector('#output_box textarea').value;
                        navigator.clipboard.writeText(text)
                            .then(() => { alert('Command copied to clipboard!'); })
                            .catch(err => { alert('Failed to copy'); });
                    });
                    </script>
                    """)

        # Quick Examples
        gr.Markdown("### ⚡ Quick Examples")
        gr.Examples(
            examples=[
                ["Find all files larger than 200MB"],
                ["List running processes sorted by memory usage"],
                ["Rename all .txt files to .md"],
                ["Check disk usage in human readable format"]
            ],
            inputs=text_input
        )

        # Generate click
        btn.click(
            fn=get_terminal_command,
            inputs=text_input,
            outputs=text_output,
            show_progress="minimal"
        )

    # Launch demo with Render settings
    port = int(os.environ.get("PORT", 8080))
    demo.launch(server_name="0.0.0.0", server_port=port)


if __name__ == "__main__":
    if not api_key:
        print("❌ GROQ_API_KEY not found.")
    else:
        main()
