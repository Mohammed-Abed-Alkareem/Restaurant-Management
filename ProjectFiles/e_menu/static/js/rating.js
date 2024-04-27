document.addEventListener('DOMContentLoaded', function() {
  const starsContainers = document.querySelectorAll('.stars');

  starsContainers.forEach(function(starsContainer) {
    const stars = starsContainer.querySelectorAll('.star');

    stars.forEach(function(star) {
      star.addEventListener('click', function() {
        const rating = parseInt(this.getAttribute('data-rating'));
        updateRating(starsContainer, rating);
      });

      star.addEventListener('mouseover', function() {
        const hoverRating = parseInt(this.getAttribute('data-rating'));
        highlightStars(starsContainer, hoverRating);
      });

      star.addEventListener('mouseout', function() {
        const currentRating = parseInt(starsContainer.querySelector('input[name="rating"]').value);
        highlightStars(starsContainer, currentRating);
      });
    });
  });

  function updateRating(starsContainer, rating) {
    highlightStars(starsContainer, rating);

    // Update hidden input field with the rating
    const hiddenField = starsContainer.querySelector('input[name="rating"]');
    hiddenField.value = rating;
  }

  function highlightStars(starsContainer, rating) {
    const stars = starsContainer.querySelectorAll('.star');

    stars.forEach(function(star) {
      const starRating = parseInt(star.getAttribute('data-rating'));
      if (starRating <= rating) {
        star.style.color = '#ffcc00';
      } else {
        star.style.color = '#ccc';
      }
    });
  }
});
