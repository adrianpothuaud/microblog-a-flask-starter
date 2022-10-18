from app import app

@app.route("/")
@app.route("/index")
def index():
    # Greeting as a String
    return "Hello, World!"
