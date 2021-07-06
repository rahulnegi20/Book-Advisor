# Book-Your-Advisor API 

This API allows you to create(for admin)/ book an appointment with Advisor (date-time-string).

Made using : Django Rest Framework 

Hosted on Heroku : 

## Admin Use only

### Register Advisor : 
<br>
 link : https://bookadvisor123.herokuapp.com/admin/advisor/

![img](https://i.imgur.com/JPjZ2SL.png)


## User 

### Register a new user

link : https://bookadvisor123.herokuapp.com/user/register

 > Note : remember your user id 

![img](https://i.imgur.com/9f7Av90.png)

### Login with JWT Authentication method

You can use `mod header` extension to pass the `JWT Token` in headers. [Chrome Extension](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj/related?hl=en)

login with your credentials you will get `referesh` & `access` token, pass access token in mod header and then

![img](https://i.imgur.com/1xnLV4l.png)

### List of Available Advisors 

link : https://bookadvisor123.herokuapp.com/user/user-id/advisor/
 
 > Use your user-id instead of your `user-id` 
  
![img](https://i.imgur.com/1hdONsv.png)
 
 ### Book an appointment
 
 link : https://bookadvisor123.herokuapp.com/user/user-id/advisor/advisor-id
 
 >  Use `advisor-id` of the advisor you want to book for 
 
![img](https://i.imgur.com/Q97qb9W.png)


### Get list of all booked advisors 

link : https://bookadvisor123.herokuapp.com/user/user-id/advisor/booking 


![img](https://i.imgur.com/bliXggi.png)



That's all for now.
