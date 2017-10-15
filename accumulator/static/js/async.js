window.onload = function(){
  var http = new XMLHttpRequest();

  http.onreadystatechange = function(){
    console.log(http.status)
    if(http.readyState == 4 && http.status == 200){
      console.log('It is happening here ', http.response);
    } else{
      console.log('Nothing is happening here ', http.readyState)
    }
  }
  console.dir(open)
  http.open("GET", "daily_match_dates", true);
  console.log(http.open)
  http.send();
}

// var geturl = window.location
// console.log(geturl)
