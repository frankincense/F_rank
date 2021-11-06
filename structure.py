customers = {
    "John Donovan": "Paid",
    "Sylvester Stallone": "Owing",
    "Sandra Ikechi": "Owing",
    "Modupe Morenikeji": "Owing",
    "Silas Ntulikuli": "Owing",
    "Gowon Gocome": "Paid",
    "Fap Fakura": "Paid",
}

debtors_count = 0
nondebtors_count = 0
"""
for value in customers.values():
    if(value.lower() == "owing"):
        debtors_count+=1
"""
print("The number of debtors are ",  debtors_count)

#THE RATIO OF PAYING CUSTOMERS TO DEBTORS 
ratio=[]
for value in customers.values():
    if(value.lower() == "owing"): 
        debtors_count+=1
    else:
        nondebtors_count+=1

ratio.insert(0, nondebtors_count)
ratio.insert(1, debtors_count)

print("The ratio OF PAYING CUSTOMERS TO DEBTORS ", ratio)
