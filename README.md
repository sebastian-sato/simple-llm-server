# simple-llm-server
Simple Python HTTP server for accessing a locally hosted LLM over the web or a VPN (like Tailscale).

This is primarily intended for personal use of a local LLM, or for simple LLM enabled projects. It is not suitable for general deployment.

**Get dependencies:**
```
pip3 install fastapi uvicorn
```
**Setting up with Tailscale:**
1. Install Tailscale on the machine running the LLM, you can find installation instructions at tailscale.com
2. Set up a "funnel" on the LLM machine via this command: ```sudo tailscale funnel --bg 8000``` so that it is accessible from anywhere
3. Install Tailscale on any devices you would like to access the LLM from.
4. Run server.py on the LLM hosting machine. You will need to have Hugging Face's transformers library installed in the Python environment. You will probably want to use a different model than what I'm using, so some changes will be necessary.
5. app.py and client.py provide an example of connecting to the server and using the LLM as a chatbot. To test it, make sure Tailscale is installed on your other device and run app.py to connect to the server.

It is not strictly required to use a VPN like Tailscale, but it is advisable, since this implementation currently does not include any form of authentication.
