import sender_stand_request

response = sender_stand_request.get_users_table()
print(response.status_code)   # какой код вернул сервер
print(response.text)          # что лежит в ответе