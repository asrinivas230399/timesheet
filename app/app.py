```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Edit Page</title>
    <style>
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <h1>Edit Customer Details</h1>
    <form id="customerEditForm">
        <label for="customerName">Customer Name (required):</label>
        <input type="text" id="customerName" name="customerName" required>
        <br>
        <label for="description">Description (optional):</label>
        <textarea id="description" name="description"></textarea>
        <br>
        <label for="image">Image (optional):</label>
        <input type="file" id="image" name="image" accept="image/*">
        <br>
        <button type="submit">Save</button>
    </form>
    <div id="message"></div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('customerEditForm');
            const messageDiv = document.getElementById('message');

            // Mock function to get current customer details
            function getCustomerDetails() {
                return {
                    customerName: 'John Doe',
                    description: 'Regular customer',
                    image: null
                };
            }

            // Mock function to update customer details in the database
            function updateCustomerDetails(details) {
                return new Promise((resolve, reject) => {
                    // Simulate a successful update
                    setTimeout(() => resolve('Customer details updated successfully'), 1000);
                });
            }

            // Load current customer details
            const currentDetails = getCustomerDetails();
            document.getElementById('customerName').value = currentDetails.customerName;
            document.getElementById('description').value = currentDetails.description;

            form.addEventListener('submit', function(event) {
                event.preventDefault();
                const customerName = document.getElementById('customerName').value.trim();
                const description = document.getElementById('description').value.trim();
                const image = document.getElementById('image').files[0];

                if (!customerName) {
                    messageDiv.textContent = 'Customer Name is required.';
                    messageDiv.className = 'error';
                    return;
                }

                const customerDetails = { customerName, description, image };
                updateCustomerDetails(customerDetails)
                    .then(successMessage => {
                        messageDiv.textContent = successMessage;
                        messageDiv.className = 'success';
                    })
                    .catch(errorMessage => {
                        messageDiv.textContent = errorMessage;
                        messageDiv.className = 'error';
                    });
            });
        });
    </script>
</body>
</html>
```