# Ping

👨‍💼 Let's get our MCP server running. The Python SDK for MCP supports `ping`
out of the box, so all we need to do is initialize the server, set up a
transport for it, and then it should respond to `ping` requests.

<callout-info>
	ℹ️ NOTE: When initializing your MCP server, you'll need to provide `name` and
	`version` fields. The `name` is a human-readable identifier for your server
	(for example, `MyProductName`), and the `version` indicates the version of
	your server (such as `1.0.0`). These fields help clients and tools identify
	and interact with your server correctly, and are required by the MCP
	specification.
</callout-info>

Start in `src/index.py` and follow the instructions in the comments.

Right now if you try to run the server, you'll get an error. Let's fix that!

## Testing Your Server

### Option A: Python Test Client

Run the test client:

```bash
cd Python
uv run python 01-Ping/src/test_client.py
```

This will spawn your server and test the ping functionality.

### Option B: MCP Inspector

1. Start the inspector: `npx @modelcontextprotocol/inspector`
2. Configure connection:
   - **Transport**: `stdio`
   - **Command**: `uv`
   - **Args**: `run python 01-Ping/src/index.py`
   - **Working Directory**: `/path/to/mcp-capabilities/Python`
3. Click "Connect" to interact with your server

### Option C: Manual JSON-RPC Test

Send a raw ping request:

```bash
cd Python
echo '{"jsonrpc":"2.0","id":1,"method":"ping"}' | uv run python 01-Ping/src/index.py
```

- 📜 [MCP Python SDK Docs](https://github.com/modelcontextprotocol/python-sdk)
- 📜 [MCP Spec: Ping](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/ping)

