import requests
import json

# Test the MCP server's SSE endpoint
response = requests.get("http://localhost:8000/sse", stream=True)
print(f"Response status: {response.status_code}")
