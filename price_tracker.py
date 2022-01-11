import requests
import smtplib
from bs4 import BeautifulSoup


class AmazonTracker:
    def __init__(self, preferred_price, my_email, email_password, product_url, header):
        self.email_user = my_email
        self.preferred_price = preferred_price
        self.email_password = email_password
        self.product_url = product_url
        self.header = header

        self.product_title = None
        self.product_price = None
        self.response = None
        self.soup = None

    def check_product(self):
        self.get_response()
        self.create_soup()
        self.get_product_title()
        self.get_product_price()
        self.compare_prices()

    # This is used to update self.response to any new url
    def get_response(self):
        self.response = requests.get(url=self.product_url, headers=self.header)
        print("Response received.")

    # Used to update self.soup with new self.response after using get_respose
    def create_soup(self):
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

    # Finds the price text within the element and converts it to a float
    def get_product_price(self):
        self.product_price = float(self.soup.find('span', class_="a-offscreen").text.replace('$', ''))

    def get_product_title(self):
        self.product_title = self.soup.find('span', id='productTitle').text.strip("        ")

    def update_preferred_price(self, new_price):
        self.preferred_price = float(new_price)

    # Used to determine if products current price is less than, or equal to, preferred price
    def compare_prices(self):
        product_price_dropped = False

        if self.product_price > self.preferred_price:
            print(f"Product priced over ${self.preferred_price}")
        elif self.product_price < self.preferred_price:
            print(f"Product is priced below ${self.preferred_price}, at ${self.product_price}")
            product_price_dropped = True
        elif self.product_price < self.preferred_price:
            print(f"Product is priced exactly at ${self.preferred_price}")
            product_price_dropped = True

        if product_price_dropped:
            print("Emailing user")
            self.email_user_info()

    def email_user_info(self):
        sent_from = self.email_user
        to = self.email_user
        subject = "Amazon Item Price Drop!"
        body = f"{self.product_title} for ${self.product_price}.\n {self.product_url}"
        email_text = """From: %s\n To: %s\nSubject:%s\n%s\n""" % (sent_from, to, subject, body)

        try:
            server = smtplib.SMTP('smtp.gmail.com', port=587)
            server.starttls()
            server.login(self.email_user, self.email_password)
            server.sendmail(from_addr=sent_from, to_addrs=to, msg=email_text.encode('utf-8'))
            server.close()
            print("Successfully sent email")
            print(body)
        except smtplib.SMTPException:
            print("Error: unable to send email")
