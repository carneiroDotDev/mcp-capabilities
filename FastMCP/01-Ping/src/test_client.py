#!/usr/bin/env python3
"""Test client for the FastMCP Ping Server."""

import asyncio

from fastmcp.client import Client
from fastmcp.client.transports import PythonStdioTransport


async def test_ping():
    """Test the ping functionality of the FastMCP server."""
    transport = PythonStdioTransport("01-Ping/src/index.py")
    client = Client(transport)

    async with client:
        tools = await client.list_tools()
        print(f"✅ Connected. Available tools: {len(tools)}")


if __name__ == "__main__":
    asyncio.run(test_ping())
