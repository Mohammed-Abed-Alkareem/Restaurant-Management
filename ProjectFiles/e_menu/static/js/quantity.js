document.addEventListener("DOMContentLoaded", function () {
  // Select the increment and decrement buttons
  const incrementButton = document.querySelector(".increment");
  const decrementButton = document.querySelector(".decrement");
  const quantityInput = document.querySelector(".quantity-input");
  const priceDisplay = document.querySelector(".price-display");

  // Extract the base price of one meal quantity
  let basePrice = extractPrice(priceDisplay.textContent);

  // Reset the price on referesh
  quantityInput.value = 1;
  updatePrice();

  function extractPrice(priceString) {
    // Extract only the numeric part
    const numericPart = priceString.match(/\d+(\.\d+)?/);

    // If a numeric value is found, parse it as a float and return it
    if (numericPart) {
      return parseFloat(numericPart[0]);
    }

    return null;
  }

  function updatePrice() {
    const totalPrice = parseInt(quantityInput.value, 10) * basePrice;
    priceDisplay.textContent = `₪ ${totalPrice}`;
  }

  incrementButton.addEventListener("click", function () {
    // Prevent going over the maximum limit
    if (parseInt(quantityInput.value, 10) >= 15) {
      quantityInput.value = 15;
    } else {
      quantityInput.value = parseInt(quantityInput.value, 10) + 1;
    }
    updatePrice();
  });

  decrementButton.addEventListener("click", function () {
    if (parseInt(quantityInput.value, 10) > 1) {
      quantityInput.value = parseInt(quantityInput.value, 10) - 1;
      updatePrice();
    }
  });
});
