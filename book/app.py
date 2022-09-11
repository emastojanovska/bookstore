from flask import Flask
from routes import book_blueprint
from models import db, init_app
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'OOQs-wGt2Fq5oWHfb8wOAA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(book_blueprint)
init_app(app)
migrate = Migrate(app, db)
if __name__ == '__main__':
    app.run(debug=True, port=5002)

