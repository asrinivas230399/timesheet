document.getElementById('customerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const address = document.getElementById('address').value;

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, phone, address })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert(data.message);
        }
    })
    .catch(error => console.error('Error:', error));
});

function load_tooltips() {
    const tooltips = {
        name: 'Enter the full name of the customer.',
        email: 'Enter a valid email address.',
        phone: 'Enter the phone number with country code.',
        address: 'Enter the complete address of the customer.'
    };

    Object.keys(tooltips).forEach(id => {
        const element = document.getElementById(id);
        element.addEventListener('focus', () => {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.innerText = tooltips[id];
            element.parentElement.appendChild(tooltip);
        });

        element.addEventListener('blur', () => {
            const tooltip = element.parentElement.querySelector('.tooltip');
            if (tooltip) {
                tooltip.remove();
            }
        });
    });
}

load_tooltips();