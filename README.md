Chatbot Application
Overview
This is a Flask-based web application that integrates a chatbot for health-related inquiries. The chatbot uses Natural Language Processing (NLP) to understand and respond to user queries. The chatbot can provide information based on symptoms and find doctors based on provided pincodes.

Files
app.py: This file sets up the Flask web application, defines the routes, and handles user requests.
bot.py: This file contains the chatbot logic, including text processing and response generation.
Setup
Prerequisites
Python 3.x
Flask
NLTK (Natural Language Toolkit)
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
cd <repository_name>
Install the required Python packages:

bash
Copy code
pip install flask nltk
Download the NLTK data required for the chatbot:

python
Copy code
import nltk
nltk.download('punkt')
nltk.download('wordnet')
Running the Application
Ensure that you have the symptom.txt and pincodes.txt files in the same directory as the Python scripts. These files should contain the symptom descriptions and doctor information by pincode, respectively.

Start the Flask application:

bash
Copy code
python app.py
Open your web browser and navigate to http://127.0.0.1:5000/ to interact with the chatbot.

Usage
On the main page, you can enter your query about health symptoms or ask for doctor information based on pincode.
The chatbot will respond to your queries using the data from symptom.txt and pincodes.txt.
Project Structure
app.py:
Initializes and configures the Flask application.
Defines two routes:
/ for serving the main page.
/entry for handling AJAX requests from the frontend.
bot.py:
Loads and preprocesses the data from symptom.txt and pincodes.txt.
Defines various functions for processing user inputs and generating responses.
Contains the main logic for understanding and responding to user queries.
Detailed Explanation of Code
app.py
Imports:
Flask, render_template, request, jsonify, make_response from flask
chat from bot
Routes:
/: Renders the main HTML page.
/entry: Handles POST requests to generate a chatbot response.
bot.py
Imports:
nltk, re, random, string
NLP Setup:
Downloads necessary NLTK datasets.
Reads and preprocesses the symptom and pincode data.
Response Functions:
LemTokens, LemNormalize: Tokenization and normalization functions.
Various predefined responses and patterns for different types of queries (e.g., greetings, symptoms, doctor lookup).
chat: Main function to handle user input and generate appropriate responses.
Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
