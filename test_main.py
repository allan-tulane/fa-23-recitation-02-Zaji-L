from main import *
  
  def test_simple_work():
  """ done. """
  assert simple_work_calc(10, 2, 2) == 60
  assert simple_work_calc(20, 3, 2) == 240
  assert simple_work_calc(30, 4, 2) == 900
  
  def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 21
  assert work_calc(20, 1, 2, lambda n: n*n) == 2875
  assert work_calc(30, 3, 2, lambda n: n) == 819
  