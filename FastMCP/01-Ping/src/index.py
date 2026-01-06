#!/usr/bin/env python3
"""
FastMCP Ping Server

This is a minimal FastMCP stdio-based server, ported from the Python MCP example.
It initializes a FastMCP server and runs it over stdio (the default transport).
"""

import sys

from fastmcp import FastMCP

if __name__ == "__main__":
    try:
        server = FastMCP(name="luiz-fastmcp-server", version="1.0.0")
        print("Luiz FastMCP Server is running and ready!", file=sys.stderr)
        server.run()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)
