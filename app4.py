from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Add this line to set the secret key
bootstrap = Bootstrap(app)

watches = [
    { "name": "Rolex Datejust", "price": "12.000 $", "description": "Iconic and timeless, Rolex watches are renowned for their precision, durability, and luxury. A symbol of success and craftsmanship.", "image": "Rolex_Datejust.jpg"},
    { "name": "Audemars Piguet Royal Oak", "price": "32.000 $", "description": "Bold and innovative, AP blends cutting-edge design with traditional Swiss watchmaking, best known for the Royal Oak.", "image": "Audemars_Piguet_Royal_Oak.jpg"},
    { "name": "Patek Philippe Nautilus", "price": "75.000 $", "description": "The pinnacle of horology, Patek Philippe creates elegant, highly intricate timepieces that hold their value for generations.", "image": "Patek_Philippe_Nautilus.jpg"},
]

class OpinionForm(FlaskForm):
    number = StringField('How many watches do you want to add to your shopping cart?', validators=[DataRequired(), Length(min=1, max=2)])
    submit = SubmitField('Submit')

@app.route('/')
def galleryPage():
    return render_template('index.html', watches=watches)

@app.route('/watch/<int:watchId>', methods=['GET', 'POST'])
def singleProductPage(watchId):
    form = OpinionForm()
    if form.validate_on_submit():
        number = form.number.data
        flash(f'Added {number} of {watches[watchId]["name"]} to your shopping cart.')
        return redirect(url_for('singleProductPage', watchId=watchId))
    if 0 <= watchId < len(watches):
        return render_template('SingleWatch.html', watch=watches[watchId], number=watchId, form=form)
    else:
        return "Watch not found", 404

if __name__ == '__main__':
    app.run(debug=True)

