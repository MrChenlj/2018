# num = float(input("请输入一个数字： "))
# num_sqrt = num ** 0.5
# print('%0.2f 的平方根为 %0.3f'%(num, num_sqrt))

# import cmath
# aa = 25
# a = float(input("输入 a："))
# b = float(input('输入 b：'))
# c = float(input('输入 c：'))
#
# d = (b**2) - (4*a*c)
# print(d)
# sol1 = (-b-cmath.sqrt(d))/(2*a)
# sol2 = (-b+cmath.sqrt(d))/(2*a)
# print(d)
# print(cmath.sqrt(aa))
#
# print('结果为 {0} 和 {1}'.format(sol1,sol2))

# import cmath
# a = float(input('请输入三角形的第一边长：'))
# b = float(input('请输入三角形的第二边长：'))
# c = float(input('请输入三角形的第三边长：'))
#
# s = (a + b + c) / 2
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print('三角形面积为 %0.2f' % area)
#
# result = cmath.sqrt(s*(s-a)*(s-b)*(s-c))
# print('三角形面积为 %s' % result)
# import random
# print(random.randint(0,9))
#
# celsius = float(input('请输入摄氏温度： '))
# fahernheit = (celsius * (9/5)) + 32
# print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahernheit))

# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#     return False
# print(is_number('fott'))
# print(is_number('1'))
# print(is_number(1.3))
# print(is_number('1e3'))
# num = int(input('请输入一个数字： '))
# if (num % 2) == 0:
#     print('{0} 是偶数'.format(num))
# else:
#     print('{0} 是奇数'.format(num))

# year = int(input('请输入一个年份： '))
# if (year % 4) == 0:
#     if ( year % 100) == 0:
#         if (year % 400) == 0:
#             print('%s是闰年' % year)
#         else:
#             print('{0}不是闰年'.format(year))
#     else:
#         print('{0}是闰年'.format(year))
# else:
#     print('{0}不是闰年'.format(year))
#
# print(year / 4)
#
# if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
#     print('{0}是闰年'.format(year))
# else:
#     print('{0}不是闰年'.format(year))

#
# import datetime
# def getYesterday():
#     today = datetime.date.today()
#     oneday = datetime.timedelta(days=0)
#     yesterday = today - oneday
#     return yesterday
# y = getYesterday()
# print(y)
# y = '%s' % y
#
# yy, mm, dd =  y.split('-')
#
# import calendar
# print(calendar.month(int(yy),int(mm)))

# def is_leap_year(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 ==0
#
# def get_num_of_days_in_month(year, month):
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         return 31
#     elif month in (4, 6, 9, 11):
#         return 30
#     elif is_leap_year(year):
#         return 29
#     return 28
# def get_total_num_of_days(year, month):
#     days = 0
#     for y in range(1800, year):
#         if is_leap_year(y):
#             days += 366
#         else:
#             days += 365
#     for m in range(1, month):
#         days += get_num_of_days_in_month(year, m)
#     return days
# def get_start_day(year, month):
#     day = (3 + get_total_num_of_days(year, month)) % 7
#     if day == 0:
#         day = 7
#     return day
#
#
# def print_table_head(year, month):
#     if month >= 10:
#         print(str(month) + '月' + ' '*38 + str(year) + '年')
#     else:
#         print(str(month) + '月' + ' ' * 39 + str(year) + '年')
#     print("%s" % '-'*48)
#     l = ('星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日')
#     for i in l:
#         print(format(i, '2'), end=' ')
# def print_calender(year, month):
#     print_table_head(year, month)
#     days = get_num_of_days_in_month(year, month)
#     start_day_of_week = get_start_day(year, month)
#     l = []
#     while start_day_of_week > 0:
#         l.append('')
#         start_day_of_week -= 1
#     for day in range(1, days + 1):
#         l.append(day)
#     for i in range(len(l)):
#         print(format(l[i], '6'), end=' ')
#         if i % 7 == 0:
#             print()
#
#         i -= 1
#     print()
# print_calender(2018, 7)

# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != k) and (i != j) and (j != k):
#                 print(i, j, k)

