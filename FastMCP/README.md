# FastMCP Exercises

This folder contains the FastMCP implementation of the MCP exercises (ported from the Python examples).

## Prerequisites

- Python 3.10 or higher
- `uv` (optional) - used in examples to run commands in an isolated environment

## Setup

From the `FastMCP/` directory, install dependencies using `uv` (optional) or your preferred tool:

```bash
cd FastMCP
uv sync    # if you use `uv`
```

Alternatively, create/activate a venv and `pip install -r requirements.txt`.

## Running Projects

### 01-Ping

This is a simple FastMCP-based ping server that communicates over stdio.

Run the Ping server directly:

```bash
# From the FastMCP/ directory
uv run python 01-Ping/src/index.py
```

Or, if you prefer using the system Python with a virtual environment:

```bash
python 01-Ping/src/index.py
```

### Testing the Ping Server

Use the provided test client to spawn and test the server (it uses stdio transport):

```bash
# From the FastMCP/ directory
uv run python 01-Ping/src/test_client.py
```

This will:
- spawn the `01-Ping` server as a child process
- initialize a client session
- send a `ping` request and print the result

### Using the MCP Inspector

You can also use the MCP Inspector (Node.js tool) to connect to stdio-based servers.

```bash
# Run the inspector (via npx)
npx @modelcontextprotocol/inspector
```

Configure a new connection in the inspector:
- Transport: `stdio`
- Command: `uv` (or `python`)
- Args: `run python 01-Ping/src/index.py` (or `01-Ping/src/index.py`)
- Working Directory: full path to this `FastMCP/` folder
