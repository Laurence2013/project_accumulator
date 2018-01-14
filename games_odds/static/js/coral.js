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
          mainHtml += '<td><a href="'+ matchday_dates[i][1] +'">Click here</a></td>';
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
  coralGetTodaysMatches: function(){
    var http = new XMLHttpRequest();
    http.onreadystatechange = function(){
      if(http.readyState == 4 && http.status == 200){
        var get_todays_matches = JSON.parse(http.responseText);
        var today_matches_length = Object.keys(get_todays_matches).length;

        var mainHtml = '';
        mainHtml += '<div class="row" id="refresh_padding">';
        mainHtml += '<div class="col-sm-6"></div>';
        mainHtml += '<div class="col-sm-4">';
        mainHtml += '<a href="#" >Click here to refresh</a>';
        mainHtml += '<b><i></i></b>';
        mainHtml += '</div>';
        mainHtml += '<div class="col-sm-2">';
        mainHtml += '<a href="#" >Click here to save into Database</a>';
        mainHtml += '</div>';
        mainHtml += '</div>';
        mainHtml += '<table class="table table-bordered">';
        mainHtml += '<thead>';
        mainHtml += '<tr>';
        mainHtml += '<th>Games</th>';
        mainHtml += '<th>Home</th>';
        mainHtml += '<th>Draw</th>';
        mainHtml += '<th>Away</th>';
        mainHtml += '</tr>';
        mainHtml += '</thead>';
        mainHtml += '<tbody>';
        for(var i = 0; i < today_matches_length; i++){
          mainHtml += '<tr>';
          mainHtml += '<td><i>'+ get_todays_matches[i][0] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][1] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][2] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][3] +'</i></td>';
          mainHtml += '</tr>  ';
        }
        mainHtml += '</tbody>';
        mainHtml += '</table>';
        coral_match_day.innerHTML = mainHtml;
      }
    }
    http.open("GET", "coral_matches_0", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    coral_match_day.innerHTML = '<div class="col-sm-12 text-center">Requesting ...</div>';
  },
  coralGetTomorrowsMatches: function(){
    var http = new XMLHttpRequest();
    http.onreadystatechange = function(){
      if(http.readyState == 4 && http.status == 200){
        var get_todays_matches = JSON.parse(http.responseText);
        var today_matches_length = Object.keys(get_todays_matches).length;

        var mainHtml = '';
        mainHtml += '<div class="row" id="refresh_padding">';
        mainHtml += '<div class="col-sm-6"></div>';
        mainHtml += '<div class="col-sm-4">';
        mainHtml += '<a href="#" >Click here to refresh</a>';
        mainHtml += '<b><i></i></b>';
        mainHtml += '</div>';
        mainHtml += '<div class="col-sm-2">';
        mainHtml += '<a href="#" >Click here to save into Database</a>';
        mainHtml += '</div>';
        mainHtml += '</div>';
        mainHtml += '<table class="table table-bordered">';
        mainHtml += '<thead>';
        mainHtml += '<tr>';
        mainHtml += '<th>Games</th>';
        mainHtml += '<th>Home</th>';
        mainHtml += '<th>Draw</th>';
        mainHtml += '<th>Away</th>';
        mainHtml += '</tr>';
        mainHtml += '</thead>';
        mainHtml += '<tbody>';
        for(var i = 0; i < today_matches_length; i++){
          mainHtml += '<tr>';
          mainHtml += '<td><i>'+ get_todays_matches[i][0] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][1] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][2] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][3] +'</i></td>';
          mainHtml += '</tr>  ';
        }
        mainHtml += '</tbody>';
        mainHtml += '</table>';
        coral_match_day_1.innerHTML = mainHtml;
      }
    }
    http.open("GET", "coral_matches_1", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    coral_match_day_1.innerHTML = '<div class="col-sm-12 text-center">Requesting ...</div>';
  },
  coralGetFutureMatchesA: function(){
    var http = new XMLHttpRequest();
    http.onreadystatechange = function(){
      if(http.readyState == 4 && http.status == 200){
        var get_todays_matches = JSON.parse(http.responseText);
        var today_matches_length = Object.keys(get_todays_matches).length;

        var mainHtml = '';
        mainHtml += '<div class="row" id="refresh_padding">';
        mainHtml += '<div class="col-sm-6"></div>';
        mainHtml += '<div class="col-sm-4">';
        mainHtml += '<a href="#" >Click here to refresh</a>';
        mainHtml += '<b><i></i></b>';
        mainHtml += '</div>';
        mainHtml += '<div class="col-sm-2">';
        mainHtml += '<a href="#" >Click here to save into Database</a>';
        mainHtml += '</div>';
        mainHtml += '</div>';
        mainHtml += '<table class="table table-bordered">';
        mainHtml += '<thead>';
        mainHtml += '<tr>';
        mainHtml += '<th>Games</th>';
        mainHtml += '<th>Home</th>';
        mainHtml += '<th>Draw</th>';
        mainHtml += '<th>Away</th>';
        mainHtml += '</tr>';
        mainHtml += '</thead>';
        mainHtml += '<tbody>';
        for(var i = 0; i < today_matches_length; i++){
          mainHtml += '<tr>';
          mainHtml += '<td><i>'+ get_todays_matches[i][0] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][1] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][2] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][3] +'</i></td>';
          mainHtml += '</tr>  ';
        }
        mainHtml += '</tbody>';
        mainHtml += '</table>';
        coral_match_day_2.innerHTML = mainHtml;
      }
    }
    http.open("GET", "coral_matches_2", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    coral_match_day_2.innerHTML = '<div class="col-sm-12 text-center">Requesting ...</div>';
  },
  coralGetFutureMatchesB: function(){
    var http = new XMLHttpRequest();
    http.onreadystatechange = function(){
      if(http.readyState == 4 && http.status == 200){
        var get_todays_matches = JSON.parse(http.responseText);
        var today_matches_length = Object.keys(get_todays_matches).length;

        var mainHtml = '';
        mainHtml += '<div class="row" id="refresh_padding">';
        mainHtml += '<div class="col-sm-6"></div>';
        mainHtml += '<div class="col-sm-4">';
        mainHtml += '<a href="#" >Click here to refresh</a>';
        mainHtml += '<b><i></i></b>';
        mainHtml += '</div>';
        mainHtml += '<div class="col-sm-2">';
        mainHtml += '<a href="#" >Click here to save into Database</a>';
        mainHtml += '</div>';
        mainHtml += '</div>';
        mainHtml += '<table class="table table-bordered">';
        mainHtml += '<thead>';
        mainHtml += '<tr>';
        mainHtml += '<th>Games</th>';
        mainHtml += '<th>Home</th>';
        mainHtml += '<th>Draw</th>';
        mainHtml += '<th>Away</th>';
        mainHtml += '</tr>';
        mainHtml += '</thead>';
        mainHtml += '<tbody>';
        for(var i = 0; i < today_matches_length; i++){
          mainHtml += '<tr>';
          mainHtml += '<td><i>'+ get_todays_matches[i][0] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][1] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][2] +'</i></td>';
          mainHtml += '<td><i>'+ get_todays_matches[i][3] +'</i></td>';
          mainHtml += '</tr>  ';
        }
        mainHtml += '</tbody>';
        mainHtml += '</table>';
        coral_match_day_3.innerHTML = mainHtml;
      }
    }
    http.open("GET", "coral_matches_3", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    coral_match_day_3.innerHTML = '<div class="col-sm-12 text-center">Requesting ...</div>';
  },
}

window.onload = function(){
  getGames = new CreateANewRequest();
  if (document.getElementById('game_dates')){
    getGames.coralGetMatchDayDates();
  }
  if (document.getElementById('coral_match_day')){
    getGames.coralGetTodaysMatches();
  }
  if (document.getElementById('coral_match_day_1')){
    getGames.coralGetTomorrowsMatches();
  }
  if (document.getElementById('coral_match_day_2')){
    getGames.coralGetFutureMatchesA();
  }
  if (document.getElementById('coral_match_day_3')){
    getGames.coralGetFutureMatchesB();
  }
}
