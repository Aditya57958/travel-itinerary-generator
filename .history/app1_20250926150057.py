import gradio as gr
import requests
from pyngrok import ngrok, conf
import sys# Start the Gradio interface on a different port
demo.launch(server_name="0.0.0.0", server_port=7861, ssr_mode=False)
# Configure ngrok
conf.get_default().auth_token = "2rvlP8AgOfAVeTPRTxX7eQsXHYN_63XAA8pw8ZvMaucoYyJxJ"

# API Configuration
api_key = "sk-igUDB1syx8WueaauQk6R5p6wwL0hzdB8eeGsZuZG3Xw"

def check_langflow_server():
    """Check if Langflow server is running locally"""
    try:
        response = requests.get("http://localhost:7860/health")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

def setup_ngrok():
    """Setup ngrok tunnel for Langflow server"""
    try:
        # Start ngrok tunnel to Langflow server
        public_url = ngrok.connect(7860).public_url
        print(f"🚀 Langflow public URL: {public_url}")
        return public_url
    except Exception as e:
        print(f"❌ Error setting up ngrok: {e}")
        sys.exit(1)

# Check if Langflow is running
if not check_langflow_server():
    print("❌ Error: Langflow server is not running!")
    print("Please start Langflow server first with: python -m langflow")
    sys.exit(1)

# Setup ngrok tunnel
ngrok_url = setup_ngrok()
if not ngrok_url:
    print("❌ Failed to create ngrok tunnel")
    sys.exit(1)
# Update URL to use ngrok tunnel
url = f"{ngrok_url}/api/v1/run/866fbfbc-2186-4ff9-b520-e452fd54d529"

def create_travel_plan(input_text):
    payload = {
        "output_type": "chat",
        "input_type": "chat",
        "input_value": input_text
    }
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error making API request: {e}"
    except ValueError as e:
        return f"Error parsing response: {e}"

# Gradio UI
with gr.Blocks(title="Aditya's Travel Agency") as demo:
    gr.Markdown("<h1 style='text-align:center'>Make Your Travel Plan with Aditya's Travel Agency ✈️</h1>")
    
    with gr.Row():
        input_text = gr.Textbox(
            label="Enter your travel preferences and details",
            placeholder="E.g., Trip from São Paulo to Uberlândia, MG on August 23, 2024. Enjoys beer, pão de queijo, coffee..."
        )
    
    output_text = gr.Textbox(
        label="Your Travel Itinerary",
        placeholder="Your itinerary will appear here",
        interactive=False
    )
    
    submit_btn = gr.Button("Create Travel Plan")
    submit_btn.click(fn=create_travel_plan, inputs=input_text, outputs=output_text)

# Step 2: Launch Gradio UI (no share=True since Hugging Face doesn’t allow it)
demo.launch(server_name="0.0.0.0", server_port=7860, ssr_mode=False)
