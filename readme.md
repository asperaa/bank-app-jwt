## JWT-Based Authentication for RESTFul APIs
#### django-rest-framework-simplejwt - A JSON Web Token authentication plugin for the Django REST Framework.

simplejwt plugin is being used to authenticate the APIs.

The cURL scripts are as follows - 

GET request to get the bank/branch details for a given IFSC code
<pre>
curl -X GET \
  'http://localhost:8000/api/bank_detail/?limit=7&offset=0&ifsc=YESB0GSB001' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYyNzU4Mjk1LCJqdGkiOiJmY2U3YWI0N2QyNzg0OWQ5OTc2ZWMwMGNiMmU1YmYyNCIsInVzZXJfaWQiOjF9.hOj8-MfE0TJ8P4OCgWBWdQ0wQyAlty5klQ4GU5WucoY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: 658baeba-1b37-4c5d-91a7-49b100175cb0' \
  -H 'cache-control: no-cache'
</pre>

GET request to get the details of various branches for given bank and city
<pre>
curl -X GET \
  'http://localhost:8000/api/branch_detail/?limit=7&offset=4&name=YES%20BANK&city=NAGPUR' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYyNzU4Mjk1LCJqdGkiOiJmY2U3YWI0N2QyNzg0OWQ5OTc2ZWMwMGNiMmU1YmYyNCIsInVzZXJfaWQiOjF9.hOj8-MfE0TJ8P4OCgWBWdQ0wQyAlty5klQ4GU5WucoY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: 55c06a7b-7f4f-4b84-8b75-603edb96e06b' \
  -H 'cache-control: no-cache'
</pre>

Note: You can execute .sh file for each of the above cURL scripts which are present in bank/bank_details.sh and bank/branch_details.sh .