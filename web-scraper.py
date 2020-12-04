import requests
from bs4 import BeautifulSoup
import smtplib

URL ='https://www.amazon.in/Redmi-Note-Space-Black-Storage/dp/B07X4PXKZ7/ref=br_msw_pdt-1?_encoding=UTF8&smid=A23AODI1X2CEAE&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=7K3H6CHCNYV00HT3CCKD&pf_rd_t=36701&pf_rd_p=72d48896-4d71-41bb-878b-961db227d942&pf_rd_i=desktop'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36' }

def check_price():
    page= requests.get(URL,headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()
    convert=price[2:8]
    print(title)
    print(convert)

    if convert=='10,499':
        print('price dropped')
        send_email('Dropped')

    elif convert >'10,499':
        send_email('Increased')

    else:
        print('same')


def send_email(read):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('enter email','enter password')
    subject= f'PRICE HAS {read}\n\n'
    body ='Check it out ! https://www.amazon.in/Redmi-Note-Space-Black-Storage/dp/B07X4PXKZ7/ref=br_msw_pdt-1?_encoding=UTF8&smid=A23AODI1X2CEAE&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=7K3H6CHCNYV00HT3CCKD&pf_rd_t=36701&pf_rd_p=72d48896-4d71-41bb-878b-961db227d942&pf_rd_i=desktop'

    msg= f"Subject:{subject}\n\n{body}"

    server.sendmail('enter email id sender',
    'enter receipent email id',msg
    )
    print('EMAIL SENT !')

    server.quit()



check_price()
