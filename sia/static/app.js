// Function to fetch products from the Flask API
async function fetchProducts() {
    console.log("fetchProducts called")
    try {
        const response = await fetch('/api/products');
        const products = await response.json();
        renderProductCards(products);
    } catch (error) {
        console.error('Error fetching products:', error);
    }
}

// Function to create product cards dynamically
function renderProductCards(products) {
    const productGrid = document.getElementById('product-grid');
    productGrid.innerHTML = ''; // Clear existing products

    products.forEach((product) => {
        // Create product card element
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');

        // Make the entire card clickable
        productCard.addEventListener('click', function() {
            window.location.href = `/product/${product.id}`; // Redirect to the product details page
        });

        // Create image element
        const productImage = document.createElement('img');
        productImage.src = product.imageUrl;
        productImage.alt = product.name;
        
        // Set a default image if the original image fails to load
        productImage.onerror = function() {
            this.src = '/static/images.png'; // Set your default image path here
        };

        // Create product title
        const productTitle = document.createElement('h3');
        productTitle.textContent = product.name;

        // Create price information elements
        const productInfo = document.createElement('div');

        // Show renting info if available
        if (product.rentPrice) {
            const rentInfo = document.createElement('p');
            rentInfo.textContent = `Renting available at ₹${product.rentPrice} for ${product.rentDuration} days`;
            rentInfo.classList.add('available'); // Add green color
            productInfo.appendChild(rentInfo);

            const buyNotAvailable = document.createElement('p');
            buyNotAvailable.textContent = 'Buying not available';
            buyNotAvailable.classList.add('not-available'); // Add gray color
            productInfo.appendChild(buyNotAvailable);
        } else if (product.buyPrice) {
            const buyInfo = document.createElement('p');
            buyInfo.textContent = `Available to buy at ₹${product.buyPrice}`;
            buyInfo.classList.add('available'); // Add green color
            productInfo.appendChild(buyInfo);

            const rentNotAvailable = document.createElement('p');
            rentNotAvailable.textContent = 'Renting not available';
            rentNotAvailable.classList.add('not-available'); // Add gray color
            productInfo.appendChild(rentNotAvailable);
        }

        // Append elements to product card
        productCard.appendChild(productImage);
        productCard.appendChild(productTitle);
        productCard.appendChild(productInfo);

        // Append product card to the grid
        productGrid.appendChild(productCard);
    });
}

// Fetch products when the page loads
document.addEventListener('DOMContentLoaded', fetchProducts);



