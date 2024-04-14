function toggleCartVisibility() {
  var cartPreview = document.getElementById("cart-preview");
  if (cartPreview.style.display === "block") {
    cartPreview.style.display = "none";
  } else {
    cartPreview.style.display = "block"; // Shows the cart in the content area
  }
}
