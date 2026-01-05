import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'

// MCP TypeScript SDK Docs:
//   https://github.com/modelcontextprotocol/typescript-sdk

const luizMcpServer = new McpServer(
	{
		// server id should be lowercase and a short name
		name: 'luiz-mcp-server',
		// human-friendly title
		title: 'Luiz MCP Server',
		version: '1.0.0',
	},
    {
        instructions: `You are Luiz MCP Server, an AI that can solve math problems. 
		You can perform addition, subtraction, multiplication, and division. 
		Always provide clear and concise explanations for your solutions.`,
    }
)

async function main() {
	// create a new StdioServerTransport
	const transport = new StdioServerTransport()
	// connect the server to the transport
	await luizMcpServer.connect(transport)

	// add a log (using console.error) to the console to let the user know the server is running
	console.error('Luiz MCP Server is running and ready to solve math problems!')
}

main().catch((error) => {
	console.error('Fatal error in main():', error)
	process.exit(1)
})

