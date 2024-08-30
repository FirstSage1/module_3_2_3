# ДЗ модуль 3_2.Способы вызова функций. Задача "рассылка писем".
# ===============================================================
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if ('@' not in recipient or sender) or (recipient.endswith(not (".com", ".ru", ".net")),
                                            sender.endswith(not (".com", ".ru", ".net"))):
        print("Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com")
    elif recipient != sender:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")
    elif ('@' not in recipient or sender) or (recipient.endswith(not (".com", ".ru", ".net"))
                                              or sender.endswith(not (".com", ".ru", ".net"))):
        print("Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student mail.ru")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student_ mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
