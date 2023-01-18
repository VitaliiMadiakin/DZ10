# Сперва импортируем Flask и функцию считывания данных из JSON-файла
from flask import Flask
from utils import load_data

# Затем создадим экземпляр этого Flask, назовем его app -
# это будет наше приложение

app = Flask(__name__)


# Что такое __name__ ?
# При запуске сценария значение переменной __name__ равно __main__
# Эта переменная помогает Flask разбираться, где он находится
# и без нее он просто не заработает

# Функция печатает всех пользователей в запрошенном форматировании


def page_index():
    user_data = ''
    for data in load_data():
        user_data += f"Имя кандидата - {data['name']}\n" \
                     f"Позиция кандидата - {data['position']}\n" \
                     f"{data['skills']}\n" \
                     f"\n"
    return f'<pre>{user_data}</pre>'


# Функция выводит пользователя по запрошенному ID

def page_candidate(x):
    candidate_picture = ''
    candidate_data = ''
    for data in load_data():
        if int(x) == data['id']:
            candidate_picture += f"<img src={data['picture']}>"
            candidate_data += f"Имя кандидата - {data['name']}\n" \
                              f"Позиция кандидата - {data['position']}\n" \
                              f"{data['skills']}\n" \
                              f"\n"
            return f'{candidate_picture}\n <pre>{candidate_data}</pre>'
    return "Нет пользователя с таким ID"


# Функция выводит пользователя по запрошенному скилу

def page_skills(x):
    skills_data = ''
    for data in load_data():
        if x.lower() in data['skills'].lower():
            skills_data += f"Имя кандидата - {data['name']}\n" \
                           f"Позиция кандидата - {data['position']}\n" \
                           f"{data['skills']}\n" \
                           f"\n"
    if len(skills_data) > 0:
        return f'<pre>{skills_data}</pre>'
    return "Нет пользователя с таким скилом"


# Теперь используем методы у приложения, которые зарегистрируют маршрут

app.add_url_rule('/', view_func=page_index)
app.add_url_rule('/candidate/<x>', view_func=page_candidate)
app.add_url_rule('/skill/<x>', view_func=page_skills)

# Теперь стартуем сервер, чтобы обрабатывать запросы от пользователей

app.run()
