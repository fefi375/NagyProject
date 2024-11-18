window.onload = function() {
    if (localStorage.getItem('loggedOut') === 'true') {
        const popup = document.getElementById('popup');
        popup.style.display = 'flex';

        localStorage.removeItem('loggedOut');

        setTimeout(function() {
            popup.style.display = 'none';
        }, 3000);
    }
};