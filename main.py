# ------------------ Automatic bday mail -------------#
import smtplib

import pandas
import datetime as dt
from random import randint
# ----------Credenciales-----------
my_email = 'marco.a.ponce.p@gmail.com'
password = '&+7UdnP*VO7je'



# --------------Update the birthdays.csv------------


bdays_data = pandas.read_csv('cumpleaños.csv')
bd_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in bdays_data.iterrows()}

today = dt.datetime.now()
today_tuple = (today.month, today.day)


# -------------- Check if today matches one birthday -----------


if today_tuple in bd_dict:
    file_path = f'letter_templates/letter_{randint(1, 3)}.txt'
    bd_person = bd_dict[today_tuple]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", bd_person["name"])


    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()  # Makes our connexion secure
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=bd_person['email'],
            msg=f'Subject: BD {bd_person["name"]} \n\n {contents}'
        )





# ---------- Choose one random letter from the templates and replace data --------------



# ---------- Send the letter generated to the personal email --------------


