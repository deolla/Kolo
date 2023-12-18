document.addEventListener('DOMContentLoaded', function() {
    // Get the splash container
    const splashContainer = document.querySelector('.splash-container');

    // Create a new animation
    splashContainer.style.opacity = 0;

    splashContainer.animate([
        { opacity: 0, transform: 'translateY(-20px)' },
        { opacity: 1, transform: 'translateY(0px)' }
    ], {
        duration: 1000,
        easing: 'cubic-bezier(0.23, 1, 0.32, 1)',
        fill: 'forwards'
});

// Redirect after animation

setTimeout(function() {
    window.location.href = BASE_URL; // Redirect to login page
}, 5000);
});