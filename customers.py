# Customers.py


# import calendar
import datetime
from datetime import datetime,date,timedelta

import time
import smtplib, ssl

# for start tls 587
#for ssl 
# port = 465
# smtp_server = "smtp.gmail.com"
# sender_email = "neepssystemandsales@gmail.com"
# receiver_email = "pranav.chandran@gmail.com"

# password = '9656888140'


# def split(customers,products):

#     # get current date
#     today = date.today()
#     # print(today)

#     # Difference can be check by this
#     # join = date(year,month,day)   
#     t1 = date(year = 2020, month = 4, day = 24)
#     # end = date(year,month,day)  
#     t2 = date(year = 2020, month = 4, day = 27)
#     t3 = t2 - t1
#     print("Difference =", t3)

#     return customers,products


# print(split('Pranav','Prime'))

def split():
    joineddate = ['26/4/2020 ','26/4/2020 ', '23/4/2020 ']
    customers = ['Athul:Prime','Pranav:Prime']

    # details = {[lambda x,y:for x in joineddate and for y in customers]}
    # print(list(map(lambda x,y,z: l1,l2,l3)))
    # print(list(map(lambda x,y,z: x+y+z, l1,l2,l3)))
    details = (list(map(lambda x,y:x+y, joineddate , customers)))
    for x in details:
        print(x)
    # print(details)    
    # for y in joineddate:
    #     details.append(y)

    # for x in customers:
    #     details.append(x)

    #     print(y)
        # print(details)


    
    # for y,x in joineddate,customers:
    #     print([x],y)
    # print(joineddate,customers)
    return split

split()


    
def days(year,month,day,*customers):
    
    # year = int(input('2020'))
    # month = int(input('5'))
    # day = int(input('24'))

    smtp_server = "smtp.gmail.com"
    sender_email = "neepssystemandsales@gmail.com"
    receiver_email = "pranav.chandran@gmail.com"

    password = '9656888140'
    today = date.today()
    date1 = date(year,month,day)
    # date1 = date(2020, 4, 24)
    t3 = {today - date1}

    if t3 == {timedelta(days=30)}:
        message = f"{customers} subscription period Ended"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
            server.login(sender_email,password)
            server.sendmail(sender_email,receiver_email,message)

        print(f'{customers} Subscription Renewal Time')

    else:
        print(f'{customers} Subscription not end')
    print('Billed from : ',today)
    
    print(*t3)
    # for x in t3:
    #     print(x)
    # print(str(customers))
    # print(f'{customers}  now ,{t3}')
    
    return customers
    
starttime=time.time()
while True:
    # it means one day-for an app running every 1 day at pythonanywhere
    time.sleep(86400)
    # time.sleep(5)
    # time.sleep(10.0 - ((time.time() - starttime) % 10.0))
    days(2020,4,24,'pranav')
    days(2020,4,23,'Athul')





# format year month date
# a = datetime(2020,4,26)
# print(a)


# for getting date and time

# datetime_object = datetime.datetime.now()
# print(datetime_object)

# print(message)
# cal = calendar()
# print(cal.iterweekdays())


# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
#     server.login(sender_email,password)
#     server.sendmail(sender_email,receiver_email,message)



# app = qpzxxbydoqkrsego  