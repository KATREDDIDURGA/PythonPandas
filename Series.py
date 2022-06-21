import pandas as pd
#Series : one dimentional labled array 
#Series is a class
#single collection data store things in order and gives you an identifier called index
#Object doesntot belong to python but beongs to pandas
#output is ordered collection of data
#list is orgdered, dictionary is not ordered and has identifier...series makes these two properties combined together
'''One-dimensional ndarray with axis labels (including time series).
Labels need not be unique but must be a hashable type. 
The object supports both integer- and label-based indexing and provides 
a host of methods for performing operations involving the index. '''
#***************lists to series**********************
ice_cream = ['chocolate','vanilla','strawberry','red velvet']
print(pd.Series(ice_cream))
'''
0     chocolate
1       vanilla
2    strawberry
3    red velvet
dtype: object  ----data type string is expressed as object in python'''


lottery = [10,20,30,40,50]
print(pd.Series(lottery))
'''0    10
1    20
2    30
3    40
4    50
dtype: int64 ----here 64 is number of bytes each integer is occupying the memory'''

Registrations=[True, False,True, True, True]
print(pd.Series(Registrations))

'''0     True
1    False
2     True
3     True
4     True
dtype: bool'''
#***************dictionary to series**********************

sushi = {
    "salmon" : "orange",
    "tuna" :  "red",
    "Eel" : "brown"
}
print(pd.Series(sushi))
'''
salmon    orange   ----will have numeric index 0 and identifier as salmon
#tuna         red
#Eel        brown
#dtype: object
# '''



#series can have duplicate lables