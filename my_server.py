from fastmcp import FastMCP

# Create FastMCP server with stateless_http=True for Copilot Studio compatibility
# This follows Microsoft's recommended pattern for cloud deployment
mcp = FastMCP(
    "Simple MCP Server",
    stateless_http=True,  # Required for Copilot Studio integration
    host="127.0.0.1",
    port=8000
)

@mcp.tool()
async def add(a: int, b: int) -> int:
    """Add two numbers and return the sum."""
    return a + b

@mcp.tool()
async def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"

# Simple resource that clients can read via resources/read
@mcp.resource("resource://welcome")
def welcome_message() -> str:
    """Provides a welcome message via MCP resources."""
    return "Welcome to the Simple MCP Server!"

# Additional tools for better Copilot Studio discovery
@mcp.tool()
async def list_tools() -> list:
    """List all available tools on this MCP server."""
    return [
        {"name": "add", "description": "Add two numbers and return the sum"},
        {"name": "greet", "description": "Return a friendly greeting for the given name"}
    ]

@mcp.tool()
async def get_server_info() -> dict:
    """Get information about this MCP server."""
    return {
        "name": "Simple MCP Server",
        "version": "1.0.0",
        "description": "A simple MCP server with basic arithmetic and greeting tools",
        "tools": ["add", "greet", "list_tools", "get_server_info"],
        "resources": ["welcome"]
    }

if __name__ == "__main__":
    # Use streamable-http transport for Copilot Studio compatibility
    # This is the recommended transport type for Microsoft Copilot Studio
    mcp.run(transport="streamable-http")