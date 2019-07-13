## JWT-Based Authentication for RESTFul APIs
#### django-rest-framework-simplejwt - A JSON Web Token authentication plugin for the Django REST Framework.

django-rest-framework-simplejwt plugin is being used to authenticate the APIs.

The cURL scripts are as follows - 

GET request to get the bank/branch details for a given IFSC code.
<pre>
curl -X GET \
  'http://banking-apps.herokuapp.com/api/branch_detail/?limit=7&offset=4&name=YES%20BANK&city=NAGPUR' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzNDY5MzE4LCJqdGkiOiI2YWNmNzM3Yjc3YTc0NTVlYWU4YTQzMmFjM2ZmMzE2MyIsInVzZXJfaWQiOjF9.CJOjN3AFScxIgzdWdwe4e7ShIsI2KolGpSMLWsxr4hk' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: 55c06a7b-7f4f-4b84-8b75-603edb96e06b' \
  -H 'cache-control: no-cache'
</pre>

GET request to get the details of various branches for given bank and city.
<pre>
curl -X GET \
  'http://banking-apps.herokuapp.com/api/bank_detail/?limit=7&offset=0&ifsc=YESB0GSB001' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzNDY5MzE4LCJqdGkiOiI2YWNmNzM3Yjc3YTc0NTVlYWU4YTQzMmFjM2ZmMzE2MyIsInVzZXJfaWQiOjF9.CJOjN3AFScxIgzdWdwe4e7ShIsI2KolGpSMLWsxr4hk' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: 658baeba-1b37-4c5d-91a7-49b100175cb0' \
  -H 'cache-control: no-cache'
</pre>

Note: You can execute .sh file for each of the above cURL scripts which are present in bank/bank_details.sh and bank/branch_details.sh .
