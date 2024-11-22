średnia = int(input("podaj średnią"))

if średnia >=100:
  print("celująca")
  
elif średnia <=99 and średnia >= 90:
  print("bardzo dobra")
  
elif średnia <=89 and średnia >= 75:
  print("dobra")
  
elif średnia <=74 and średnia >= 60:
  print("dostateczny")
  
elif średnia <=59 and średnia >= 50:
  print("dopuszczająca")

else:
  print("niedopuszczająca")