def critical_hpur_Counter(n:int,vehicle_count:list):
  if(n<1):
    return 0
  number = 0
  for i in range(1,n):
      if(vehicle_count[i]>=50 and vehicle_count[i]>vehicle_count[i-1]):
        number +=1
  return number

n = int(input("Enter the number of hours: "))
num = list(map(int,input("Enter the number of vehicle per hour seperated by space:").split()))

a = critical_hpur_Counter(n,num)
print(a)