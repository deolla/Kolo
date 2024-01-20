document.addEventListener('DOMContentLoaded', function () {
    // Check if biometric checkbox is supported
    const biometricCheckbox = document.getElementById('biometric');

    if (biometricCheckbox) {
        // Simulate biometric authentication (replace with actual implementation)
        biometricCheckbox.addEventListener('change', function () {
            if (this.checked) {
                alert('Biometric authentication enabled.');
                // You can add additional logic here for handling biometric authentication
            }
        });
    }
});
