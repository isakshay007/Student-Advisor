import os
import shutil
import streamlit as st
from PIL import Image
from lyzr import ChatBot

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

# Set Streamlit page configuration
st.set_page_config(
    page_title="Lyzr",
    layout="centered",
    initial_sidebar_state="auto",
    page_icon="./logo/lyzr-logo-cut.png",
)

# Load and display the logo
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Student Advisor🎓")
st.markdown("### Built using Lyzr SDK🚀")
st.markdown("Navigate your academic journey effortlessly with our Student Advisor app, leveraging Lyzr's ChatBot for personalized insights tailored to your coursework and ambitions.")

# Function to remove existing files in the directory
def remove_existing_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            st.error(f"Error while removing existing files: {e}")

# Set the local directory
data_directory = "data"

# Create the data directory if it doesn't exist
os.makedirs(data_directory, exist_ok=True)

# Remove existing files in the data directory
remove_existing_files(data_directory)


# Function to implement RAG Lyzr Chatbot
def rag_implementation(file_path):
    # Check the file extension
    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() == ".pdf":
        # Initialize the PDF Lyzr ChatBot
        rag = ChatBot.pdf_chat(
            input_files=[file_path],
            llm_params={"model": "gpt-4"},
        )
    elif file_extension.lower() == ".docx":
        # Initialize the DOCX Lyzr ChatBot
        rag = ChatBot.docx_chat(
            input_files=[file_path],
            llm_params={"model": "gpt-4"},
        )
    else:
        # Handle unsupported file types
        raise ValueError("Unsupported file type. Only PDF and DOCX files are supported.")

    return rag


# Function to get Lyzr response
def advisor_response(file_path, ambition):
    rag = rag_implementation(file_path)
    prompt = f"""Your name is Isha, always remember that, and you are a student advisor at a university. Always introduce yourself.
                 
                 To generate advice for the uploaded document, please follow the instructions below:
                    
                      - Course work and grades: Being a Student Advisor, look into the uploaded marksheet and give important insights about where the student performance lies.
                     
                      - Ambition: Informed by the student's ambition (replace {ambition}), advise them on the steps required to excel in their chosen path.
                     
                      - Academic advice: Being a Student Advisor, look into the uploaded document and give important insights about where the student's strength and weaknesses lie and how to improve them.
                     
                      - Career guidance: Being a student Advisor utilize the student's ambition, coursework, and grades, offer pertinent suggestions for their career trajectory.
                     
                      - Personal development: Being a student Advisor offer guidance on fostering high productivity through effective time management techniques and engaging in relevant extracurricular activities.
                     
                      - Please ensure adherence to these steps and provide responses akin to a student advisor. """

    response = rag.chat(prompt)
    return response.response

# File upload widget
uploaded_file = st.file_uploader("Upload your Marksheet⬇️", type=["pdf", "docx"])

if uploaded_file is not None:
    # Save the uploaded file to the data directory
    file_path = os.path.join(data_directory, uploaded_file.name)
    with open(file_path, "wb") as file:
        file.write(uploaded_file.getvalue())
    
    # Display the path of the stored file
    st.success("File successfully saved")

    # User input for student's ambition
    ambition = st.text_input("What is your Ambition?")

    # Generate advice button
    if st.button("Get Advice"):
        if not ambition:
            st.warning("Please enter your ambition.")
        else:
            automatic_response = advisor_response(file_path, ambition)
            st.markdown(automatic_response)

# Footer or any additional information
with st.expander("ℹ️ - About this App"):
    st.markdown(
        """Experience the seamless integration of Lyzr's ChatBot as you refine your documents with ease. For any inquiries or issues, please contact Lyzr."""
    )
    st.link_button("Lyzr", url="https://www.lyzr.ai/", use_container_width=True)
    st.link_button(
        "Book a Demo", url="https://www.lyzr.ai/book-demo/", use_container_width=True
    )
    st.link_button(
        "Discord", url="https://discord.gg/nm7zSyEFA2", use_container_width=True
    )
    st.link_button(
        "Slack",
        url="https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw",
        use_container_width=True,
    )
