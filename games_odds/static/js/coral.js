function CreateANewRequest(){}

CreateANewRequest.prototype = {
  constructor: CreateANewRequest,
  coralGetMatchDayDates: function(){
    var http = new XMLHttpRequest();
    http.onreadystatechange = function(){
      if(http.readyState == 4 && http.status == 200){
        var matchday_dates = JSON.parse(http.responseText);
        var matchday_length = Object.keys(matchday_dates).length;

        var mainHtml = '';
        mainHtml += '<h2>This is Coral main page</h2>';
        mainHtml += '<table class="table table-bordered">';
        mainHtml += '<thead>';
        mainHtml += '<tr>';
        mainHtml += '<th>Date</th>';
        mainHtml += '<th>Click button to view</th>';
        mainHtml += '</tr>';
        mainHtml += '</thead>'
        mainHtml += '<tbody>';
        for(var i = 0; i < matchday_length; i++){
          mainHtml += '<tr>';
          mainHtml += '<td>'+ matchday_dates[i][0] +'</td>';
          mainHtml += '<td> Click here </td>';
          mainHtml += '</tr>';

        }
        mainHtml += '</tbody>';
        mainHtml += '</table>';
        game_dates.innerHTML = mainHtml;
      }
    }
    http.open("GET", "coral_matchday_dates", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    game_dates.innerHTML = '<div class="col-sm-12 text-center">Requesting ...</div>';
  },
}

window.onload = function(){
  getGames = new CreateANewRequest();
  if (document.getElementById('game_dates')){
    getGames.coralGetMatchDayDates();
  }
}
