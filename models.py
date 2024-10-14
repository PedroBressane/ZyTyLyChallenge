import os
from flask import Flask
from dotenv import load_dotenv
from models import db
from routes import register_routes

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

register_routes(app)

if __name__ == '__main__':
    port = int(os.getenv('API_LISTENING_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
