from flask import Flask, render_template, request, jsonify
import wikipedia
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/get_summary', methods=['POST'])
def get_summary():
    data = request.json
    query = data.get('query')
    target_language = data.get('language', 'en')
    
    try:
        # Detect language of the query
        query_language = translator.detect(query).lang
        
        # Translate the query to English if it's not already in English
        if query_language != 'en':
            query = translator.translate(query, src=query_language, dest='en').text
        
        # Fetch summary in English
        summary = wikipedia.summary(query, sentences=3)

        # Translate the summary to the target language
        translated_summary = translator.translate(summary, src='en', dest=target_language).text
    except wikipedia.exceptions.DisambiguationError as e:
        translated_summary = f"Your query is ambiguous, please be more specific. Possible options: {', '.join(e.options)}"
    except wikipedia.exceptions.PageError:
        translated_summary = "The page does not exist, please try another query."
    except Exception as e:
        translated_summary = f"An error occurred: {e}"
    
    return jsonify({'summary': translated_summary})

if __name__ == '__main__':
    app.run(debug=True)
