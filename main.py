import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.de/-/en/Nikkipet-Jogging-Running-Walking-Abdominal/dp/B01IT9WE0C/ref=sr_1_29?keywords=hunde" \
      "+laufleine&qid=1678995837&refinements=p_72%3A419117031&rnid=419116031&sprefix=dog+runn%2Caps%2C109&sr=8-29 "


# Set the headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7'
}

# Make the request
response = requests.get(url, headers=headers)


# Create BeautifulSoup object
soup = BeautifulSoup(response.content, 'lxml')

# Find the span element that contains the price and Extract the text from the span element
product_price = soup.find(class_="a-offscreen").get_text()


# Take final price as float
price_without_currency = product_price.split("€")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# Get title of product
product_Name = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").get_text()

# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
# smtp_port = 587
smtp_username = 'elizatxbox@gmail.com'
smtp_password = 'luyooaxezocqtktk'

# Set up the email message
sender_email = 'elizatxbox@gmail.com'
recipient_email = 'elizat88@gmail.com'
subject = 'Price Alert !!!!'
body = f'{product_Name}\nis now : €{price_as_float}'

message = f'Subject: {subject}\n\n{body}'

# Send the email
if price_as_float <= 20:
    with smtplib.SMTP(smtp_server) as connection:
        connection.starttls()  # secure the code
        connection.login(user=smtp_username, password=smtp_password)  # Login to e-mail
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=message.encode('utf-8')
        )  # send e-mail
        print('Email sent successfully')


