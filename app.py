from flask import Flask, request, jsonify
from nlp_processor import NLPProcessor
import datetime

app = Flask(__name__)
nlp_processor = NLPProcessor()
tasks = []

@app.route('/process', methods=['POST'])
def process():
    text = request.json.get('text')
    intent, entities = nlp_processor.parse(text)
    
    if intent == 'remind':
        task = {
            'task': text,
            'due': entities.get('DATE', 'No date specified'),
            'created': datetime.datetime.now().isoformat()
        }
        tasks.append(task)
        response = f"Reminder set: {task['task']}"
    elif intent == 'show' and 'tasks' in text:
        response = "Here are your tasks:\n" + "\n".join([f"{i+1}. {t['task']} due {t['due']}" for i, t in enumerate(tasks)])
    else:
        response = "Sorry, I didn't understand that."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
