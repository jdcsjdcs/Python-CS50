months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]

while True:

    date = input('Date: ')

    try:
        m, d, y = date.split('/')
        if 0 < int(m) < 13 and 0 < int(d) < 32:
            break

    except:
        try:
            m, d, y = date.split(' ')
            d.endswith(',') == True

            if m in months and 0 < int(d.replace(',','')) < 32 and d.endswith(','):
                d = d.replace(',','')
                m = months.index(m) + 1
                break
        except:
            print()
            pass

print(f'{int(y)}-{int(m):02}-{int(d):02}')