amount_due = 50

while amount_due > 0:
    print(f'Amount due: {amount_due}')
    coin = input('Insert coin: ')
    if coin in ['5', '10', '25']:
        amount_due = amount_due - int(coin)

print(f'Change: {abs(amount_due)}')