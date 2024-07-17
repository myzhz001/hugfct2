import gradio as gr

# Define the function for classification with detailed exception handling
def classify_text(text):
    try:
        result = model(text)
        print("Model output:", result)
        # Ensure the result is formatted as a string
        return f"Label: {result[0]['label']}, Score: {result[0]['score']:.4f}"
    except Exception as e:
        print("Error during model inference:", e)
        traceback.print_exc()
        return "Error during model inference"

# Create the Gradio interface
iface = gr.Interface(fn=classify_text, inputs="text", outputs="text")
iface.launch()
