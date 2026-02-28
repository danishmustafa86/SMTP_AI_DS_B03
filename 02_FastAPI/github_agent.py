import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

SYSTEM_PROMPT = """You are a helpful GitHub assistant. You have access to GitHub tools via MCP.
You can help users:
- Search and explore repositories (code, README, files, structure)
- Summarize project documentation
- Look up GitHub user profiles and their public activity
- Find issues, pull requests, and releases
- Compare repositories or explore organizations

Always be concise, accurate, and cite specific details (repo names, usernames, links) in your answers."""


def extract_text(content_blocks: list) -> str:
    """Pull only text blocks out of a response content list."""
    parts = []
    for block in content_blocks:
        if hasattr(block, "text"):
            parts.append(block.text)
    return "".join(parts).strip()


def run_agent():
    if not ANTHROPIC_API_KEY:
        print("ERROR: ANTHROPIC_API_KEY is not set. Add it to a .env file or your environment.")
        return
    if not GITHUB_TOKEN:
        print("ERROR: GITHUB_TOKEN is not set. Add it to a .env file or your environment.")
        return

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    mcp_servers = [
        {
            "type": "url",
            "url": "https://api.githubcopilot.com/mcp/",
            "name": "github",
            "authorization_token": GITHUB_TOKEN,
        }
    ]

    tools = [
        {
            "type": "mcp_toolset",
            "mcp_server_name": "github",
        }
    ]

    conversation: list[dict] = []

    print("=" * 60)
    print("  GitHub AI Agent  —  Powered by Claude + GitHub MCP")
    print("=" * 60)
    print("Ask me anything about GitHub repositories, profiles,")
    print("documentation, issues, and more.")
    print("Type 'exit' or 'quit' to stop, 'clear' to reset chat.")
    print("=" * 60)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        if user_input.lower() == "clear":
            conversation.clear()
            print("Conversation cleared.")
            continue

        conversation.append({"role": "user", "content": user_input})

        try:
            response = client.beta.messages.create(
                model="claude-opus-4-5",
                max_tokens=4096,
                system=SYSTEM_PROMPT,
                messages=conversation,
                mcp_servers=mcp_servers,
                tools=tools,
                betas=["mcp-client-2025-11-20"],
            )
        except anthropic.APIError as e:
            print(f"\n[API Error] {e}")
            conversation.pop()
            continue

        # Store full content list so tool-use blocks are preserved in history
        conversation.append({"role": "assistant", "content": response.content})

        reply = extract_text(response.content)
        if reply:
            print(f"\nAssistant: {reply}")
        else:
            print("\nAssistant: (no text returned — the agent may have used tools silently)")


if __name__ == "__main__":
    run_agent()
