"use strict"
// path -- string specifying URL to which data request is sent 
// callback -- function called by JavaScript when response is received       
//from the rubric maches with the post request on the bottom on the page

function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}



function getData(){
 ajaxGetRequest("/bar", showBar);
 ajaxGetRequest("/pie", showPie);
//  ajaxGetRequest("/line", show_lineGraph)
}


function showBar(response){
  let data = JSON.parse(response)
  let bargraph = [{"x":[], "y":[], type: 'bar'}]
  let format = {title:"Fully Vaccinated by Location", font :{family: 'Times New Roman'},xaxis: {title: "Location"}, yaxis:{title:"% Fully Vaccinated"}}
  for(let things of data){
    bargraph[0]["x"].push(things[0])
    bargraph[0]["y"].push(Number(things[1]))
  }
  Plotly.newPlot("bar", bargraph, format)
}

function ajaxPostRequest(path, data, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("POST", path);
    request.send(data);
}

function showPie(response){
  let data = JSON.parse(response)
  let piegraph = [{"values": [], "labels":[], type: 'pie'}]
  let labels = ['Janssen', 'Moderna', 'Pfizer', 'Unknown']
  for(let la of labels){
   piegraph[0]["labels"].push(la)
  }
  let layout = {height: 400, width: 500};
  let moderna = 0;
  let pfizer = 0;
  let janssen = 0;
  let unknown = 0;
  for(let part of data){
    moderna = moderna + part[0]
    pfizer = pfizer + part[1]
    janssen = janssen + part[2]
    unknown = unknown + part[3]
  }
  piegraph[0]["values"].push(moderna)
  piegraph[0]["values"].push(pfizer)
  piegraph[0]["values"].push(janssen)
  piegraph[0]["values"].push(unknown)
  Plotly.newPlot("pie",piegraph, layout)   
}



function getLocData(){
  let loc = document.getElementById("locText");
  let jsonblob = JSON.stringify(loc["value"]);
  ajaxPostRequest("/line", jsonblob, showlineGraph);
}


function showlineGraph(response){
  let data = JSON.parse(response)
  console.log(data)
  let location = data[0][1]
  let line = [{"x": [], "y": [], type: 'line'}]
  for(let part of data){
    line[0]["x"].unshift(part[0])
    line[0]["y"].unshift(Number(part[2]))

  }
  console.log(line)
  let layout = {
  title: '% of '+ location + ' Fully Vaccinated By Date',
  xaxis: {
    title: 'Date'
  },
  yaxis: {
    title: '% Fully Vaccinated'
  }
 };
  Plotly.newPlot("line", location, line);
}



// path -- string specifying URL to which data request is sent
// data -- JSON blob being sent to the server
// callback -- function called by JavaScript when response is received
//mirrors the function on the top of the page
//from rubric
