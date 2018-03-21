import requests
from random import getrandbits
url = 'https://www.soleheaven.com/pages/wotherspoon-raffle'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say  
def main(limit):
    for i in range(1, limit+1):
        num = getrandbits(40)
        email = 'your_email+{}@gmail.com'.format(num) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'id': '40e2ef-33312',
            'type': 'full',
            'refer_source': '',
            'entry_source': https://www.soleheaven.com/pages/wotherspoon-raffle
            'email': email,
            'email_again': '',
            '23202_1521393710': 'UKyoursize' # put size here ie UK9 or UK9.5 do not remove UK
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    x = int(raw_input("How many entries do you want: "))
    main(x)


# this is a modification of github user yousefissa's needsupply raffle script
# not my original creation therefore do not take full credit for it
