
# Token telegran bot
bot_token = '1704242403:AAGLIRz-u1TgfP6NZjn-2VE8T1VdgWKNPsE' # токен бота
CHANNEL_ID = 1385830528 # id канала куда будет отсылаться информация, ид без -100 в начале (например: 124873248) - указать заместо нуля

# ID admin
admin_id = 468853775 # id админа - указать заместо нуля

bot_login = 'reklama_shopbot' # логин бота
ref_percent = 5 # Процент реферальной системы

QIWI_NUMBER = '+998909773089'    # номер киви
QIWI_TOKEN = '658b6c618d2d33cd9ae1f5a0334ad932'            # токен киви

text_purchase = '❕ Вы выбрали: ' \
                '{name}\n\n' \
                '{info}\n\n' \
                '💠 Цена: {price} рублей\n' \
                '💠 Кол-во товара: {amount}' \


# инфа
info = '''❗️ Информация:\n'''

# Пополнение баланса
replenish_balance = '⚠️ Пополнение баланса\n\n' \
                    '🥝 Оплата киви: \n\n' \
                    '👉 Номер  {number}\n' \
                    '👉 Коментарий  {code}\n' \
                    '👉 Сумма  от 1 до 15000 рублей'

# Профиль
profile = '🧾 Профиль\n\n' \
          '❕ Ваш id - {id}\n' \
          '❕ Ваш логин - {login}\n' \
          '❕ Дата регистрации - {data}\n\n' \
          '💰 Ваш баланс - {balance} рублей'
