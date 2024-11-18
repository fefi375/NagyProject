function logout(event) {
    event.preventDefault();

    localStorage.setItem('loggedOut', 'true');

    window.location.href = "/";
}