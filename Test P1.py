
cleaning_rate = 60
cavity_filling_rate = 200
xray_rate = 100
tax_rate = 0.15

name = input("Enter patient's name: ")
cleaning = input("Was cleaning performed? (y/n): ")
cavity_filling = input("Was cavity-filling performed? (y/n): ")
xray = input("Was X-Ray performed? (y/n): ")

def calculate_bill(name, cleaning, cavity_filling, xray):
   
    subtotal = 0
    if cleaning == 'y':
        subtotal += cleaning_rate
    if cavity_filling == 'y':
        subtotal += cavity_filling_rate
    if xray == 'y':
        subtotal += xray_rate

    if subtotal > 300:
        subtotal *= 0.9
    elif subtotal > 200:
        subtotal *= 0.95
    
    tax = subtotal * tax_rate
    
    total = subtotal + tax
   
    print("Melanie Dental Clinic")
    print("--------------------")
    print(f"Receipt for patient name: {name}")
    print("--------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print("--------------------")
    print(f"Total: ${total:.2f}")

calculate_bill(name, cleaning, cavity_filling, xray)

