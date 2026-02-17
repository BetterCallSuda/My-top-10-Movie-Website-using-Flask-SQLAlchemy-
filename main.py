from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from torch import unique
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
'''

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
Bootstrap5(app)

# CREATE DB
class Movie(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer)
    Description = db.Column(db.String(120))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Float)
    review = db.Column(db.String(120))
    img_url = db.Column(db.String(120))

    def __repr__(self):
        return (f"id= {self.title} title= {self.title} year= {self.year} rating= {self.rating}"
                f"ranking= {self.ranking} review= {self.review} img_url= {self.img_url}")


# CREATE TABLE
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
