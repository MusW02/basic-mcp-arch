import logging # records what your server is doing
import os
# import random
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

OLLAMA_API_KEY = os.environ.get('OLLAMA_API_KEY')
if not OLLAMA_API_KEY:
    logger.warning("LLAMA_API_KEY environment variable not set. Some tools may not work properly.")

OLLAMA_MODEL = "deepseek-v3.1:671b-cloud"

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
    
@mcp.tool()
def ask_llama(prompt: str, max_tokens:int = 100) -> str:
    if not OLLAMA_API_KEY:
        logger.warning("LLAMA_API_KEY not set. Returning error message.")
        return "LLAMA_API_KEY environment variable not set. Please set it to use this tool."
    
    logger.info(f"Tool called: ask_llama(prompt='{prompt}')")
    
    try:
        headers = {
            "Authorization": f"Bearer {OLLAMA_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }

        ollama_endpoint = "https://ollama.com/api/generate"

        response = requests.post(
            ollama_endpoint,
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()

        result = response.json()
        return result.get("response", "No response from Llama.")
    
    except requests.RequestException as e:
        logger.error(f"Error communicating with Ollama API: {e}")
        return "Sorry, I couldn't communicate with the Llama API right now."   
    
@mcp.tool()
def chat_with_deepseek(messages: list, max_tokens: int = 512) -> str:
    if not OLLAMA_API_KEY:
        return "LLAMA_API_KEY environment variable not set. Please set it to use this tool."
    
    logger.info(f"Tool called: chat_with_deepseek with {len(messages)} messages")

    try:
        headers = {
            "Authorization": f"Bearer {OLLAMA_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": OLLAMA_MODEL,
            "messages": messages,
            "stream":False
        }

        ollama_endpoint = "https://ollama.com/api/chat"

        response = requests.post(
            ollama_endpoint,
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()

        result = response.json()
        return result.get("message", {}).get("content", "No response from DeepSeek.")

    except requests.RequestException as e:
        logger.error(f"Error communicating with Ollama API: {e}")
        return "Sorry, I couldn't communicate with the Llama API right now."
    
  
if __name__ == "__main__":
    logger.info("Starting MCP server...")
    try:
        mcp.run(transport = "stdio")
    except Exception as e:
        logger.error(f"Error running MCP server: {e}")
        sys.exit(1)
    finally:
        logger.info("MCP server has stopped.")