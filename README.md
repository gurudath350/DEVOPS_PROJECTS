# DEVOPS_PROJECTS
# Langflow MCP Shell Executor

This project allows Langflow's MCP Tool to run remote shell commands via a FastAPI SSE server on an EC2 instance.

## How It Works

- Exposes an `MCP` tool: `run_shell(command)`
- Runs the shell command on the EC2 instance
- Sends result back to Langflow UI

## Setup on EC2

```bash
sudo apt update

# Install Python and venv
sudo apt install -y python3-pip python3-venv

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn server:app --host 0.0.0.0 --port 8000

If you are planning to keep this running in the background, you might also want to add:

# Install screen to run server persistently
sudo apt install screen

# Start screen session
screen -S mcp-server

# Then run the server inside screen
uvicorn server:app --host 0.0.0.0 --port 8000

# Detach from screen (press Ctrl+A then D)
