from app import app


@app.route("/")
@app.route("/index")
def index():
    # Mock User
    user = {"username": "adrian"}
    # Return HTML String
    return (
        """
<html>
    <head>
        <title>Microblog | Home</title>
    </head>
    <body>
        <h1>Hello, """
        + user["username"]
        + """!</h1>
    </body>
</html>
        """
    )
