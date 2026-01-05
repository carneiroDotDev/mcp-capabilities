// Test the MCP server by sending a ping request
import { Client } from '@modelcontextprotocol/sdk/client/index.js'
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js'

async function test() {
    const client = new Client({
        name: 'TestClient',
        version: '1.0.0',
    })
    
    // This spawns your server!
    const transport = new StdioClientTransport({
        command: 'tsx',
        args: ['01-Ping/src/index.ts'],
    })
    
    await client.connect(transport)
    const result = await client.ping()
    console.log('Ping result:', result)
    
    await client.close()
}

await test().catch(console.error)