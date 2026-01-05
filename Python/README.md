# MCP Capabilities - Python

This directory contains Python exercises for MCP (Model Context Protocol) servers.

## Prerequisites

- Python 3.10 or higher
- [UV](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

## Setup

From the `Python/` directory, install dependencies using UV:

```bash
cd Python
uv sync
```

This will:
- Create a virtual environment (if it doesn't exist)
- Install all dependencies from `pyproject.toml`
- Install development dependencies (pytest, etc.)

## Running Projects

### 01-Ping

**Important**: MCP servers using stdio don't listen on a network port. They communicate via standard input/output (stdin/stdout). To test and interact with your server, use the MCP Inspector (see below).

Run the Ping server directly (for testing):

```bash
# From the Python/ directory
uv run python 01-Ping/src/index.py
```

## Using the MCP Inspector

The MCP Inspector is a web-based tool that lets you interact with your MCP server through a browser interface. It works with stdio-based servers by spawning your server as a child process.

### Installation

The MCP Inspector is a Node.js tool. You can use it globally or via npx:

```bash
# Install globally (optional)
npm install -g @modelcontextprotocol/inspector

# Or use npx (no installation needed)
npx @modelcontextprotocol/inspector
```

### Running the Inspector

1. **Start the Inspector**:

```bash
# From the Python/ directory
npx @modelcontextprotocol/inspector
```

This will:
- Start a local web server (typically on port 3000 or similar)
- Open your browser to the inspector interface
- Display connection instructions

2. **Configure the Server Connection**:

In the MCP Inspector web interface, you'll need to configure:

- **Transport**: `stdio`
- **Command**: `uv` (or `python` if you prefer)
- **Args**: `run python 01-Ping/src/index.py`
- **Working Directory**: The full path to your `Python/` directory

**Example configuration**:
- Transport: `stdio`
- Command: `uv`
- Args: `run python 01-Ping/src/index.py`
- Working Directory: `/mcp-capabilities/Python`

**Alternative using python directly** (if you have the venv activated):
- Transport: `stdio`
- Command: `python`
- Args: `01-Ping/src/index.py`
- Working Directory: `/mcp-capabilities/Python`

3. **Test the Connection**:

Once connected, you can:
- Send a `ping` request to verify the server is working
- View server capabilities
- Test tools and resources (as you add them)
- See request/response logs

### Quick Test Script

You can also create a simple test script. Create `test_ping.py` in the `Python/` directory:

```python
#!/usr/bin/env python3
import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_ping():
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", "01-Ping/src/index.py"],
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.ping()
            print("Ping successful!", result)

if __name__ == "__main__":
    asyncio.run(test_ping())
```

## Development

### Adding Dependencies

To add a new dependency:

```bash
uv add <package-name>
```

To add a development dependency:

```bash
uv add --dev <package-name>
```

### Running Tests

Run tests using pytest:

```bash
uv run pytest
```

### Activating the Virtual Environment

If you want to activate the virtual environment manually:

```bash
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

However, with UV, you typically don't need to activate the venv - just use `uv run` for commands.

## Project Structure

```
Python/
├── pyproject.toml          # Project dependencies and configuration
├── requirements.txt         # Alternative dependency file (for reference)
├── .venv/                   # Virtual environment (created by UV)
└── 01-Ping/                 # First exercise
    ├── src/
    │   ├── __init__.py
    │   └── index.py         # Main server file
    └── README.md
```

## Notes

- UV automatically manages the virtual environment in `.venv/`
- Dependencies are defined in `pyproject.toml`
- Use `uv run` to execute commands in the project's virtual environment
- The `requirements.txt` file is kept for reference but UV primarily uses `pyproject.toml`

