document.addEventListener('DOMContentLoaded', async () => {
    const listMoviesElement = document.getElementById('list_movies');
    const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
  
    try {
      const response = await fetch(apiUrl);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      const movies = data.results;
  
      movies.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listMoviesElement.appendChild(listItem);
      });
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  });
  