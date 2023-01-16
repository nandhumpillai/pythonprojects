import requests
from bs4 import BeautifulSoup as Bs
import smtplib
from email.mime.text import MIMEText

url = 'https://coinmarketcap.com/currencies/bitcoin/'

headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

page = requests.get(url, headers=headers)
print(page.status_code)


soup = Bs(page.content, 'html.parser')
# print(soup.prettify())
price = soup.find_all(attrs={"class": "priceValue"}).__str__()
print(str(price))
print(smtplib.SMTP_PORT)


def sendmailtoone():
    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()  # encryption
        sender = 'asokananu65@gmail.com'
        recipient = 'shilpaseetha699@gmail.com'
        mail.login('asokananu65@gmail.com', 'zntckcditpbsgzkp')
        content = "This is another mail sent by nandhu"
        header = 'To:' + recipient + '\n' + 'From:' \
                 + sender + '\n' + 'subject:email tester\n'
        content = header + content
        mail.sendmail(sender, recipient, content)
        mail.quit()
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")


def sendmail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    msg = MIMEText("""body""")
    sender = 'asokananu65@gmail.com'
    recipients = ['nandhumpillai0@gmail.com', 'asokananu65@gmail.com', 'nandhurock347@gmail.com',
                  'viswajithbhanderi@gmail.com', 'sudhakarsandeep146@gmail.com']
    msg['Subject'] = "subject line"
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    s.login('asokananu65@gmail.com', 'zntckcditpbsgzkp')
    s.sendmail(sender, recipients, msg.as_string())
    s.close()


while True:
    sendmailtoone()
 