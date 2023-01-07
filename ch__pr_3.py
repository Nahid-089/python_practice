#sum(n) = sum(n-1) + n




def recur_sum(n):

 if n == 1 or n == 0:
     return 1
  return n + recur_sum(n-1)

print(recur_sum(num))




