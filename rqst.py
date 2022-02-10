import requests


def status_check_address(address):
    print(address)
    url = "https://tools.usps.com/tools/app/ziplookup/zipByAddress"
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'User-Agent': 'Mozilla/'
                    '5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/'
                    '537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
      'Accept': 'application/json',
      'Cookie': 'TLTSID=40c81afa3815161e900100e0ed96ae55; '
                'NSC_uppmt-usvf-ofx=ffffffff3b462a2345525d5f4f58455e445a4a4212d3'
    }
    response = requests.post(url, headers=headers, data=address)
    data = response.json()
    print(data['resultStatus'])
    return data['resultStatus']

