def solution(A,D):
    balance = 0
    monthly_debits = 0 
    monthly_debit_total = 0 
    current_month = D[0][:7]
    
    for i in range(len(A)):
        if A[i] < 0:
            monthly_debits += A[i]
            monthly_debit_total += A[i]
            
            balance += A[i]
            
            next_trancaction_month = D[i+1] if i+1 < len(D) else None
            if next_trancaction_month != current_month:
                if monthly_debits >= 3 and monthly_debit_total <= -100:
                    balance += 5
                    monthly_debits = 0
                    if next_trancaction_month:
                        current_month = next_trancaction_month
        
        return balance