# auth-simple



## Login
```
curl --location --request POST 'http://localhost:5000/api/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "zungx",
    "password": "123456"
}'
```

