from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def init_app(kemalphonesolutions):
    db.init_app(kemalphonesolutions)