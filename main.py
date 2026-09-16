# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas as pd
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
letters = ['letter_1.txt','letter_2.txt','letter_3.txt']
def get_letter(date):
    person_file = birthdays[(birthdays.month==date.month) & (birthdays.day ==date.day)]
    name = person_file.name.item()
    filepath = f"letter_templates/{random.choice(letters)}"

    with open(filepath,"r") as file:
        content = file.read()
        new_letter = content.replace("[NAME]", name)

    return new_letter

birthdays = pd.read_csv("birthdays.csv")
dates_list = []
for index,row in birthdays.iterrows():
    birthday = datetime.datetime(year= row.year,month=row.month,day=row.day)
    dates_list.append(birthday)

today = datetime.datetime.now()
for date in dates_list:
    if date.day == today.day and date.month == today.month:
        letter2send = get_letter(date)
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(email,PASSWORD)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg= letter2send
            )
