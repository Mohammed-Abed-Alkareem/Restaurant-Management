document.addEventListener("DOMContentLoaded", function () {
  const starsContainers = document.querySelectorAll(".stars");

  starsContainers.forEach(function (starsContainer) {
    const stars = starsContainer.querySelectorAll(".star");
    const ratingId = starsContainer.getAttribute("data-rating-id");

    stars.forEach(function (star) {
      star.addEventListener("click", function () {
        const rating = parseInt(this.getAttribute("data-rating"));
        updateRating(starsContainer, rating, ratingId);
      });

      star.addEventListener("mouseover", function () {
        const hoverRating = parseInt(this.getAttribute("data-rating"));
        highlightStars(starsContainer, hoverRating);
      });

      star.addEventListener("mouseout", function () {
        const currentRating = parseInt(
          starsContainer.querySelector(`input[name="${ratingId}"]`).value
        );
        highlightStars(starsContainer, currentRating);
      });
    });
  });

  function updateRating(starsContainer, rating, ratingId) {
    highlightStars(starsContainer, rating);

    // Update hidden input field with the rating based on the rating type
    // This is where we send the cusotmer rating to the backend
    const hiddenField = starsContainer.querySelector(
      `input[name=${CSS.escape(ratingId)}]`
    );
    hiddenField.value = rating;
  }

  function highlightStars(starsContainer, rating) {
    const stars = starsContainer.querySelectorAll(".star");

    // We iterate over the each star to check which one to
    // highlight
    stars.forEach(function (star) {
      // We get the rating of each of the five stars at
      // every iteration
      const starRating = parseInt(star.getAttribute("data-rating"));

      // if the value of the current star is less than the rating
      // of the user, then highlight it, else, don't
      if (starRating <= rating) {
        star.style.color = "#ffcc00";
      } else {
        star.style.color = "#ccc";
      }
    });
  }
});