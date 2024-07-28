document.addEventListener('DOMContentLoaded', () => {
    const updateHeader = document.getElementById('update_header');
    const header = document.querySelector('header');
  
    updateHeader.addEventListener('click', () => {
      header.textContent = 'New Header!!!';
    });
  });