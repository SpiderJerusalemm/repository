def read_last(lines, file = open('c:/py/prticle.txt')):    
  file = file.readlines()
    for i in range(lines, 0, -1):        
      print(file[-(i)])
lines = int(input())
read_last(lines) 
