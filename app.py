from flask import Flask
from general.general import index_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(index_bp)

if __name__ == "__main__":
    app.run()
