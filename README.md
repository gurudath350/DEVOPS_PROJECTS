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
sudo apt install python3-pip
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8000
