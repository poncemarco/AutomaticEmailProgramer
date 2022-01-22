import smtplib
import datetime as dt
my_email = 'marco.a.ponce.p@gmail.com'
password = '&+7UdnP*VO7je'

'''with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()   # Makes our connexion secure
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='marko_ponce@hotmail.com',
        msg='Subject:Practice \n\n This is the body of my email'
    )
'''
# datetime module
now = dt.datetime.now() # Get the correct time
year = now.year     # Se puede obtener algunos atributos
# print(now)
# Create a day
date_of_birth = dt.date(year=1998, month=11, day=14)
print(date_of_birth)