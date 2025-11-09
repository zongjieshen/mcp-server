import asyncio
from fastmcp import Client

# Add your FastMCP Cloud API key here
API_KEY = "fmcp_B6_S9f81eWKNDPEZIA6V0yHNnHJNg_HBj5IS1mo2AT8"

# Configuration-based client to include headers (per FastMCP Client docs)
config = {
    "mcpServers": {
        "server": {
            "transport": "http",
            "url": "https://zongjie-mcp-server-test.fastmcp.app/mcp",
            "headers": {"Authorization": f"Bearer {API_KEY}"},
        }
    }
}

client = Client(config)

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()
        
        # Execute operations
        # With configuration-based clients, tools are prefixed with the server name key
        result = await client.call_tool("greet", {"name": "FastMCP"})
        print(tools)
        print(resources)
        print(prompts)

asyncio.run(main())