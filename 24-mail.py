import smtplib

hostname = 'smtp.gmail.com'                         #SMTP (Simple Mail Transfer Protocol) server address for Gmail.              
email = 'srikanthj2311@gmail.com'
password = 'thrbixnnbybftarq'                       #Password that we take from gmail account--security--app passwords.

with smtplib.SMTP(host=hostname) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg=f'Subject: Test from Python \n\n Hi Srikanth\n This is test mail from python'    #Send mail with particular subject and body.
        
    )