// function toggleCartVisibility() {
//     var cartPreview = document.getElementById('cart-preview');
//     if (cartPreview.style.display === 'block') {
//         cartPreview.style.display = 'none';
//     } else {
//         cartPreview.style.display = 'block';
//     }
// }
// function toggleCartVisibility() {
//   const cartPreview = document.getElementById("cart-preview");
//   const contentBlock = document.querySelector("#content"); // Make sure this is your content block's ID or class

//   if (
//     cartPreview.style.display === "none" ||
//     cartPreview.parentElement !== contentBlock
//   ) {
//     contentBlock.appendChild(cartPreview); // Move cart to content block
//     cartPreview.style.display = "block"; // Show cart
//     cartPreview.style.position = "static"; // Ensure it's in normal document flow in content
//   } else {
//     cartPreview.style.display = "none"; // Hide cart
//   }
// }
// function toggleCartVisibility() {
//   const cartPreview = document.getElementById("cart-preview");
//   const contentBlock = document.querySelector("#content"); // Ensure this is the correct selector for your content block

//   if (
//     cartPreview.style.display === "none" ||
//     cartPreview.parentElement !== contentBlock
//   ) {
//     contentBlock.appendChild(cartPreview); // Move cart to content block
//     cartPreview.style.display = "block"; // Show cart
//     cartPreview.style.position = "static"; // Ensure it's in normal document flow in content
//   } else {
//     cartPreview.style.display = "none"; // Hide cart
//   }
// }
function toggleCartVisibility() {
  var cartPreview = document.getElementById("cart-preview");
  if (cartPreview.style.display === "block") {
    cartPreview.style.display = "none";
  } else {
    cartPreview.style.display = "block"; // Shows the cart in the content area
  }
}
