import logging # records what your server is doing
import os
import random
import sys # allows script to exit in case of errors
import requests 
from mcp.server.fastmcp import FastMCP

# Configure logging

name = "demo-mcp-server"

logging.basicConfig(
    level=logging.INFO,
    format = '%(name)s - %(levelname)s - %(message)s',
    handlers = [logging.StreamHandler()]
    )
logger = logging.getLogger(name)

# Creating the MCP server


mcp = FastMCP(name)

# Defining tools

@mcp.tool()
def add(a: int, b: int) -> int:
    logger.info(f"Tool called: add({a} , {b})")
    return a + b

@mcp.tool()
def get_current_weather(city: str) -> str:
    logger.info(f"Tool called: get_current_weather({city})")

    try:
        endpoint = "https://wttr.in"
        response = requests.get(f"{endpoint}/{city}", timeout=15)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logger.error(f"Error fetching weather data: {e}")
        return "Sorry, I couldn't fetch the weather data right now."
    
if __name__ == "__main__":
    logger.info(f"Starting MCP server...")
    try:
       # os.environ['PORT'] = str(port)
        mcp.run(transport = "sse")
    except Exception as e:
        logger.error(f"Error running MCP server: {e}")
        sys.exit(1)
    finally:
        logger.info("MCP server has stopped.")