// Function to fetch cart items from server and update HTML
function fetchCartItems() {
    fetch('/customer/get_cart_items')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            updateCartItems(data.items);
        })
        .catch(error => {
            console.error('Error fetching cart items:', error);
        });
}

// Function to update cart items in HTML
function updateCartItems(items) {
    const cartItemsContainer = document.getElementById('cart-items-container');
    cartItemsContainer.innerHTML = ''; // Clear existing cart items

    items.forEach(item => {
        const cartItemDiv = document.createElement('div');
        cartItemDiv.classList.add('cart-item');

        const itemName = document.createElement('div');
        itemName.classList.add('item-name');
        itemName.textContent = item.name;

        const quantityInput = document.createElement('input');
        quantityInput.type = 'number';
        quantityInput.classList.add('quantity-input');
        quantityInput.value = item.quantity;
        quantityInput.min = '1';
        quantityInput.addEventListener('change', function() {
            updateQuantity(item.id, parseInt(this.value));
        });

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', function() {
            deleteItem(item.id);
        });

        cartItemDiv.appendChild(itemName);
        cartItemDiv.appendChild(quantityInput);
        cartItemDiv.appendChild(deleteButton);

        cartItemsContainer.appendChild(cartItemDiv);
    });
}

// Function to update quantity of an item
function updateQuantity(itemId, newQuantity) {
    fetch('/customer/update_quantity', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            itemId: itemId,
            newQuantity: newQuantity
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        fetchCartItems(); // Refresh cart items after updating quantity
    })
    .catch(error => {
        console.error('Error updating quantity:', error);
    });
}

// Function to delete an item from the cart
function deleteItem(itemId) {
    fetch('/customer/delete_item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            itemId: itemId
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        fetchCartItems(); // Refresh cart items after deleting
    })
    .catch(error => {
        console.error('Error deleting item:', error);
    });
}

// Call fetchCartItems function when page loads
window.onload = fetchCartItems;
