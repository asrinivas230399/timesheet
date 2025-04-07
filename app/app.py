```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Add Page</title>
    <style>
        .error { color: red; }
        .required::after { content: "*"; color: red; }
    </style>
</head>
<body>
    <h1>Add New Customer</h1>
    <form id="customerForm">
        <div>
            <label for="customerName" class="required">Customer Name</label>
            <input type="text" id="customerName" name="customerName" required>
        </div>
        <div>
            <label for="description">Description</label>
            <textarea id="description" name="description"></textarea>
        </div>
        <div>
            <label for="image">Image/Logo (optional)</label>
            <input type="file" id="image" name="image" accept="image/*">
        </div>
        <div>
            <button type="submit">Add Customer</button>
            <button type="button" onclick="cancel()">Cancel</button>
        </div>
        <div id="message"></div>
    </form>

    <script>
        document.getElementById('customerForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const customerName = document.getElementById('customerName').value.trim();
            const messageDiv = document.getElementById('message');
            if (!customerName) {
                messageDiv.textContent = 'Error: Customer Name is required.';
                messageDiv.className = 'error';
            } else {
                messageDiv.textContent = 'Customer successfully added!';
                messageDiv.className = '';
                this.reset();
            }
        });

        function cancel() {
            document.getElementById('customerForm').reset();
            document.getElementById('message').textContent = '';
        }
    </script>
</body>
</html>
```