document.addEventListener('DOMContentLoaded', () => {
    const characterElement = document.getElementById('character');
    const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        characterElement.textContent = data.name;
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
      });
  });
  