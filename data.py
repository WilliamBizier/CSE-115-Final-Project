# Project 3.0 \
#contains projects 2 and 3 


import csv 
import urllib.request
import json



def json_loader(stringurl):
  hold=urllib.request.urlopen(stringurl)
  string=hold.read().decode()
  blob=json.loads(string)
  return blob


def make_values_numeric(liststrings,dic):
  for sec in liststrings:
    a=float(dic[sec])
    dic[sec]=a
  return dic


def write_values(liststringss,listdicks):
  with open(liststringss,'w') as fp:
    writer=csv.writer(fp)
    for lists in listdicks:
      writer.writerow(lists)

def save_data(lok,lod,filename):
  with open(filename,'w') as fw:
    writer=csv.writer(fw)
    writer.writerow(lok)
    for part in lod:
      out=[]
      for parts in lok:
        out.append(part[parts])
      writer.writerow(out)


def dic_list_gen(stringlist,diclist):
  out=[]
  for line in diclist:
    a=0
    b=0
    temp={}
    for part in stringlist:
      temp[stringlist[a]]=line[b]
      a+=1
      b+=1
    out.append(temp)
  return out


def load_data(csvfile):
  temp=[]
  with open(csvfile) as fp:
    reader=csv.reader(fp)
    reading=next(reader)
    print(reading)
    for line in reader:
      temp.append(line)
    result=(dic_list_gen(reading,temp))
  return result


def make_lists(lists, dictionary):
    out = []
    for line in dictionary:
        temp = []
        for listss in lists:
            a = str(listss)
            b = line.get(a)
            temp.append(b)
        out.append(temp)
    return out

def read_values(csvfile):
    out = []
    with open(csvfile) as fp:
        reader = csv.reader(fp)
        next(reader)
        for line in reader:
            out2 = []
            for lines in line:
                out2.append(lines)
            out.append(out2)
    return out
