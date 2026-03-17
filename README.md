# csv-upload-api
Django rest api to upload csv

## features
upload CSV file through API
validate name, email, age
store valid records
skip invalid and duplicate records
Return summary of success and failed records

## Validation Rules
name: required
email: must be valid and unique
age: must be between 0 and 120

## API endpoint
POST /api/upload

## How to run
install dependencies: pip install django djangorestframework
run migrations: python manage.py migrate
start server: python manage.py runserver

## Testing
Tested using postman with sample CSV files
Basic unit testing included

## sample csv
name,email,age
sree,sree@example.com,25
