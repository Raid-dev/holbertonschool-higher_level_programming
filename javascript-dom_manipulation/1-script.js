document.addEventListener("DOMContentLoaded", function() { 

    const redHeaderElement = document.querySelector('#red_header');
    const headerElement = document.querySelector('header');
        
    redHeaderElement.addEventListener('click', function() {        
        headerElement.style.color = '#FF0000';
    });
});