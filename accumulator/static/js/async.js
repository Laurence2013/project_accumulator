function CreateANewRequest(){}

CreateANewRequest.prototype = {
  constructor: CreateANewRequest,
  getPathName: function(){
    var http = new XMLHttpRequest();
    http.onreadystatechange = function(){
      if(http.readyState == 4 && http.status == 200){
        var dates = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml += '<button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">View all game dates<span class="caret"></span></button>';
        mainHtml += '<ul class="dropdown-menu" role="menu">';
        for (i = 0; i < dates.length; i++){
          mainHtml += '<li><a href="'+ dates[i].pk +'">'+ dates[i]['fields'].dates_of_games + '</a></li>';
        }
        mainHtml += '</ul>';
        results.innerHTML = mainHtml;
      }
    }
    http.open("GET", "daily_match_dates", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    results.innerHTML = 'Requesting ...';
  },
  mainPageLoad: function(){
    var http = new XMLHttpRequest();
    http.onreadystatechange = function(){
      if(http.readyState == 4 && http.status == 200){
        var mainHtml = '';
        mainHtml += '<div class="col-sm-12 text-center">';
        mainHtml += '<div><b>Please select one of the bookies from the drop down menu</b></div>';
        mainHtml += '</div>';
        main_page_load.innerHTML = mainHtml;
      }
    }
    http.open("GET", "daily_match_dates", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    main_page_load.innerHTML = '<div class="col-sm-12 text-center">Requesting ...</div>';
  },
  loadEachGame: function(){
    var http = new XMLHttpRequest();
    http.onreadystatechange = function(){
      if(http.readyState == 4 && http.status == 200){
        var games_with_odds = JSON.parse(http.responseText);
        count = 0
        for(var i in games_with_odds){
          if(games_with_odds.hasOwnProperty(i)) count++;
        }
        var mainHtml = '';
        mainHtml += '<table class="table table-bordered">';
        mainHtml += '<thead>';
        mainHtml += '<tr>';
        mainHtml += '<th>Games</th>';
        mainHtml += '<th>Home Odds</th>';
        mainHtml += '<th>Draw Odds</th>';
        mainHtml += '<th>Away Odds</th>';
        mainHtml += '</tr>';
        mainHtml += '</thead>';
        mainHtml += '<tbody>';
        for(i = 0; i < count; i++){
          mainHtml += '<tr>'
          // games_with_odds[i]['fields'].games_id and games_with_odds[i]['fields'].match
          mainHtml += '<td><input type="checkbox" name="accumulator" value="'+ games_with_odds[i][4] +'" autocomplete="off"/><i> - '+ games_with_odds[i][0] +'</i></td>'
          // games_with_odds[i]['fields'].home_odds
          mainHtml += '<td><i name="home" id="home_odds">'+ games_with_odds[i][1] +'</i></td>'
          // games_with_odds[i]['fields'].draw_odds
          mainHtml += '<td><i name="home" id="home_odds">'+ games_with_odds[i][2] +'</i></td>'
          // games_with_odds[i]['fields'].away_odds
          mainHtml += '<td><i name="home" id="home_odds">'+ games_with_odds[i][3] +'</i></td>'
          mainHtml += '</tr>'
        }
        mainHtml += '</tbody>';
        mainHtml += '</table>';
        mainHtml += '<hr />';
        mainHtml += '<p>';
        mainHtml += 'Stake £: <input id="stake" name="stake" type="text" placeholder="Enter stake here" />';
        mainHtml += '</p>';
        mainHtml += '<button class="btn btn-primary btn-sm" data-target="#myModal" data-toggle="modal">Get accumulator</button>';
        // mainHtml += '<button class="btn btn-primary btn-sm" data-target="#accumulator" data-toggle="modal">Get accumulator</button>';
        each_match.innerHTML = mainHtml;
      }
    }
    http.open("GET", "games/daily_match_games", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
  },
  combinations: function(){
    var http = new XMLHttpRequest();
    http.onreadystatechange = function(){
      if(http.readyState == 4 && http.status == 200){
        var games_with_odds = JSON.parse(http.responseText);
        var games_output = Object.keys(games_with_odds);
        var stake = games_with_odds['stake'];
        var total_games = games_output.length - 2;
        var total_cost = stake * total_games;
        var calc_profit_counter = 0;
        var calc_below_profit_counter = 0;

        var mainHtml = '';
        mainHtml += '<div class="clearfix"></div>';
        mainHtml += '<div class="grid">';
        mainHtml += '<div class="row">';
        mainHtml += '<div class="col-sm-5 col-xs-6"><p class="get_font_size_1"><b>Your chosen games are as follows:</b></p>';
        for(j = 0; j < games_with_odds['match'].length; j++){
            mainHtml +='<p class="get_font_size_2">'+games_with_odds['match'][j]+'</p>';
        }
        mainHtml += '</div>';
        mainHtml += '<div class="col-sm-2 col-xs-3"><p class="get_font_size_1"><b>Other infos:</b></p>';
        mainHtml += '<p class="get_font_size_2"><b>Stake(£): </b>'+ stake +'</p>';
        mainHtml += '<p class="get_font_size_2"><b>Total games: </b>'+ total_games +'</p>';
        mainHtml += '<p class="get_font_size_2"><b>Stake cost(£): </b>'+ total_cost +'</p>';
        mainHtml += '</div>';
        mainHtml += '<div class="row">';
        mainHtml += '<div class="col-sm-5 col-xs-3"><p class="get_font_size_1"><b>Other infos:</b></p>';
        mainHtml += '<p class="get_font_size_2"><b>No. Profit below stake (£): </b>';
        for(k = 0; k < games_output.length - 2; k++){
          var calc_profit = games_with_odds[k][2] - total_cost;
          if(calc_profit.toFixed(2) < 0){
            calc_below_profit_counter += 1;
          }
        }
        mainHtml += calc_below_profit_counter;
        mainHtml += '</p>';
        mainHtml += '<p class="get_font_size_2"><b>No. Profit above or equal to stake (£): </b>';
        for(k = 0; k < games_output.length - 2; k++){
          var calc_profit = games_with_odds[k][2] - total_cost;
          if(calc_profit.toFixed(2) > 0){
            calc_profit_counter += 1;
          }
        }
        mainHtml += calc_profit_counter;
        mainHtml += '</p>';
        mainHtml += ' </div>';
        mainHtml += '</div>';
        mainHtml += '</div>';
        mainHtml += '</div>';
        mainHtml += '<table class="table table-bordered">';
        mainHtml += ' <thead>';
        mainHtml += '   <tr>';
        mainHtml += '     <th>Games outcome</th>';
        mainHtml += '     <th>Match odds 1</th>';
        mainHtml += '     <th>Match odds 2</th>';
        mainHtml += '     <th>Match odds 3</th>';
        mainHtml += '     <th>Match odds 4</th>';
        mainHtml += '     <th>Gross profit from stake</th>'
        mainHtml += '     <th>Net profit from stake</th>';
        mainHtml += '   </tr>';
        mainHtml += ' </thead>';
        mainHtml += ' <tbody>';

        for(i = 0; i < games_output.length - 2; i++){
          games_1 = games_with_odds[i][0][1] ? games_with_odds[i][0][1] : '';
          games_2 = games_with_odds[i][0][3] ? games_with_odds[i][0][3] : '';
          games_3 = games_with_odds[i][0][5] ? games_with_odds[i][0][5] : '';
          games_4 = games_with_odds[i][0][7] ? games_with_odds[i][0][7] : '';
          mainHtml += '<tr>';
          mainHtml += '<td>'+ games_1 + '  ' + games_2  + '  ' + games_3 + '  ' + games_4 +'</td>';
          if(typeof(games_with_odds[i][1][0]) === 'undefined'){
            mainHtml += '<td></td>';
          }else{
            mainHtml += '<td>'+ games_with_odds[i][1][0] +'</td>';
          }
          if(typeof(games_with_odds[i][1][1]) === 'undefined'){
            mainHtml += '<td></td>';
          }else{
            mainHtml += '<td>'+ games_with_odds[i][1][1] +'</td>';
          }
          if(typeof(games_with_odds[i][1][2]) === 'undefined'){
            mainHtml += '<td></td>';
          }else{
            mainHtml += '<td>'+ games_with_odds[i][1][2] +'</td>';
          }
          if(typeof(games_with_odds[i][1][3]) === 'undefined'){
            mainHtml += '<td></td>';
          }else{
            mainHtml += '<td>'+ games_with_odds[i][1][3] +'</td>';
          }
          mainHtml += '<td>'+ games_with_odds[i][2] +'</td>';
          if(games_with_odds['stake']){
            var per_odd_calc = games_with_odds[i][2] - total_cost;
            if(per_odd_calc > 0){
              mainHtml += '<td>' + per_odd_calc.toFixed(2) + '</td>';
            }else{
              mainHtml += '<td id="BelowStake">' + per_odd_calc.toFixed(2) + '</td>';
            }
          }else{
            mainHtml += '<td></td>';
          }
          mainHtml += '</tr>';
        }
        mainHtml += ' </tbody>';
        mainHtml += '</table>';
        mad_combos.innerHTML = mainHtml;
      }
    }
    http.open("GET", "123456/combos", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
  }
}

window.onload = function(){
  getGames = new CreateANewRequest();
  if(window.location.pathname != '/index/'){
    getGames.getPathName();
  }
  if(document.getElementById('main_page_load')){
    getGames.mainPageLoad();
  }
  if(document.getElementById('each_match')){
    getGames.loadEachGame();
  }
  if(document.getElementById('mad_combos')){
    getGames.combinations();
  }
}
