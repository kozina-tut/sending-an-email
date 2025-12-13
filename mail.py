import os
from dotenv import load_dotenv
load_dotenv()

import smtplib

letter = f"""From: {os.environ['HIDDEN-LOGIN']}
To: {os.environ['HIDDEN-LOGIN']}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";"""


text = """

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное 
время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить 
на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить 
уведомление о релизе сразу на имейл."""
text = text.replace("%friend_name%", "Гильермо")
text = text.replace("%my_name%", "Владос")
text = text.replace("%website%", "https://dvmn.org/profession-ref-program/kukarachae/kyV0o/")


letter_text = (letter + text)
letter_text = letter_text.encode("UTF-8")


login = os.environ['HIDDEN-LOGIN']
password = os.environ['HIDDEN-PASSWORD']
email_from = os.environ['HIDDEN-LOGIN']
email_to = os.environ['HIDDEN-LOGIN']
message = letter_text


server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail(email_from, email_to, message)                                                                                            
server.quit()


