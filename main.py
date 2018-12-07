import requests
phone = '89992223456'

def pizzalarenzo(phone):
    headers = {
        'name':'%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone': phone,
        'time':'%D0%91%D0%BB%D0%B8%D0%B6%D0%B0%D0%B9%D1%88%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F'
    }
    response_pizzalarenzo = requests.post(url='https://pizzalarenzo.ru/api/callback.php', headers=headers)

def tarelochka(phone):
    headers = {
        'url':'tarelochcka-2016%40yandex.ru',
        'name_1':'%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone_1': phone

    }
    response_tarelochka = requests.post(url='https://xn--80achdsmuvm0h.xn--p1ai/send/send_1.php', headers=headers)

def pizzapan(phone):
    headers = {
        'name':'%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'mytel': phone

    }
    response_pizzapan = requests.post(url='http://pizzapan.ru/send2.php', headers=headers)
    print(response_pizzapan)

def dostaevsky():
    headers = {
        'phone':'+7 999 233-23-43'
    }
    response_dostaevsky = requests.post(url='https://msk.dostaevsky.ru/ajax/feedback/back_call.php', headers=headers)
    print(response_dostaevsky)

# pizzalarenzo(phone)
# tarelochka(phone)
# pizzapan(phone)
dostaevsky()