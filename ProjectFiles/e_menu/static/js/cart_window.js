function toggleCartVisibility() {
  var cartPreview = document.getElementById("cart-preview");
  if (cartPreview.style.display === "block") {
    cartPreview.style.display = "none";
  } else {
    cartPreview.style.display = "block";
    fetchSessionAndUpdateCartPreview(); // Fetch session data and update cart preview when the cart is shown
  }
}

// Function to fetch session data and update cart preview
function fetchSessionAndUpdateCartPreview() {
  fetch("/customer/get_cart_items")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      updateCartPreview(data.items);
    })
    .catch((error) => {
      console.error("Error fetching session data:", error);
    });
}

// Function to update cart preview with session data
function updateCartPreview(items) {
  const cartItemsContainer = document.getElementById("cart-items-container");
  cartItemsContainer.innerHTML = ""; // Clear existing cart items

  items.forEach((item) => {
    const cartItemDiv = document.createElement("div");
    cartItemDiv.classList.add("cart-item");

    const img = document.createElement("img");
    img.src = `/static/img/menuItems/${item.id}.png`;
    img.alt = item.name;
    img.width = 100;
    img.height = 100;

    const itemDetailsDiv = document.createElement("div");
    itemDetailsDiv.classList.add("item-details");

    const itemNameSpan = document.createElement("span");
    itemNameSpan.classList.add("item-name");
    itemNameSpan.textContent = item.name;

    const itemPriceSpan = document.createElement("span");
    itemPriceSpan.classList.add("item-price");
    itemPriceSpan.textContent = `$${item.price.toFixed(2)}`; // Format price as currency

    const itemQuantitySpan = document.createElement("span");
    itemQuantitySpan.classList.add("item-quantity");
    itemQuantitySpan.textContent = `Quantity: ${item.quantity}`;

    itemDetailsDiv.appendChild(itemNameSpan);
    itemDetailsDiv.appendChild(itemPriceSpan);
    itemDetailsDiv.appendChild(itemQuantitySpan); // Append quantity to item details

    cartItemDiv.appendChild(img);
    cartItemDiv.appendChild(itemDetailsDiv);

    cartItemsContainer.appendChild(cartItemDiv);
  });
}
window.onload = fetchSessionAndUpdateCartPreview;