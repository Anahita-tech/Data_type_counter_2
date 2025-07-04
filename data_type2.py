a=[1971,2025,'Spacex','Elon_Musk',20.5,54 ,[10,'Tesla',20],{'a':4 , 'b':3 , 4:2},[4,5] ,True,False] # Sample Input
result={'int':0 , 'str':0 ,'float':0 , 'list':0 , 'dict':0 ,'Bool':0} #Initialize counters for different datas as an dictionary
for i in a:
    if isinstance(i,bool): # Using 'isinstance( , ) for detecting the type of data   (Please refer to readme file)
        result['Bool']+=1
    elif isinstance(i,int):
        result['int']+=1
    if isinstance(i,str):
        result['str']+=1
    elif isinstance(i,list):
        result['list']+=1
    elif isinstance(i,dict):
        result['dict']+=1
    elif isinstance(i,float):
        result['float']+=1
print('Result=',result)