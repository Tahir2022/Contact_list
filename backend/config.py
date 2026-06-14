from flask import Flask  # type: ignore[import]
from flask_sqlalchemy import SQLAlchemy  # type: ignore[import]
from flask_cors import CORS  # type: ignore[import]

app = Flask(__name__) 
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    

db = SQLAlchemy(app)