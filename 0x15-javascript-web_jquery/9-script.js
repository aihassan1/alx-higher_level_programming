const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.getJSON(url, (data) => {
  $('#hello').text(data.hello);
});
