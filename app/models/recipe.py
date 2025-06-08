from app.utils.extensions import db

class Recipe(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Colum(db.String(120), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    time_minuts = db.Column(db.Integer, nullable=False)

    