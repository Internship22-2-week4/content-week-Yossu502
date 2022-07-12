
def likes(like):
  if len(like) == 3:
    return like
  
  elif len(like) == 4:
    return f'{like[0]}K'

  elif len(like) == 5:
    return f'{like[0:2]}K'
  
  elif len(like) == 6:
    return f'{like[0:3]}K'
  
  elif len(like) == 7:
    return f'{like[0]}M'
  
  elif len(like) == 8:
    return f'{like[0:2]}M'
  
  elif len(like) >= 9:
    return f'{like[0:3]}M'



if __name__ == '__main__':
  print(likes(str(983)))
  print(likes(str(1900)))
  print(likes(str(54000)))
  print(likes(str(120800)))
  print(likes(str(25222444)))