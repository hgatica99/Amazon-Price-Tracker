from price_tracker import AmazonTracker
from bs4 import BeautifulSoup
import os
import pprint

header = ({'Accept-Language': 'en-US,en;q=0.9',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})

product_url = "https://www.amazon.com/Google-Pixel-Pro-Smartphone-Telephoto/dp/B09HYR2NC8/ref=sr_1_2_sspa?keywords=phone&qid=1641865558&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSzVLVVVGR1o1SldEJmVuY3J5cHRlZElkPUEwMTU0Mjk0MlFCQlZBM0dON1VXSCZlbmNyeXB0ZWRBZElkPUEwOTM0NTEzMTRUTlhDUUpENENHMyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

email_user = os.environ.get("USER_EMAIL")
email_password = os.environ.get("USER_EMAIL_PASSWORD")

preferred_price = float(900)

pp = pprint.PrettyPrinter(indent=4)

amazon_tracker = AmazonTracker(preferred_price=preferred_price, my_email=email_user, email_password=email_password,
                               product_url=product_url, header=header)

amazon_tracker.check_product()




