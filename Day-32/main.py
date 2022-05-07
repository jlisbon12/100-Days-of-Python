# import smtplib
#
# my_email = "trashmoon70@gmail.com"
# password = "lisbon2020"
#
# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="jlisbon12@outlook.com", msg="Subject:Hello\n\n"
#                                                                                   "This is the body of the email")

#
# import datetime as dt
#
# today = dt.datetime.now()
# year = today.year
# month = today.month
# wk = today.weekday()
# print(year)
# print(month)
# print(wk)
#
# date_of_birth = dt.datetime(year= 2001, month= 10, day= 27, hour=4)
# print(date_of_birth)

# CHALLENGER
import random
import smtplib
import datetime as dt
from email.mime.text import MIMEText

today = dt.datetime.now()
wk = today.weekday()
my_email = "trashmoon70@gmail.com"
password = "lisbon2020"


if wk == 4:
    with open("quotes.txt", "r") as q:
        list_quotes = q.readlines()
        quote = random.choice(list_quotes)
    print(quote)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="jlisbon12@outlook.com",
                            msg=f'Subject:Happy Birthday\n\n{quote}')
