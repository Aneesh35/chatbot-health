# Chatbot Application

## Overview

This is a Flask-based web application that integrates a chatbot for health-related inquiries. The chatbot uses NLP to understand and respond to user queries, providing information based on symptoms and doctor availability by pincode.

## Files

- **app.py**: Sets up the Flask web application and handles user requests.
- **bot.py**: Contains the chatbot logic, including text processing and response generation.

## Setup

### Prerequisites

- Python 3.x
- Flask
- NLTK

### Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Install the required packages:
    ```bash
    pip install flask nltk
    ```

3. Download NLTK data:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    ```

### Running the Application

1. Ensure `symptom.txt` and `pincodes.txt` are in the same directory as the scripts.
2. Start the Flask application:
    ```bash
    python app.py
    ```
3. Open `http://127.0.0.1:5000/` in your browser to interact with the chatbot.

## Usage

- Enter your health queries or ask for doctor information by pincode on the main page.
- The chatbot responds using data from `symptom.txt` and `pincodes.txt`.

## Project Structure

- **app.py**: 
    - Initializes Flask, defines routes for the main page and AJAX requests.
- **bot.py**: 
    - Loads and preprocesses data.
    - Defines functions for processing inputs and generating responses.
    - Main chatbot logic.

## Contributing

Fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

---

This version is ready for you to copy and paste directly into a README file.
