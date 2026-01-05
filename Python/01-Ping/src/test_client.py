#!/usr/bin/env python3
import asyncio
import sys
from pathlib import Path

# Add parent directory to path to import mcp
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_ping():
    """Test the ping functionality of the MCP server"""
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", "01-Ping/src/index.py"],
        env=None,
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            # Test ping
            result = await session.send_ping()
            print(f"✅ Ping successful! Result: {result}")
            
            # List available tools/resources (if any)
            try:
                tools = await session.list_tools()
                print(f"📋 Available tools: {len(tools.tools)}")
            except Exception as e:
                print(f"ℹ️  No tools available: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(test_ping())
    except KeyboardInterrupt:
        print("\n⚠️  Test interrupted")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Test failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)