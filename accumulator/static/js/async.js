window.onload = function(){
  var http = new XMLHttpRequest();

  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      console.log(http.response);
    }
  }

  http.open('GET', 'json/daily_match_dates.json', true);
  http.send();
}
