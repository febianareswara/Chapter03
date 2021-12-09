from datetime import *
print('Menghitung selisih hari')
print('-----------------------')
today = date.today()
def diffDate(x):
    today = date.today()
    x = datetime.strptime(x, '%Y-%m-%d').date()
    diff = today - x
    return abs(diff)
print(today)
print('Jadi selisih hari ini sampai dengan 2021-12-30 adalah :')
print((diffDate('2021-12-30').days),'hari')
