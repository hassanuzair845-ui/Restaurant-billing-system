#billing system

print('Welcome to Syed Resturent')
total_bill=0
while True:
    print('\nMenu' )
    print('1. Burrger = $5')
    print('2. Shwarma = $8')
    print('3. Drinks = $2')
    print('4. Fries = $1')

    choice=int(input('Enter Item number: '))
    quantity=int(input('Enter Quantity: '))

    if choice==1:
        item='Burger'
        price= 5

    elif choice==2:
        item='Shwarma'
        price= 8

    elif choice==3:
        item='drinks'
        price= 2

    elif choice==4:
        item='fries'
        price=1
    else:
        print('Invalid Item')
        continue

    bill=price*quantity
    total_bill=total_bill+bill

    print('\nitem :', item)
    print(' Price:', price)
    print(' quantity:', quantity)
    print('Item Bill:', bill)

    more=input('Do you want to order more items? (Y/N)')
    if more.lower()!='y':
        break

print('Final bill:')
print('total bill: ', total_bill)

print('\n Thankyou visiting')
    



  