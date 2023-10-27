# Entity
Company
Employee
with one to many relationship

# End Points
/companies                  GET         get all companies
/companies/{id}             GET         get company by id
/companies/{id}             PUT         update company by id
/companies/{id}             DELETE      delete company by id
/companies                  POST        add new company
/companies/{id}/employees   GET         get all employees of company

same for employee

# Steps involved
1. install Django and DRF(Django Rest Framework)
2. setup modal setup in django
3. setup serializers
4. setup views
5. setup urls
6. Test API