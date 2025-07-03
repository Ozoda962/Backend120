print("Hello world")

a = 4
b=5
c = a + b

print(c)


from datetime import date,timedelta

def yakshanbalar_royxati(yil):
    
    boshlanish = date(yil, 1, 1)
    tugash = date(yil, 12, 31)
    kun = boshlanish
    royxat = []

    while kun <= tugash:
        if kun.weekday() == 6:
            royxat.append(kun)
        kun += timedelta(days=1)

    for sana in royxat:
        print(sana)
    


print(yakshanbalar_royxati(2024))