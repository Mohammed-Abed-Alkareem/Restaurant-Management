// static/script.js

let confirmationCallback; // Define a global variable to hold the callback function

function showModal() {
    document.getElementById('confirmationModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('confirmationModal').style.display = 'none';
}

function confirmAction() {
    closeModal(); // Close the modal first
    if (confirmationCallback) {
        confirmationCallback(); // Trigger the callback function if it's set
    } else {
        console.error("No callback function set for confirmation.");
    }
}

function noAction() {
    closeModal(); // Close the modal
    window.location.href = "/employee/dashboard";
}

// Set the callback function for form submission
function setConfirmationCallback(callback) {
    confirmationCallback = callback;
}

// Close the modal if the user clicks anywhere outside of it
window.onclick = function(event) {
    var modal = document.getElementById('confirmationModal');
    if (event.target == modal) {
        closeModal();
    }
}
