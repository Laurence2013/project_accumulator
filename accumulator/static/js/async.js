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
    http.setRequestHeader('Contet-type', 'application/json', true);
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
    http.setRequestHeader('Contet-type', 'application/json', true);
    http.send();
    main_page_load.innerHTML = '<div class="col-sm-12 text-center">Requesting ...</div>';
  },
  loadEachGame: function(){
    var http   = new XMLHttpRequest();
    http.onreadystatechange = function(){
      if(http.readyState == 4 && http.status == 200){
        var games_with_odds = JSON.parse(http.responseText);
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
        for(i = 0; i < games_with_odds.length; i++){
          mainHtml += '<tr>'
          mainHtml += '<td><input type="checkbox" name="accumulator" value='+ games_with_odds[i]['fields'].games_id +'/><i name="game" id="games"> - '+ games_with_odds[i]['fields'].match +'</i></td>'
          mainHtml += '<td><i name="home" id="home_odds">'+ games_with_odds[i]['fields'].home_odds +'</i></td>'
          mainHtml += '<td><i name="home" id="home_odds">'+ games_with_odds[i]['fields'].draw_odds +'</i></td>'
          mainHtml += '<td><i name="home" id="home_odds">'+ games_with_odds[i]['fields'].away_odds +'</i></td>'
          mainHtml += '</tr>'
        }
        mainHtml += '</tbody>';
        mainHtml += '</table>';
        mainHtml += '<hr />';
        mainHtml += '<p>';
        mainHtml += 'Stake £: <input id="stake" name="stake" type="text" placeholder="Enter stake here" />';
        mainHtml += '</p>';
        mainHtml += '<input type="submit" value="Get accumulator" />';
        each_match.innerHTML = mainHtml;
      }
    }
    http.open("GET", "games/daily_match_games", true);
    http.setRequestHeader('Contet-type', 'application/json', true);
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
}

  // if(window.location.pathname != '/index/'){
  //     CreateANewRequest.http.onreadystatechange = function(){
  //         if(CreateANewRequest.http.readyState == 4 && CreateANewRequest.http.status == 200){
  //           var dates = JSON.parse(CreateANewRequest.http.responseText);
  //           var mainHtml = '';
  //           mainHtml += '<button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">View all game dates<span class="caret"></span></button>';
  //           mainHtml += '<ul class="dropdown-menu" role="menu">';
  //           for (i = 0; i < dates.length; i++){
  //             mainHtml += '<li><a href="'+ dates[i].pk +'">'+ dates[i]['fields'].dates_of_games + '</a></li>';
  //           }
  //           mainHtml += '</ul>';
  //           results.innerHTML = mainHtml;
  //         }
  //       }
  //
  //     CreateANewRequest.http.open("GET", "daily_match_dates", true);
  //     CreateANewRequest.http.setRequestHeader('Contet-type', 'application/json', true);
  //     CreateANewRequest.http.send();
  //     results.innerHTML = 'Requesting ...';
  //   }else{
  //     if(document.getElementById('main_page_load')){
  //       CreateANewRequest.http.onreadystatechange = function(){
  //         if(CreateANewRequest.http.readyState == 4 && CreateANewRequest.http.status == 200){
  //           var mainHtml = ''
  //           mainHtml += '<div class="col-sm-12 text-center">';
  //           mainHtml += '<div><b>Please select one of the bookies from the drop down menu</b></div>';
  //           mainHtml += '</div>';
  //           main_page_load.innerHTML = mainHtml;
  //         }
  //       }
  //       CreateANewRequest.http.open("GET", "daily_match_dates", true);
  //       CreateANewRequest.http.setRequestHeader('Contet-type', 'application/json', true);
  //       CreateANewRequest.http.send();
  //       main_page_load.innerHTML = '<div class="col-sm-12 text-center">Requesting ...</div>';
  //   }
  //   if (document.getElementById('each_match')){
  //     console.log('this is to load')
  //   }
  // }
