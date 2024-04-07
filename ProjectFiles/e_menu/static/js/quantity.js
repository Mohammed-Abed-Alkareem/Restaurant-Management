document.addEventListener("DOMContentLoaded", function () {
  // Select the increment and decrement buttons
  const incrementButton = document.querySelector(".increment");
  const decrementButton = document.querySelector(".decrement");
  const quantityInput = document.querySelector(".quantity-input");
  const priceDisplay = document.querySelector(".price-display"); // Select the price display element
  const dishPrice = 5; // Assume each dish costs 5 units of currency

  // Reset the price on referesh
  quantityInput.value = 1;

  function updatePrice() {
    const totalPrice = parseInt(quantityInput.value, 10) * dishPrice;
    priceDisplay.textContent = `₪ ${totalPrice}`;
  }
  // Increment the value
  incrementButton.addEventListener("click", function () {
    if (parseInt(quantityInput.value, 10) >= 15) {
      // Prevent going over the maximum limit
      quantityInput.value = 15;
    } else {
      quantityInput.value = parseInt(quantityInput.value, 10) + 1;
    }
    updatePrice();
  });

  // Decrement the value
  decrementButton.addEventListener("click", function () {
    if (parseInt(quantityInput.value, 10) > 1) {
      quantityInput.value = parseInt(quantityInput.value, 10) - 1;
      updatePrice();
    }
  });
});
