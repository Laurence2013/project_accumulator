window.onload = function(){
  var http = new XMLHttpRequest();

  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      var dates = JSON.parse(http.responseText);
      console.log(dates);
      console.log(dates[0]['fields']);
      console.log(dates[1]);
      var results = document.getElementById('results');
      results.innerHTML = dates[0]['fields'].dates_of_games;
    }
  }
  http.open("GET", "daily_match_dates", true);
  http.setRequestHeader('Contet-type', 'application/json', true);
  http.send();
  results.innerHTML = 'requesting ...';
}
