# Test_job_ixvan

auth/users/ - Регистрация пользовтаеля(POST)

Параметры:
Username
Password

auth/jwt/create - Получение токена(POST)

Параметры:
Username
Password

api/accounts/profile/ - Информация об аккаунте(GET)(Bearer Token)

api/accounts/profile/category/add (POST)(Bearer Token)

Параметры:
name

api/accounts/profile/category/update/(PATH)(Bearer Token)

Параметры:
name
id

api/accounts/profile/category/delate/(DEL)(Bearer Token)

Параметры:
id

api/accounts/profile/transactions/(GET)

api/accounts/profile/transactions/accrual(POST)(ADD)

Параметры:
amount - cумму
category - категория(id)
organization - организация
description - описание

api/accounts/profile/transactions/writeoff(POST)(del)
Параметры:
amount - cумму
category - категория(id)
organization - организация
description - описание
