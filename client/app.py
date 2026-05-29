from client import sendAndRecieve
import json

# Maintain conversation history locally
local_chat_state = {
    "messages": [
    ],
}

# Simple chat loop example for talking with the chatbot over the terminal, you can replace this with your own
# application integration
done = False
while not done:
    # Get user prompt
    prompt = input("User: ")
    local_chat_state["messages"].append({"role":"user","content":prompt})

    # Send prompt to the LLM server
    server_payload = {"payload": local_chat_state, "max_tokens": 500}

    # Receive response
    response = sendAndRecieve(server_payload)
    
    try:
        if response.status_code == 200:
            # Success
            response_data = response.json()
            response = response_data["message"]

            print("\nAssistant response: \n\n" + response + "\n")

            # Update local conversation history
            local_chat_state["messages"].append({"role":"assistant","content":""})
        else:
            # Report HTTPExceptions 
            print(f"Server Error (Status {response.status_code}):")
            try:
                # Show JSON response
                print(json.dumps(response.json(), indent=2))
            except ValueError:
                # Fallback if the server returned raw text instead of JSON
                print(response.text)
    except requests.exceptions.ConnectionError:
        print(
            f"Could not connect to {URL}. If you are using Tailscale on the server side, check that Tailscale is also running on your device."
        )
    except requests.exceptions.Timeout:
        print("The request timed out. The LLM server is taking a while to respond.")