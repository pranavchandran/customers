# sending mail First
# from customers import days
# import smtplib, ssl

# for start tls 587
#for ssl 
# port = 465
# smtp_server = "smtp.gmail.com"
# sender_email = "neepssystemandsales@gmail.com"
# receiver_email = "pranav.chandran@gmail.com"

# password = '9656888140'

# days(2020,4,24,'pranav')
# days(2020,4,23,'Athul')
# print(customers)

# message = f"{customers} subscription period Ended"

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
#     server.login(sender_email,password)
#     server.sendmail(sender_email,receiver_email,message)


# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(EMAIL_HOST,EMAIL_PORT,context=context) as server:
#     server.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
#     server.sendmail(EMAIL_HOST_USER,receiver_email,message)


import time
starttime=time.time()
while True:
  print("tick")
  time.sleep(10.0 - ((time.time() - starttime) % 10.0))