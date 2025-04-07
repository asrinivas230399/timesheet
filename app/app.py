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
    <form id="customerForm">
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
            const form = document.getElementById('customerForm');
            const messageDiv = document.getElementById('message');

            form.addEventListener('submit', function(event) {
                event.preventDefault();
                const customerName = form.customerName.value.trim();

                if (!customerName) {
                    messageDiv.textContent = 'Customer Name is required.';
                    messageDiv.className = 'error';
                    return;
                }

                const formData = new FormData(form);
                fetch('/api/updateCustomer', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        messageDiv.textContent = 'Customer details updated successfully.';
                        messageDiv.className = 'success';
                    } else {
                        messageDiv.textContent = 'Error updating customer details.';
                        messageDiv.className = 'error';
                    }
                })
                .catch(() => {
                    messageDiv.textContent = 'Error updating customer details.';
                    messageDiv.className = 'error';
                });
            });

            // Fetch current customer details and populate the form
            fetch('/api/getCustomerDetails')
                .then(response => response.json())
                .then(data => {
                    form.customerName.value = data.customerName || '';
                    form.description.value = data.description || '';
                    // Assume image handling is done separately
                });
        });
    </script>
</body>
</html>
```