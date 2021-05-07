import smtplib

LOGIN  = str(input('my e-mail: '))

PASSWORD = str(input('password: '))

FROM = (LOGIN)

TO = str(input('recipient: '))

MESSAGE = 'Hello my friend!'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login(LOGIN, PASSWORD)

server.sendmail(FROM,TO,MESSAGE)

server.quit()




