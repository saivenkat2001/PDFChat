import gradio as gr
from dotenv import load_dotenv
from app.pdf_processor import PDFProcessor
from app.chatbot import ChatBot

def main():
    load_dotenv()

    pdf_processor = PDFProcessor()
    chatbot = ChatBot()

    with gr.Blocks() as demo:
        gr.HTML("<h1 align='center'>PDF Chat</h1>")

        with gr.Row():
            upload_files = gr.File(label='Upload a PDF', file_types=['.pdf'], file_count='single')

        chatbot_ui = gr.Chatbot()
        msg = gr.Textbox(label="Enter your question here")
        
        upload_files.upload(pdf_processor.add_docs, upload_files)
        msg.submit(chatbot.answer_query, inputs=[msg, chatbot_ui], outputs=[msg, chatbot_ui])

        demo.launch(share=True)

if __name__ == '__main__':
    print("Starting the application...")
    main()
