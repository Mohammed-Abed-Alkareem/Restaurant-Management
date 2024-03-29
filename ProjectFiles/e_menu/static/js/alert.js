document.addEventListener('DOMContentLoaded', function () {
    var alertElement = document.getElementById('myAlert');
    var inputFields = document.querySelectorAll('input');

    // Function to hide the alert
    function hideAlert() {
        alertElement.classList.add('d-none');
    }

    // Add event listener to input fields
    inputFields.forEach(function (input) {
        input.addEventListener('input', hideAlert);
    });
});