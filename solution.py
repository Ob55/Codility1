def solution(A, D):
  balance = 0
  mothly_payment = 0
  totoal_income = 0
  
  for i in range(len(A)):
      if A[i] < 0:
          month_payments += 1
          month_total += A[i]
      else:
          month_payments = 0
          month_total = 0
      balance += A[i]
        
        