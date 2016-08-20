def data_type(myarg):
  if type(myarg) is str:
    return len(myarg)
  
  elif type(myarg) is None:
    return 'no value'
  
  elif type(myarg) is bool:
    if myarg:
      return True
    return False
  
  elif type(myarg) is int:
    if myarg < 100:
      return 'less than 100'
    elif myarg > 100:
      return 'more than 100'
    elif myarg == 100:
      return 'equal to 100'
  
  elif type(myarg) is list:
    if len(myarg) >= 3:
      return myarg[2]
    return 'length is less than required'

# print data_type('')
# print data_type(True)
# print data_type(6999)
# print data_type([1,2])
