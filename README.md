<htmml>
<p align="center" style = "font-size:30">
  <b> VOUCHER CODES VERIFICATION [DJANGO] </b><br>
  <i> M. Ruben (Last updated: November 2019) </i><br>
  <a href=https://github.com/m-rbn/vouchers_django/blob/master/README.md#apps>[APPS]</a> 
  <a href=https://github.com/m-rbn/vouchers_django/blob/master/README.md#admin-credentials>[CREDENTIALS]</a>
  <a href=https://github.com/m-rbn/vouchers_django/blob/master/README.md#voucher-codes>[CODES]</a> 
  <a href=https://github.com/m-rbn/vouchers_django/blob/master/README.md#requirements>[REQUIREMENTS]</a>
</p>
<hr>
<p>This repository is intended for the documentation of a Django based web app. 
The basic specification for the project is to create a form for entering voucher codes. The site would then inform the user whether the voucher code is valid.
If it is valid, the amount of discount would then be displayed. In addition, each voucher code can only be used for 3 times only.
Using the same code for more than 3 times would result in the voucher code being invalid.</p> 
<hr>
</html>

# APPS
There are two apps in this project which is home and vouchers.

***home***: The home page containing links for admin login and voucher validation.

***vouchers***: A form to query the database for voucher information. Entering a valid voucher code would return voucher information.

# ADMIN CREDENTIALS
Below is the username and password needed to login as admin. Note: *Both are case sensitive.*

***Username***: site-admin 

***Password***: 1234

# VOUCHER CODES 
Below are two existing voucher codes in the database.

***Code***: q1w2e
 
***Discount Rate***: RM10 

***Usage Limit***: 3 times 

<br> 

***Code***: a1s2d 

***Discount Rate***: 10% 

***Usage Limit***: 3 times

# REQUIREMENTS 
Below are the requirements for this Django project: 

Django==2.2.7

pytz==2019.3

sqlparse==0.3.0

This can also be found in requirements.txt located in the vchr_site folder. Install it in your virtual environment using:

```python
pip install -r requirements.txt
```







 













