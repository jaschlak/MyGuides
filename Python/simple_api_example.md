# API simple example

    this is a simple example of how to setup a python api from video: https://www.youtube.com/watch?v=s_ht4AKnWZg
    
## code

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return("Hello World!")

    if __name__ == '__main__':
        app.run(debug=True,port=5433)