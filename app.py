from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from wednesday.agent import ConversationAgent

import logging

app = Flask(__name__)

logging.basicConfig(filename='log.txt', level=logging.INFO)
CORS(app)

# have to initialise the chat agent outside the function body
# Since this has to maintain the context globaly
chat_agent = ConversationAgent()

@app.route('/query', methods=['POST'])
@cross_origin()
def respond_to_user():
    """
    Respond to user query.
    """
    query_raw = request.get_json()
    if not isinstance(query_raw, dict):
        return jsonify({'error': 'Invalid input format expect a dict with \'message\' as a key'}), 400
    
    if not query_raw.get('message'):
        return jsonify({'error': 'system expects \'message\' as a key in the request body'}), 400

    query = query_raw['message']
    response = {'response': chat_agent.respond(query)}

    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
