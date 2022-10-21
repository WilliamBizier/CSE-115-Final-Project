#Project 1 ( the vaccine one and stuff)

def max_value(listDic,stringKey):
  number=""
  for dics in listDic:
   strings=dics[stringKey]
   if strings>number:
     number=strings 
  return number 


def init_dictionary(listDics,stringkey):
  dictionary={}
  for indics in listDics: 
    if stringkey in indics: 
      v=indics[stringkey]
      dictionary[v]=0
  return dictionary

def sum_matches(lod,k,v,tgt):
  matches=0
  for inlod in lod: 
    value=inlod[k]
    if value==v: 
      matches=matches+inlod[tgt]
  return matches 

def copy_matching(lod,k,v):
  thelist=[]
  for inlod in lod: 
    if v==inlod[k]:
      thelist=thelist+[inlod]
  return thelist



