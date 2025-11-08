from fastmcp import FastMCP

# Minimal FastMCP server with a single tool
mcp = FastMCP("Simple MCP Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers and return the sum."""
    return a + b

@mcp.tool
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"

# Simple resource that clients can read via resources/read
@mcp.resource("resource://welcome")
def welcome_message() -> str:
    """Provides a welcome message via MCP resources."""
    return "Welcome to the Simple MCP Server!"

if __name__ == "__main__":
    # Local development: run HTTP server for easy testing at http://localhost:8000/mcp
    # FastMCP Cloud will import the server object and ignore this block.
    mcp.run(transport="http", host="127.0.0.1", port=8000)