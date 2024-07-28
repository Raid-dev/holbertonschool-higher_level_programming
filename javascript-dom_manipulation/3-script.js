document.addEventListener("DOMContentLoaded", function() { 

    const toggleHeader = document.querySelector('#toggle_header');
    const header = document.querySelector('header');
        
    toggleHeader.addEventListener('click', function() {        
        if (header.className =='red') {
            header.className ='green';
        } else {
            header.className ='red';
        }
    });
});