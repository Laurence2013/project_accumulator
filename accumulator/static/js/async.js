window.onload = function(){
  var http = new XMLHttpRequest();

  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      var dates = JSON.parse(http.responseText);
      var results = document.getElementById('results');
      var mainHtml = '';
      console.log(http.responseText)
      mainHtml += '<button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">View all game dates<span class="caret"></span></button>';
      mainHtml += '<ul class="dropdown-menu" role="menu">';
      for (i = 0; i < dates.length; i++){
        mainHtml += '<li><a href='+ i +'>' + dates[i]['fields'].dates_of_games + '</a></li>';
      }
      mainHtml += '</ul>';
      results.innerHTML = mainHtml;
    }
  }
  http.open("GET", "daily_match_dates", true);
  http.setRequestHeader('Contet-type', 'application/json', true);
  http.send();
  results.innerHTML = 'requesting ...';
}
