from fastapi import FastAPI
from fastmcp import FastMCP
import subprocess

mcp = FastMCP("EC2ShellExecutor")

@mcp.tool()
async def run_shell(command: str) -> str:
    """
    Run a shell command on the EC2 instance and return output.
    """
    try:
        result = subprocess.run(
            command, shell=True, text=True, capture_output=True, timeout=30
        )
        return result.stdout or result.stderr
    except Exception as e:
        return str(e)

app = FastAPI()
app.mount("/", mcp.sse_app())
