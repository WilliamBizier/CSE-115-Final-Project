import bottle
import json
import data
import processing


@bottle.route("/")
def html_provider():
 return bottle.static_file("index.html", root=".")

@bottle.route("/master.js")
def js_provider():
  return bottle.static_file("master.js", root=".")

#the juicy stuff
@bottle.route("/bar")
def barGraphgen():
  datapart1 = data.load_data("saved_data.csv")
  thedate = processing.max_value(datapart1, 'date')
  temp = []
  for dicks in datapart1:
   if thedate == dicks["date"]:
      temp.append(dicks)
  data2 = data.make_lists(["location", "series_complete_pop_pct"], temp)
  return json.dumps(data2)

@bottle.route("/pie")
def pieGraphgen():
  datapart1 = data.load_data("saved_data.csv")
  temp = []
  for dicks in datapart1:
   datapart2 = data.make_values_numeric(['administered_moderna', 'administered_pfizer', 'administered_janssen', 'administered_unk_manuf'], dicks)
   temp.append(datapart2)
  datapart3 = data.make_lists(['administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf'], temp)
  return json.dumps(datapart3)


@bottle.post("/line")
def lineGraphgen():
  jsonstuff = bottle.request.body.read().decode()
  repotow = json.loads(jsonstuff)
  datapart1 = data.load_data("saved_data.csv")
  temp = []
  for dick in datapart1:
   if "2021" in dick["date"] and repotow == dick["location"]:
    temp.append(dick)
  datapart2 = data.make_lists(["date","location", "series_complete_pop_pct"],temp)
  print(jsonstuff)
  return json.dumps(datapart2)





import os.path
def load_data():
  csvfile = 'saved_data.csv'
  if not os.path.isfile(csvfile):
   url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
   info = data.json_loader(url)
   heads =['date','location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
   data.save_data(heads, info, 'saved_data.csv')


load_data()
bottle.run(host="0.0.0.0",post=8080, debug=True)