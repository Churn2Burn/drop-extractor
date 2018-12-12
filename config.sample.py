import os
directory = os.path.dirname(os.path.abspath(__file__))
file = "chromedriver.exe"

CHROMEDRIVER_PATH = os.path.join(directory, file)

IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993
IMAP_SSL = True
IMAP_USERNAME = ''
IMAP_PASSWORD = ''

FOLDER = ''

FROM_EMAIL = 'rewards@notifications.earnwithdrop.com'
API_Key = ''

card_amount = '//*[@id="top-content2"]/h2[2]'
card_number = '//*[@id="top-content2"]/p'