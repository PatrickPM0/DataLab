from flask import Flask
from routes import blueprints


app = Flask(__name__)
app.config.from_object("config.Config")


for bp in blueprints:
    app.register_blueprint(bp)

if __name__ == "__main__":
    app.run()
