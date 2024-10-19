from flask import Flask, render_template, jsonify, request, flash, Blueprint

app = Flask(__name__)

#app.secret_key = 'your_super_secret_key_here'

#app.config.from_prefixed_env()
#app.config["SECRET_KEY"]

# Example product data (you can replace this with database data)
products = [
    {"id": 1, "name": "Football", "buyPrice": 19.99, "rentPrice": None, "rentDuration": None, "imageUrl": "/static/product1.jpg", "description": "A high-quality football for outdoor games."},
    {"id": 2, "name": "Badminton Racket", "buyPrice": None, "rentPrice": 14.99, "rentDuration": 1, "imageUrl": "/static/product2.jpg", "description": "Lightweight badminton racket for a competitive edge."},
    {"id": 3, "name": "Tennis Ball", "buyPrice": 39.99, "rentPrice": None, "rentDuration": None, "imageUrl": "/static/product3.jpg", "description": "Durable tennis balls for long-lasting play."},
    {"id": 4, "name": "Yoga Mat", "buyPrice": None, "rentPrice": 29.99, "rentDuration": 3, "imageUrl": "/static/product4.jpg", "description": "Eco-friendly yoga mat for comfortable practice."},
    {"id": 5, "name": "Smartphone", "buyPrice": 59.99, "rentPrice": None, "rentDuration": None, "imageUrl": "/static/product5.jpg", "description": "Latest smartphone with high-resolution camera."},
    {"id": 6, "name": "Cooking Pot", "buyPrice": None, "rentPrice": 34.99, "rentDuration": 2, "imageUrl": "/static/product6.jpg", "description": "Stainless steel cooking pot for all your culinary needs."},
    {"id": 7, "name": "Badminton Shuttlecock", "buyPrice": 79.99, "rentPrice": 19.99, "rentDuration": 5, "imageUrl": "/static/product7.jpg", "description": "High-speed shuttlecocks for professional games."},
    {"id": 8, "name": "Basketball", "buyPrice": None, "rentPrice": 39.99, "rentDuration": 4, "imageUrl": "/static/product8.jpg", "description": "Official size basketball for outdoor courts."},
    {"id": 9, "name": "Skateboard", "buyPrice": 99.99, "rentPrice": None, "rentDuration": None, "imageUrl": "/static/product9.jpg", "description": "Durable skateboard for tricks and stunts."},
    {"id": 10, "name": "Cycling Helmet", "buyPrice": None, "rentPrice": 44.99, "rentDuration": 1, "imageUrl": "/static/product10.jpg", "description": "Lightweight helmet for safe cycling."},
    {"id": 11, "name": "Camping Tent", "buyPrice": 119.99, "rentPrice": 24.99, "rentDuration": 3, "imageUrl": "/static/product11.jpg", "description": "Spacious camping tent for outdoor adventures."},
    {"id": 12, "name": "Fishing Rod", "buyPrice": None, "rentPrice": 49.99, "rentDuration": 2, "imageUrl": "/static/product12.jpg", "description": "Durable fishing rod for a successful catch."},
    {"id": 13, "name": "Guitar", "buyPrice": 139.99, "rentPrice": None, "rentDuration": None, "imageUrl": "/static/product13.jpg", "description": "Acoustic guitar with a rich sound."},
    {"id": 14, "name": "Soccer Cleats", "buyPrice": None, "rentPrice": 54.99, "rentDuration": 1, "imageUrl": "/static/product14.jpg", "description": "Comfortable cleats for soccer players."},
    {"id": 15, "name": "Bicycle", "buyPrice": 159.99, "rentPrice": None, "rentDuration": None, "imageUrl": "/static/product15.jpg", "description": "High-performance bicycle for city rides."},
    {"id": 16, "name": "Weights Set", "buyPrice": None, "rentPrice": 59.99, "rentDuration": 3, "imageUrl": "/static/product16.jpg", "description": "Adjustable weights for home workouts."},
    {"id": 17, "name": "Table Tennis Paddle", "buyPrice": 179.99, "rentPrice": 39.99, "rentDuration": 5, "imageUrl": "/static/product17.jpg", "description": "Professional paddle for table tennis enthusiasts."},
    {"id": 18, "name": "Fitness Tracker", "buyPrice": None, "rentPrice": 64.99, "rentDuration": 14, "imageUrl": "/static/product18.jpg", "description": "Smart fitness tracker to monitor your activities."},
    {"id": 19, "name": "Swim Goggles", "buyPrice": 199.99, "rentPrice": None, "rentDuration": None, "imageUrl": "/static/product19.jpg", "description": "Anti-fog swim goggles for clear visibility."},
    {"id": 20, "name": "Protein Powder", "buyPrice": None, "rentPrice": 69.99, "rentDuration": 30, "imageUrl": "/static/product20.jpg", "description": "Nutritional protein powder for muscle building."},
]


views = Blueprint('views', __name__)

@views.route('/')    
def home():
    return render_template('index.html')  # Main product listing page


@views.route('/api/products')
def get_products():
    return jsonify(products)  # Send the products data as JSON

@views.route('/product/<int:product_id>')
def product_details(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return render_template('product_details.html', product=product)
    else:
        return "Product not found", 404

if __name__ == '__main__':
    app.run(debug=True)


