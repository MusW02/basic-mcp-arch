# 🚀 Basic MCP Architecture (FastMCP)

> A clean, extensible **Model Context Protocol (MCP) server** built with Python — designed to connect AI assistants to local tools and cloud LLMs.





---

## 📌 Overview

This project demonstrates a **minimal yet powerful MCP server architecture** using `fastmcp`.

It acts as a bridge between:

* 🧠 AI Assistants (Claude Desktop, Cursor)
* 🛠️ Local Tools (Python functions)
* ☁️ Cloud LLM APIs (Ollama / DeepSeek)

Perfect for:

* Learning MCP
* Building AI-powered developer tools
* Experimenting with LLM integrations

---

## ⚡ Features

### 🔧 Available Tools

| Tool                           | Description                    |
| ------------------------------ | ------------------------------ |
| `add(a, b)`                    | Simple calculator tool         |
| `get_current_weather(city)`    | Fetches real-time weather data |
| `ask_llama(prompt)`            | Sends prompt to Ollama Cloud   |
| `chat_with_deepseek(messages)` | Stateful chat with DeepSeek    |

---

## 🧠 Architecture

```
Claude Desktop / Cursor
          ↓
     MCP Client
          ↓
   FastMCP Server (Python)
          ↓
 ┌───────────────┬───────────────┐
 │ Local Tools   │ Cloud LLM APIs│
 │ (Functions)   │ (Ollama)      │
 └───────────────┴───────────────┘
```

---

## 🛠️ Tech Stack

* **Python 3.11+**
* **fastmcp**
* **requests**
* **Ollama Cloud API**
* **DeepSeek API**

---

## 📦 Installation

### 1. Clone the repo

```powershell
git clone https://github.com/MusW02/basic-mcp-arch.git
cd basic-mcp-arch
```

### 2. Create virtual environment

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### 🔑 Environment Variable

Set your API key:

```
OLLAMA_API_KEY=your_api_key_here
```

---

## 🤖 Connect with Claude Desktop

### 📍 Config File Location

* **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
* **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`

### 🧩 Add this configuration:

```json
{
  "mcpServers": {
    "demo-mcp-server": {
      "command": "C:\\Path\\To\\basic-mcp-arch\\venv\\Scripts\\python.exe",
      "args": ["C:\\Path\\To\\basic-mcp-arch\\server.py"],
      "env": {
        "OLLAMA_API_KEY": "your_ollama_cloud_api_key_here"
      }
    }
  }
}
```

### 🔄 Restart Claude Desktop

Now try:

* “Check weather in London”
* “Ask DeepSeek about AI trends”

---

## 📂 Project Structure

```
basic-mcp-arch/
│
├── server.py          # MCP server + tools
├── requirements.txt  # Dependencies
├── README.md         # Documentation
└── .gitignore        # Ignored files
```

---

## 🔄 Transport Layer

Default:

```python
mcp.run(transport="stdio")
```

For browser testing (MCP Inspector):

```python
mcp.run(transport="sse")
```

---

## 🎯 Use Cases

* Build **AI developer assistants**
* Connect **Figma / APIs / Databases to LLMs**
* Prototype **AI workflows**
* Learn **MCP architecture (important skill in 2025+)**

---

## 🚀 Future Improvements

* [ ] Add authentication layer
* [ ] Add database tools
* [ ] Add streaming responses
* [ ] Docker support
* [ ] Web dashboard

---

## 🤝 Contributing

Pull requests are welcome!

If you find a bug or want to improve something:

1. Fork the repo
2. Create a branch
3. Submit a PR

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this useful:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share it

---

## 👨‍💻 Author

**Mustafa Waqar**
Aspiring ML Engineer | AI & Data Science

---
