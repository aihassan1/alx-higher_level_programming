url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.getJSON(url, (data) => {
  $.each(data.results, function (index, film) {
    $('ul#list_movies').append('<li>' + film.title + '</li>');
  });
});
