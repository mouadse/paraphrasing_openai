const darkModeToggle = document.getElementById('dark-mode-toggle');
const body = document.querySelector('body');

darkModeToggle.addEventListener('change', function () {
    body.classList.toggle('dark-mode');
});
