# SMS sender

A simple Tkinter app that uses the Twilio api internally to send messages

# Dependencies
twilio 7.0.0 
PyPi [here](https://pypi.org/project/twilio/)

# Setup

Open up your terminal and paste the following - 

```
git clone https://github.com/fnplus/Python-scripts-collection
cd "Python-scripts-collection/SMS_SENDER"
pip install twilio
```

Now before proceeding any further head to [Twilio](https://www.twilio.com/) and sign up and follow the steps below

-  Navigate to twilio's [console](https://console.twilio.com/)
-  Copy your **ACCOUNT SID** and **AUTH_TOKEN**
-  In API.py paste them like this

```py
#[...]
def Send_msg(body,to,from_num):
    account_sid = "your_account_sid_here"
    auth_token = "your_auth_token_here"
#[...]
```

- Open up **main.py**
- Copy your trial number from twilio's console
- In the *to* entry box paste the number which you had copied
- In the *from* entry box enter the number to which you wanna send the message
- Note - **Make sure you write country code before the numbers -  Ex : +1218400xxxx**
- You're all set now, type the message and press the sent button
