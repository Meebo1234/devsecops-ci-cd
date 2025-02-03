from flask import Flask  # Import Flask

app = Flask(__name__)  # Create Flask app instance

@app.route('/')

def home():   
    return "Hello, DevSecOps World!"  # Return message when visiting "/"

if __name__ == "__main__":   

 app.run(host="0.0.0.0", port=5000)  # Run Flask app
