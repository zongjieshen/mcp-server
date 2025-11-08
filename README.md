# Simple FastMCP Server

This repository contains a minimal MCP server built with FastMCP 2.0. It exposes two tools:

- `add(a: int, b: int) -> int`: Returns the sum of two numbers.
- `greet(name: str) -> str`: Returns a friendly greeting.

## Local Development

Prerequisites:
- Python 3.9+
- `pip`

Install dependencies:

```
pip install -r requirements.txt
```

Run the server locally over HTTP:

```
python my_server.py
```

The MCP endpoint will be available at `http://localhost:8000/mcp`.

Optional: Test with a simple client script.

Create `client_test.py`:

```
import asyncio
from fastmcp import Client

async def main():
    async with Client("http://localhost:8000/mcp") as client:
        result = await client.call_tool("greet", {"name": "FastMCP"})
        print(result)

asyncio.run(main())
```

Run it:

```
python client_test.py
```

## Deploy to FastMCP Cloud

FastMCP Cloud hosts MCP servers from your GitHub repository and provides a URL like `https://your-project-name.fastmcp.app/mcp` ([1]).

Steps:
- Push this repository to GitHub (ensure `requirements.txt` is present).
- Sign in to FastMCP Cloud with your GitHub account and create a project.
- Set the entrypoint to `my_server.py:mcp` (Cloud imports the server object and ignores `__main__`) ([2]).
- Deploy; your server becomes available at `https://<project>.fastmcp.app/mcp`.

Notes:
- Cloud automatically installs dependencies from `requirements.txt` ([1]).
- Entry-point configuration accepts `file.py:object_name` syntax if you rename the server instance ([1]).

## References
- [1] FastMCP Cloud guide: https://gofastmcp.com/deployment/fastmcp-cloud
- [2] FastMCP Quickstart: https://gofastmcp.com/getting-started/quickstart