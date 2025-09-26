import gradio as gr
import requests

# API Configuration
api_key = "sk-igUDB1syx8WueaauQk6R5p6wwL0hzdB8eeGsZuZG3Xw"
url = "http://localhost:7860/api/v1/run/866fbfbc-2186-4ff9-b520-e452fd54d529"

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
        input_text = gr.Textbox(label="Enter your travel preferences and details", placeholder="E.g., Trip from São Paulo to Uberlândia, MG on August 23, 2024. Enjoys beer, pão de queijo, coffee...")
    
    output_text = gr.Textbox(label="Your Travel Itinerary", placeholder="Your itinerary will appear here", interactive=False)
    
    submit_btn = gr.Button("Create Travel Plan")
    submit_btn.click(fn=create_travel_plan, inputs=input_text, outputs=output_text)

demo.launch()
