# WikiWizard

WikiWizard is a web application that allows users to search for information on Wikipedia, get instant summaries, and translate the content into various languages. It also features voice recognition for input and text-to-speech for reading out responses.

## Features

- Instant Wikipedia summaries for user queries.
- Translation of summaries into multiple languages.
- Voice recognition for user queries.
- Text-to-speech for reading out summaries.
- A sleek and interactive user interface.

## Technologies Used

- Python
- Flask
- Wikipedia API
- Google Translate API
- HTML/CSS/JavaScript
- SpeechRecognition API
- Text-to-Speech API

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- Flask
- wikipedia-api
- googletrans==4.0.0-rc1

### Installation

1. Clone the repository:

    ```bash
   Clone This  repository.
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    flask run
    ```

    The application should now be running on `http://127.0.0.1:5000`.

### File Structure
wikiwizard/
│
├── templates/
│ ├── index.html
│ ├── chat.html
│
├── static/
│ ├── styles.css
│ ├── black.mp4
│
├── app.py
├── requirements.txt
└── README.md

### Usage

1. Open a web browser and go to `http://127.0.0.1:5000`.
2. On the home page, click on "Go to Chat" to navigate to the chat interface.
3. Enter your query in the text box, select the language for the response, and click "Send".
4. Optionally, use the voice recognition feature to input your query by clicking the "Start Voice" button.
5. To hear the response, click the "Read Out" button.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Wikipedia API](https://wikipedia-api.readthedocs.io/)
- [Google Translate API](https://pypi.org/project/googletrans/)

## Contact

For any questions or suggestions, please reach out to afzalkhan0008326@gmail.com.

Requirements File (requirements.txt)
Flask==2.0.2
wikipedia-api==0.5.4
googletrans==4.0.0-rc1


