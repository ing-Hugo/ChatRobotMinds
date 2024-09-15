import streamlit as st
from io import BytesIO
from fpdf import FPDF



#*********
import os

from dotenv import load_dotenv




#use a Mind via OpenAI Chat completion API
from openai import OpenAI



load_dotenv()

import requests

API_URL = "http://ec2-3-92-141-83.compute-1.amazonaws.com:3000/api/v1/prediction/4ddce197-2f1a-4a69-bc98-8512e9049641"

def query(payload):
        response = requests.post(API_URL, json=payload)
        return response.json()

your_minds_api_key = os.environ.get( "MIND_API_KEY") or  "MIND_API_KEY"
minds_name = "robots_test2"

# point the Openai SDK to the Minds Cloud
client = OpenAI(
    api_key= "4d32253078ba78d64b3bb400573caccf4973224e1f206ac03e252d5820e4c075",
    base_url='https://llm.mdb.ai/'
)

# print the message before making the API request
print('Answering the question may take up to 30 seconds...')






from io import BytesIO
from fpdf import FPDF

# Custom CSS for futuristic design
def add_futuristic_style():
    st.markdown(
        """
        <style>
        /* General styles for futuristic theme */
        body {
            background-color: #0d0d0d;
            color: white;
            font-family: 'Courier New', Courier, monospace;
        }
        .main > div {
            background: none !important;
        }

        /* Styling for buttons */
        .square-button {
            background-color: #0f0f0f;
            border: 2px solid #33ff99;
            color: #33ff99;
            padding: 20px;
            width: 100%;
            text-align: center;
            margin-bottom: 15px;
            border-radius: 10px;
            font-weight: bold;
            box-shadow: 0 0 15px #33ff99;
            transition: background-color 0.3s ease;
        }

        .square-button:hover {
            background-color: #33ff99;
            color: #0f0f0f;
        }

        /* Chatbot interface */
        .chatbot-box {
            border: 2px solid #33ff99;
            border-radius: 10px;
            padding: 15px;
            background-color: #1a1a1a;
            box-shadow: 0 0 20px #33ff99;
        }

        /* Proposal PDF button */
        .pdf-button {
            background-color: #33ff99;
            color: #0f0f0f;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            font-weight: bold;
            cursor: pointer;
        }

        .pdf-button:hover {
            background-color: #1a1a1a;
            color: #33ff99;
        }
        </style>
        """, unsafe_allow_html=True
    )

# Function to generate a PDF from the robot's data
def generate_pdf(robot_info):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Robot Information", ln=True, align="C")
    for key, value in robot_info.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
    
    # Save the PDF in-memory
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    
    return pdf_output

# Apply the futuristic design
add_futuristic_style()



# Define a function to display the Request Database Robot chatbot page
def show_request_robot_page():
    st.title("Request Database Robot")
    if "chat_engine" not in st.session_state:
            #chat_engine = index.as_chat_engine(chat_mode = "context",verbose = True)
            #chat_engine = index.as_chat_engine(chat_mode = "simple")
            st.title("Request Database Robot")
            
            


            if "messages" not in st.session_state:
                st.session_state.messages=[{
                    
                    
                    "role" : "assistant",
                    "content" : "Ask me a question about the database"+ "" + str(minds_name) ,
                    #   ChatMessage(
                    #      role="assistant", content="Ask me a question about Classiq open source framework for quantum computing?"
                    #     ),
                    
                    }
                    
                    ]

            if prompt:= st.chat_input("Your Question"):
                st.session_state.messages.append({

                    "role" : "user",
                    "content": prompt,
                    #ChatMessage(role="user", content=prompt), 
                }

                )


            for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.write(message["content"])


            if st.session_state.messages[-1]["role"] != "assistant":
                    with st.chat_message("assistant"):
                        with st.spinner("Thinking...."):
                            

                            #response = client.chat.completions.create(
                            #model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                            #messages=[{"role": "user", "content": prompt}],
                            #stream=False,
                            #)
                            
                        
                        # chat with the Mind you created
                         completion = client.chat.completions.create(
                                model=minds_name,
                                messages=[
                                    {'role': 'user', 'content': prompt}
                                ],
                                stream=False
                            )
                                                        
                            
                                
                            
                        
                        print(completion.choices[0].message.content)

                            #response = llm.complete(prompt)
                            #response = chat_engine.chat(prompt)
                            #response = chat_engine.chat(prompt)
                            #st.write(response.response)  
                        st.write(completion.choices[0].message.content) 
                        message = {"role": "assistant", "content":completion.choices[0].message.content}
                        st.session_state.messages.append(message) # Add response to message history

# Define a function to display the Information Data Robot page
def show_information_robot_page():
    st.title("Information Data Robot")
    st.write("This page gives information about the robot you requested.")
   
    output = query({
            "question": "Hey, how are you?",
        })
    print(output)

# Define a function to display the Proposal page
def show_proposal_page():
    st.title("Proposal")
    st.write("This page shows detailed information about the robot and allows you to download a proposal as PDF.")
    
    # Simulated robot information
    robot_info = {
        "Robot ID": "12345",
        "Model": "XR-200",
        "Status": "Requested",
        "Delivery Date": "2024-10-01"
    }
    
    for key, value in robot_info.items():
        st.write(f"**{key}**: {value}")
    
    if st.button("Convert to PDF"):
        st.write("This is where PDF generation would occur.")

# Page navigation logic
def navigate_page():
    st.sidebar.markdown("## Navigation")
    
    if "page" not in st.session_state:
        st.session_state.page = "Welcome"  # Default page
    
    if st.sidebar.button("Request Database Robot"):
        st.session_state.page = "Request"
    
    if st.sidebar.button("Information Data Robot"):
        st.session_state.page = "Information"
    
    if st.sidebar.button("Proposal"):
        st.session_state.page = "Proposal"

    # Page display logic based on button selection
    if st.session_state.page == "Request":
        show_request_robot_page()
    elif st.session_state.page == "Information":
        show_information_robot_page()
    elif st.session_state.page == "Proposal":
        show_proposal_page()
    else:
        st.title("Welcome")
        st.write("Please select a page from the sidebar.")

# Run the navigation logic
navigate_page()
