from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

watches = [
    { "name": "Rolex Datejust 41", "price": "12.000", "description": "Iconic and timeless, Rolex watches are renowned for their precision, durability, and luxury.", "image": "Rolex_Datejust_41.jpg" },
    { "name": "Audemars Piguet Royal Oak", "price": "32.000", "description": "Bold and innovative, AP blends cutting-edge design with traditional Swiss watchmaking.", "image": "Audemars_Piguet_Royal_Oak.jpg" },
    { "name": "Patek Philippe Nautilus", "price": "75.000", "description": "The pinnacle of horology, Patek Philippe creates elegant, highly intricate timepieces.", "image": "Patek_Philippe_Nautilus.jpg" },
]

@app.route('/')
def galleryPage():
    return render_template('index.html', watches=watches)

@app.route('/watch/<int:watchId>', methods=['GET', 'POST'])
def singleProductPage(watchId):
    if request.method == 'POST':
        quantity = request.form.get('quantity', 1)  # Default quantity is 1
        flash(f'You have added {quantity} {watches[watchId]["name"]} to your cart!', 'success')
        return redirect(url_for('singleProductPage', watchId=watchId))

    return render_template('SingleWatch.html', watch=watches[watchId])

if __name__ == '__main__':
    app.run(debug=True)
