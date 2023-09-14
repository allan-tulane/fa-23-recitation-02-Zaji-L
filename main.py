"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
"""Compute the value of the recurrence $W(n) = aW(n/b) + n

Params:
n......input integer
a......branching factor of recursion tree
b......input split factor

Returns: the value of W(n).
"""

  if n == 0:
    return 0 #base case
  else:
    return a * simple_work_calc(n // b, a, b) + n



pass

def work_calc(n, a, b, f):
"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

Params:
n......input integer
a......branching factor of recursion tree
b......input split factor
f......a function that takes an integer and returns 
         the work done at each node 

Returns: the value of W(n).
"""
if n<= 0:
  return 0 #base case
else:
  return a*work_calc(n//b,a,b,f) + f(n)
pass

def span_calc(n, a, b, f):
"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

Params:
n......input integer
a......branching factor of recursion tree
b......input split factor
f......a function that takes an integer and returns 
       the work done at each node 

Returns: the value of W(n).
"""
if n == 0:
        return 0  # base case
    else:
        span = f(n) 
        child_spans = [span_calc(n // b, a, b, f) for _ in range(b)]
        span += max(child_spans)
        return span
pass



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
"""
Compare the values of different recurrences for 
given input sizes.

Returns:
A list of tuples of the form
(n, work_fn1(n), work_fn2(n), ...)

"""
result = []
for c in c_values:
        for log_a in log_a_values:
            for n in sizes:
                # compute W(n) using current a, b, f
                result = work_fn1(n, a=2, b=2, c=c)
                results.append((n, c, log_a, result))
return result

def print_results(results):

  print(tabulate.tabulate(results,
              headers=['n', 'W_1', 'W_2'],
              floatfmt=".3f",
              tablefmt="github"))
  
  def test_compare_work():
  # curry work_calc to create multiple work
    def create_work_fn(a, b, f):
          def work_fn(n):
              return work_calc(n, a, b, f)
          return work_fn
  # functions taht can be passed to compare_work
    
  # create work_fn1
  work_fn1 = create_work_fn(2, 2, lambda n: n)
  # create work_fn2
  work_fn2 = create_work_fn(3, 2, lambda n: n * n)
  
  res = compare_work(work_fn1, work_fn2)
  print(res)

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
"""
Compare the values of different recurrences for
given input sizes.
Returns:
A list of tuples of the form
(n, work_fn1(n), work_fn2(n), ...)
"""
result = []
for n in sizes:
# compute W(n) using current a, b, f
result.append((
n,
span_fn1,
span_fn2
))
return result




def test_compare_span():
  def span_time(n, a, b, f):
      span = span_calc(n, a, b, f)
      return span / a  


  span_1 = span_time(10, 2, 2, lambda n: 1)
  assert span_1 == 15.0

  span_2 = span_time(20, 1, 2, lambda n: n * n)
  assert span_2 == 4140.0

  span_3 = span_time(30, 3, 2, lambda n: n)
  assert span_3 == 1640.0

