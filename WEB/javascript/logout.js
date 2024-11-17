function logoutPopup(){
    alert("Kijelentkeztél");

    window.location.href="{{ url_for('news_portal') }}";
}