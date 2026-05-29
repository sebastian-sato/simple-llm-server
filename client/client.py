import requests

SERVER_IP = "123.456.789.10" # Replace with your server's internet facing or Tailscale IP, or localhost if using an SSH tunnel.
PORT = "8000"
URL = f"http://{SERVER_IP}:{PORT}/chat"

def sendAndRecieve(payload):
    return requests.post(URL, json=server_payload, timeout=60)