$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let i = 0; i < data.results.length; i++) {
    const item = data.results[i].title;
    $('UL#list_movies').append('<li>' + item + '</li>');
  }
});
