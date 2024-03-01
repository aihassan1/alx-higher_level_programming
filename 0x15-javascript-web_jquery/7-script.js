const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.getJSON(url, (data) => {
  const char_name = data.name;
  $('#character').html(char_name);
});
