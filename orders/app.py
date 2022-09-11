from flask import Flask
from routes import order_blueprint
from models import db, init_app
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FYCA-9oQeZsOmygFdZyJ4Q'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/order.db'
init_app(app)
app.register_blueprint(order_blueprint)

migrate = Migrate(app, db)
if __name__ == '__main__':
    app.run(debug=True, port=5003)