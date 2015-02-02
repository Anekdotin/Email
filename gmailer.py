__author__ = 'Edwin'
import smtplib
import socket
import sys
import getpass

def main():
    print()

    try:
        smtpserver= smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        print ('connection to Gmail Successful!')
        try:
            gmail_user = str(input('Enter your Email: ')). lower().strip()
            gmail_pwd = str(input('Enter your password: ')).strip()
            smtpserver.login(gmail_user, gmail_pwd)
        except smtplib.SMTPException:
            print ('Authentication Failed')
            smtpserver.close()
            getpass.getpass('Press Enter to continue...')
            sys.exit(1)

    except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
        print('connection failed!')

        getpass.getpass('press ENTER to continue')
        sys.exit(1)

    while True:


        to = str(input('Send Mail To: ')).lower().strip()
        #if to != (''): break
        #print('this field is required.')
        sub = str(input("Subject: ")).strip()
        bodyMsg = str(input('Compose Email:'))
        print()
        header = 'To:' + to + '\n' + 'From:' + gmail_user + '\n' + 'Subject' + sub + '\n'
        print(header)
        msg = header + '\n' + bodyMsg + '\n\n'

        try:
            smtpserver.sendmail(gmail_user, to, msg)
        except smtplib.SMTPException:
            print('Email could not be sent!') + '\n'
            smtpserver.close()
            getpass.getpass('Press Enter to continue...')
            sys.exit(1)

        print('Email sent successfully!') + '\n'
        smtpserver.close()
        getpass.getpass('Press enter to continue...')
        sys.exit(1)



main()