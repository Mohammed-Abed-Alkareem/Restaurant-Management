// Function to fetch cart items from server and update HTML
function fetchCartItems() {
  // make an http request to the get_cart_items url
  fetch("/customer/get_cart_items")
    // handle the promise returned by the fetch function
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    // handle the promise returned from the response.json
    .then((data) => {
      updateCartItems(data.items);
    })
    .catch((error) => {
      console.error("Error fetching cart items:", error);
    });
}

function updatePrice() {
  const totalPrice = parseInt(quantityInput.value, 10) * dishPrice;
  priceDisplay.textContent = `₪ ${totalPrice}`;
}
// Function to update cart items in HTML
function updateCartItems(items) {
  const cartItemsContainer = document.getElementById("cart-items-container");
  cartItemsContainer.innerHTML = ""; // Clear existing cart items

  let totalPrice = 0;
  items.forEach((item) => {
    const mealBox = document.createElement("div");
    mealBox.classList.add("meal-box");

    const leftSide = document.createElement("div");
    leftSide.classList.add("left-side");

    const mealImage = document.createElement("img");
    mealImage.classList.add("meal-image");
    mealImage.src = `/static/img/menuItems/${item.id}.png`;
    mealImage.alt = item.name;
    mealImage.width = 100;
    mealImage.height = 100;

    const mealName = document.createElement("div");
    mealName.classList.add("meal-name");
    mealName.textContent = item.name;

    const rightSide = document.createElement("div");
    rightSide.classList.add("right-side");

    const mealDescription = document.createElement("div");
    mealDescription.classList.add("meal-description");
    mealDescription.textContent = item.description;

    const quantitySelector = document.createElement("div");
    quantitySelector.classList.add("quantity-selector");

    const quantityInputWrapper = document.createElement("div");
    quantityInputWrapper.classList.add("quantity-input-wrapper");

    const mealPrice = document.createElement("div");
    mealPrice.classList.add("meal-price");
    mealPrice.textContent = `₪ ${item.price}`;

    totalPrice += item.price;

    const decrementButton = document.createElement("button");
    decrementButton.classList.add("decrement");
    decrementButton.type = "button";
    decrementButton.textContent = "-";
    decrementButton.addEventListener("click", function () {
      const currentQuantity = parseInt(quantityInput.value);
      if (currentQuantity > 1) {
        quantityInput.value = currentQuantity - 1;
        updateQuantity(item.id, currentQuantity - 1);
      }
    });

    const quantityInput = document.createElement("input");
    quantityInput.classList.add("quantity-input");
    quantityInput.type = "number";
    quantityInput.name = "quantity";
    quantityInput.value = item.quantity;
    quantityInput.min = "1";
    quantityInput.addEventListener("change", function () {
      updateQuantity(item.id, parseInt(this.value));
    });

    const incrementButton = document.createElement("button");
    incrementButton.classList.add("increment");
    incrementButton.type = "button";
    incrementButton.textContent = "+";
    incrementButton.addEventListener("click", function () {
      const currentQuantity = parseInt(quantityInput.value);
      updateQuantity(item.id, currentQuantity >= 15 ? 15 : currentQuantity + 1);
    });

    quantityInputWrapper.appendChild(decrementButton);
    quantityInputWrapper.appendChild(quantityInput);
    quantityInputWrapper.appendChild(incrementButton);

    quantitySelector.appendChild(quantityInputWrapper);
    quantitySelector.appendChild(mealPrice);

    leftSide.appendChild(mealImage);
    leftSide.appendChild(mealName);

    rightSide.appendChild(mealDescription);
    rightSide.appendChild(quantitySelector);

    const deleteButton = document.createElement("button");
    deleteButton.classList.add("delete-button");
    deleteButton.addEventListener("click", function () {
      deleteItem(item.id);
    });

    const deleteIcon = document.createElement("img");
    deleteIcon.src = "/static/img/delete_button.png";
    deleteIcon.alt = "Delete";
    deleteIcon.width = 20;
    deleteIcon.height = 20;

    deleteButton.appendChild(deleteIcon);

    rightSide.appendChild(deleteButton);
    mealBox.appendChild(leftSide);
    mealBox.appendChild(rightSide);

    cartItemsContainer.appendChild(mealBox);
  });
  const totalPriceElement = document.createElement("div");
  totalPriceElement.classList.add("total-price");
  totalPriceElement.textContent = `Total Price: ₪ ${totalPrice}`;

  cartItemsContainer.appendChild(totalPriceElement);
}

// Function to update quantity of an item
function updateQuantity(itemId, newQuantity) {
  fetch("/customer/update_quantity", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      itemId: itemId,
      newQuantity: newQuantity,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      fetchCartItems(); // Refresh cart items after updating quantity
    })
    .catch((error) => {
      console.error("Error updating quantity:", error);
    });
}

// Function to delete an item from the cart
function deleteItem(itemId) {
  fetch("/customer/delete_item", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      itemId: itemId,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      fetchCartItems(); // Refresh cart items after deleting
    })
    .catch((error) => {
      console.error("Error deleting item:", error);
    });
}

// Call fetchCartItems function when page loads
window.onload = fetchCartItems;
