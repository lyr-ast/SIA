let offset = 0;  // Initial offset
const limit = 25;  // Number of products to fetch at a time
let loading = false;  // Prevent multiple fetches at the same time
let allProductsLoaded = false;  // Flag to stop fetching if no more products

// Function to fetch products from the Flask API
async function fetchProducts() {
    if (loading || allProductsLoaded) return;  // Prevent fetching if already loading or no more products
    loading = true;

    try {
        const response = await fetch(`/api/products?limit=${limit}&offset=${offset}`);
        const products = await response.json();

        // If fewer products are returned than the limit, assume all products have been loaded
        if (products.length < limit) {
            allProductsLoaded = true;
        }

        renderProductCards(products);

        // Update the offset for the next fetch
        offset += limit;
    } catch (error) {
        console.error('Error fetching products:', error);
    } finally {
        loading = false;  // Reset loading status
    }
}

// Function to create product cards dynamically
function renderProductCards(products) {
    const productGrid = document.getElementById('product-grid');

    products.forEach((product) => {
        // Create product card element
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');

        // Make the entire card clickable
        productCard.addEventListener('click', function() {
            window.location.href = `/product/${product.id}`;  // Redirect to the product details page
        });

        // Create image element
        const productImage = document.createElement('img');
        productImage.src = product.image_url;  // Using image_url as defined in the model
        productImage.alt = product.product_name;  // Using product_name for alt text

        // Set a default image if the original image fails to load
        productImage.onerror = function() {
            this.src = '/static/images.png';  // Set your default image path here
        };

        // Create product title
        const productTitle = document.createElement('h3');
        productTitle.textContent = product.product_name;  // Using product_name

        // Create price information elements
        const productInfo = document.createElement('div');

        // Show renting info if available
        if (product.rent_price) {
            const rentInfo = document.createElement('p');
            rentInfo.textContent = `Renting available at ₹${product.rent_price} for ${product.rent_duration} days`;
            rentInfo.classList.add('available');  // Add green color
            productInfo.appendChild(rentInfo);
        }

        // Show buying info if available
        if (product.sell_price) {
            const buyInfo = document.createElement('p');
            buyInfo.textContent = `Available to buy at ₹${product.sell_price}`;  // Using sell_price
            buyInfo.classList.add('available');  // Add green color
            productInfo.appendChild(buyInfo);
        }

        // Append elements to product card
        productCard.appendChild(productImage);
        productCard.appendChild(productTitle);
        productCard.appendChild(productInfo);  // Append only the price info

        // Append product card to the grid
        productGrid.appendChild(productCard);
    });
}

// Infinite scroll listener
window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;

    if (scrollTop + windowHeight >= documentHeight - 100 && !loading && !allProductsLoaded) {
        fetchProducts();  // Fetch more products when near bottom of the page
    }
});

// Fetch initial set of products when the page loads
document.addEventListener('DOMContentLoaded', fetchProducts);

// Script to toggle the dropdown on click
document.querySelector('.dropbtn').addEventListener('click', function() {
    const dropdownContent = this.nextElementSibling;
    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
});

// Close dropdown if clicked outside
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        const dropdowns = document.getElementsByClassName('dropdown-content');
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.style.display === 'block') {
                openDropdown.style.display = 'none';
            }
        }
    }
};
