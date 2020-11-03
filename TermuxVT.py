import requests
import time

likePROFILE = 'https://vimetop.ru/ajax/player/likeProfile.php'
urlSTATUS = 'https://vimetop.ru/ajax/player/statusChange.php'

accounts = [
{'nickname': 'ssd', 'hash': '1c0e4761a1b8b8c6c71879e61cfd09035fa183abc55cd16044205235fa183abc55d0c58eba83e76db372493c31066d82ca3c'},
            ]

text = input('Статус: ')
for i in accounts:
    s = requests.Session()
    s.headers.update({"accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7","content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-requested-with": "XMLHttpRequest","cookie": "nickname=" + i['nickname'] + "; auth_hash=" + i['hash']})
while True:
    time.sleep(10)
    data = {'text':text}
    r = s.post(urlSTATUS, data=data)
    print(r.text)
