def icecream_budget(budget:int,price_list:list):
    m  = len(price_list)
    flag = False
    for i in range(m):
          if(budget == price_list[i]):
            flag = True
    return flag

price_list = [23,35,20,10,35]
budget_shivam = int(input("Enter your budget:"))

budget_checker = icecream_budget(budget_shivam,price_list)

print(budget_checker)


