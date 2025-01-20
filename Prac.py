

# def fib_nacci(n):
#     a,b = 0,1
#     for i in range(n-1):
#         a,b =b, a+b
#     return a


# results = fib_nacci(100000)
# print(results)

# Q1
def Addition():
    sum= 0
    for i in range(1,10000):
        sum+=i
    return sum


def declarative_addition():
  return sum(range(1,1000000))

# Q2
def sum_of_range(a, b):
  sum = 0
  for i in range(a,b+1):
    sum +=i
  return sum

def sum_of_range_declarative(a, b):
  return sum(range(a, b + 1))

# Q3

def sum_of_even_numbers(a, b):
  sum= 0
  for i in range (a, b +1):
    if i % 2 == 0:
      sum+=i
  return sum

def sum_of_declarative_numbers(a,b):
    return sum(i for i in range(a, b+ 1) if i % 2 ==0)

# Q4

def sum_of_odd_and_even_numbers(a, b):
  even_sum =0
  odd_sum = 0
  for i in range(a, b +1):
    if i % 2 == 0:
      even_sum += i
    else:
      odd_sum += i
  return {"even": even_sum, "odd": odd_sum}

def sum_of_even_and_odd_numbers_declarative(a, b):
  even_sum = sum(i for i in range(a, b + 1) if i % 2 == 0)
  odd_sum = sum(i for i in range (a, b + 1)if i % 2 != 0)
  return {"even": even_sum, "odd": odd_sum}


# Q5

def sum_by_remainder_of_3(a, b):
 
  result = {'0 mod 3': 0, "1 mod 3": 0, "2 mod 3": 0}
  for i in range(a, b + 1):
    remainder = i % 3
    if remainder ==0:
      result["0 mod 3"] += i
    elif remainder == 1:
      result["1 mod 3"] +=i
    else:
      result["2 mod 3"] +=i

  return result

def sum_by_remainder_declarative(a,b):
  return {
    "0 mod 3" : sum(i for i in range (a,b + 1)if i % 3==0),
    "1 mod 3" : sum(i for i in range (a,b + 1)if i % 3==1),
    "2 mod 3" : sum(i for i in range (a,b + 1)if i % 3==2)
  }

# Q6 ?????
def sum_by_remainder_of_n(a, b, n):
 
  sum = {f"{i} mod {n}": 0 for i in range (n)}
  for i in range(a, b + 1):
    remainder = i % n
    sum[f"{remainder} mod n"] += i

  return sum

def sum_by_remainder_declarative(a,b, n):
  return {f"{i} mod {n}": sum(i for i in range(a, b + 1) if i % n ==i) for i in range(n)}


def main():
   Addition()
   sum_by_remainder_of_3(10,20)
   sum_of_even_numbers(10,20)
   sum_of_odd_and_even_numbers(10,20)
   sum_of_declarative_numbers()
   sum_of_even_and_odd_numbers_declarative(5,10)
   declarative_addition()
   sum_by_remainder_declarative(10,20,5)
   sum_by_remainder_of_n(10,22,5)

if __name__== '__main__':
    main()
   