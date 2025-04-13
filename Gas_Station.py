# Have the function GasStation(strArr) take strArr which will be an an array consisting of the following elements: N which
# will be the number of gas stations in a circular route and each subsequent element will be the string g:c where g is the amount
# of gas in gallons at that gas station and c will be the amount of gallons of gas needed to get to the following gas station.

# For example strArr may be: ["4","3:1","2:2","1:2","0:1"]. Your goal is to return the index of the starting gas station
# that will allow you to travel around the whole route once, otherwise return the string impossible. For the example above,
# there are 4 gas stations, and your program should return the string 1 because starting at station 1 you receive 3 gallons of gas
#and spend 1 getting to the next station. Then you have 2 gallons + 2 more at the next station and you spend 2 so you have
# 2 gallons when you get to the 3rd station. You then have 3 but you spend 2 getting to the final station, and at the final
#station you receive 0 gallons and you spend your final gallon getting to your starting point. Starting at any other gas
# station would make getting around the route impossible, so the answer is 1. If there are multiple gas stations that are
# possible to start at, return the smallest index (of the gas station). N will be >= 2.


def GasStation(strArr):

  ruta = []
  for k in strArr[1:]:
      split = k.split(":")
      ruta.append( (int(split[0]), int(split[1])) )

  rotacion = [ ruta[k:]+ruta[:k] for k in range(len(ruta)) ] 

  d = dict(enumerate(ruta, 1))
  d2 = { val:k  for k,val in d.items() }

  indices = []
  for ruta in rotacion:
      acum = 0
      for t in ruta:
          acum += t[0]
          acum -= t[1]
          
          if acum < 0:
              break
      
      # Si se pudo completar el trayecto... dame el idx de la estacion inicial
      if acum >= 0:
          indices.append( d2.get(ruta[0]) )
          
  if indices:
      return min(indices)
  else:
      return "impossible"

# keep this function call here 
print(GasStation(input()))
