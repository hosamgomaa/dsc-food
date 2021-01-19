from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:123@localhost:5432/food"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

f_food=db.Table('famous_food',db.metadata,autoload=True,autoload_with=db.engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=["POST"])
def search():
    city = request.form['city']
    city = db.session.query(f_food).filter(f_food.c.city==city).values('food')
    return render_template('results.html', food_names=city)

    


if __name__ =="__main__":
    app.run(debug=True)