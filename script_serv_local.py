from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    repo = data.get('repository', {}).get('full_name')
    pusher = data.get('pusher', {}).get('name')
    message = data.get('head_commit', {}).get('message')

    print("\n--- Webhook reçu depuis GitHub ---")
    print(f"Dépôt : {repo}")
    print(f"Auteur : {pusher}")
    print(f"Message du commit : {message}")
    print("----------------------------------\n")

    return "OK", 200

if __name__ == '__main__':
    app.run(port=5000)
