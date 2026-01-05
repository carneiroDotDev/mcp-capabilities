#!/usr/bin/env python3
"""
MCP Ping Server

This is a basic MCP server that implements the ping functionality.
The Python SDK for MCP supports ping out of the box, so all we need to do
is initialize the server, set up a transport for it, and then it should
respond to ping requests.

NOTE: When initializing your MCP server, you'll need to provide `name` and
`version` fields. The `name` is a human-readable identifier for your server
(for example, `MyProductName`), and the `version` indicates the version of
your server (such as `1.0.0`). These fields help clients and tools identify
and interact with your server correctly, and are required by the MCP
specification.
"""

import asyncio
import sys
from mcp.server import Server
from mcp.server.stdio import stdio_server


async def main():
    # Create a new MCP Server
    # - it should have a name of 'luiz-mcp-server', title of 'Luiz MCP Server', and a version of '1.0.0'
    # - it should have instructions for the LLM to know what this server can be used to do
    #   (we'll start out by saying it can solve math problems)
    
    server = Server(
        name="luiz-mcp-server",
        version="1.0.0",
    )
    
    # Log server startup (using stderr so it doesn't interfere with stdio communication)
    print("Luiz MCP Server is running and ready to solve math problems!", file=sys.stderr)
    
    # Create stdio transport and connect
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error in main(): {e}", file=sys.stderr)
        sys.exit(1)

