from database import db

class userinput(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    fname = db.Column(db.str(100), unique=True)
    modele = db.Column(db.str(100))
    problem = db.Column(db.str(1000))


# class AddEnqueteForm(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

#     stelling1 = db.Column(db.String(4), nullable=False)
#     stelling2 = db.Column(db.String(4), nullable=False)