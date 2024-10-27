from flask import Flask, render_template, jsonify, request, flash, Blueprint, redirect, url_for

from . import db
from .models import Item 

from flask_login import login_user, login_required, logout_user, current_user

app = Flask(__name__)

#app.secret_key = 'your_super_secret_key_here'

#app.config.from_prefixed_env()
#app.config["SECRET_KEY"]



views = Blueprint('views', __name__)

@views.route('/')    
def home():
    return render_template('index.html')  # Main product listing page


@views.route('/api/products')
def get_products():
    # Get the limit and offset from the request, defaulting to 25 and 0
    limit = int(request.args.get('limit', 25))
    offset = int(request.args.get('offset', 0))
    
    # Slice the product list based on limit and offset
    paginated_products = Item.query.offset(offset).limit(limit).all()
    products = [item.to_dict() for item in paginated_products]


    return jsonify(products)

@views.route('/product/<int:product_id>')
def product_details(product_id):
    product = Item.query.get(product_id)
    if product:
        return render_template('product_details.html', product=product)
    else:
        return render_template("404.html"), 404


@views.route('/addlisting', methods=['GET', 'POST'])
@login_required
def add_listing():
    if request.method == 'POST':
        # Retrieve form data
        product_name = request.form.get('product_name')
        category = request.form.get('category')
        sell_price = request.form.get('sell_price')
        rent_price = request.form.get('rent_price')
        rent_duration = request.form.get('rent_duration')
        description = request.form.get('description')
        image_url = request.form.get('image_url')

        # Validate required fields
        if not product_name or not category:
            flash('Product Name and Category are required.', 'danger')
            return redirect(url_for('views.add_listing'))

        # Validate numeric fields
        try:
            sell_price = float(sell_price) if sell_price else None
            rent_price = float(rent_price) if rent_price else None
            rent_duration = int(rent_duration) if rent_duration else None
            
            # Check for at least one of sell_price or rent_price
            if sell_price is None and rent_price is None:
                flash('Either Sell Price or Rent Price must be provided.', 'danger')
                return redirect(url_for('views.add_listing'))

            # If rent_price is provided, rent_duration must also be provided
            if rent_price is not None and rent_duration is None:
                flash('If Rent Price is provided, Rent Duration must also be included.', 'danger')
                return redirect(url_for('views.add_listing'))

            # Validate numeric values
            if sell_price is not None and sell_price < 0:
                flash('Sell Price must be a non-negative number.', 'danger')
                return redirect(url_for('views.add_listing'))
            if rent_price is not None and rent_price < 0:
                flash('Rent Price must be a non-negative number.', 'danger')
                return redirect(url_for('views.add_listing'))
            if rent_duration is not None and rent_duration < 0:
                flash('Rent Duration must be a non-negative integer.', 'danger')
                return redirect(url_for('views.add_listing'))

        except ValueError:
            flash('Invalid input for Sell Price, Rent Price, or Rent Duration.', 'danger')
            return redirect(url_for('views.add_listing'))

        # Create a new item instance with the logged-in user's ID
        new_item = Item(
            product_name=product_name,
            category=category,
            sell_price=sell_price,
            rent_price=rent_price,
            rent_duration=rent_duration,
            description=description,
            image_url=image_url,
            username=current_user.username  # Link the item to the logged-in user
        )

        # Add to the database
        db.session.add(new_item)
        db.session.commit()

        flash('Item added successfully!', 'success')
        return redirect(url_for('views.home'))
    
    return render_template("addlisting.html")



if __name__ == '__main__':
    app.run(debug=True)
    


