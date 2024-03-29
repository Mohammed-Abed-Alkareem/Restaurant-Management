document.addEventListener("DOMContentLoaded", function () {
    // Select the increment and decrement buttons
    const incrementButton = document.querySelector(".increment");
    const decrementButton = document.querySelector(".decrement");
    const quantityInput = document.querySelector(".quantity-input");

    // Increment the value
    incrementButton.addEventListener("click", function () {
        if (parseInt(quantityInput.value, 10) > 14) {
            quantityInput.value = 15; // Set to max limit if exceeded
        }
        quantityInput.value = parseInt(quantityInput.value, 10) + 1;
    });

    // Decrement the value
    decrementButton.addEventListener("click", function () {
        if (parseInt(quantityInput.value, 10) > 1) {
            quantityInput.value = parseInt(quantityInput.value, 10) - 1;
        }
    });
});