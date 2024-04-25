document.addEventListener('DOMContentLoaded', function() {
  const starsContainers = document.querySelectorAll('.stars');

  starsContainers.forEach(function(starsContainer) {
    const stars = starsContainer.querySelectorAll('.star');
    let rating = 0;

    stars.forEach(function(star) {
      star.addEventListener('click', function() {
        rating = parseInt(this.getAttribute('data-rating'));
        updateRating(starsContainer, rating);
      });

      star.addEventListener('mouseover', function() {
        const hoverRating = parseInt(this.getAttribute('data-rating'));
        highlightStars(starsContainer, hoverRating);
      });

      star.addEventListener('mouseout', function() {
        highlightStars(starsContainer, rating);
      });
    });
  });

  function updateRating(starsContainer, rating) {
    highlightStars(starsContainer, rating);

    // Send the rating data to the server using AJAX or form submission
    const ratingId = starsContainer.getAttribute('data-rating-id');
    console.log(`Rating ${ratingId}: ${rating}`);
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