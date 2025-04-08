document.getElementById('customerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const address = document.getElementById('address').value;

    if (name && email && phone && address) {
        alert('Customer added successfully!');
        // Here you can add code to submit the form data to a server
    } else {
        alert('Please fill out all fields.');
    }
});