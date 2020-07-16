import func_module

#func_module.module_show()

nowdate=func_module.date_now()
now_year=nowdate.year
date_today='{}년 {}월 {}일'.format(nowdate.year,nowdate.month,nowdate.day)
#print(nowdate)
#print(now_year)
print(date_today)

x_mas=nowdate.replace(month=12, day=25)
date_xmas='{}년 {}월 {}일'.format(x_mas.year,x_mas.month,x_mas.day)
print(date_xmas)

#교재
#start_time=datetime.datetime.now()
#start_time.replace(month=12, day=25)