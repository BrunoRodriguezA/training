# Tienes una lista de ventas:
sales = [
  {"user":"ana","amount":10},
  {"user":"luis","amount":7},
  {"user":"ana","amount":3},
]

# Escribe sum_by_user(sales) → {"ana": 13, "luis": 7}

def sum_by_user(sales:list[dict]) -> dict[str,int]:
    sales_by_user = {}
    
    for data in sales: 
        user = data['user']
        amount = data['amount']
        sales_by_user[user] = sales_by_user.get(user, 0) + amount
        
    return sales_by_user


print(sum_by_user(sales))