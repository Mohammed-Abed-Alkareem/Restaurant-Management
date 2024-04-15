const stars = document.querySelectorAll(".star");
let rating = 0;

stars.forEach((star) => {
  star.addEventListener("click", () => {
    rating = parseInt(star.getAttribute("data-rating"));
    updateRating();
  });
});

function updateRating() {
  stars.forEach((star) => {
    const starRating = parseInt(star.getAttribute("data-rating"));
    if (starRating >= rating) {
      star.style.color = "#ffcc00";
    } else {
      star.style.color = "#ccc";
    }
  });
}
