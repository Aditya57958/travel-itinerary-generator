import gradio as gr
from app import demo

# Create the Gradio app
app = demo.app

if __name__ == "__main__":
    demo.launch()