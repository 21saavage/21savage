Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
Traceback (most recent call last):
  File "/home/ec2017b210/sendingstuff.py", line 3, in <module>
    import smtplib
  File "/usr/lib/python3.6/smtplib.py", line 47, in <module>
    import email.utils
  File "/home/ec2017b210/email.py", line 5, in <module>
    s = smtplib.SMTP('smtp.gmail.com', 587)
AttributeError: module 'smtplib' has no attribute 'SMTP'
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
Traceback (most recent call last):
  File "/home/ec2017b210/sendingstuff.py", line 3, in <module>
    import smtplib
  File "/usr/lib/python3.6/smtplib.py", line 47, in <module>
    import email.utils
  File "/home/ec2017b210/email.py", line 5, in <module>
    s = smtplib.SMTP('smtp.gmail.com', 587)
AttributeError: module 'smtplib' has no attribute 'SMTP'
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
Traceback (most recent call last):
  File "/home/ec2017b210/sendingstuff.py", line 12, in <module>
    s.login("pravesh368@gmail.com", "back@street")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbu-\n5.7.14 zHEp9kpaKX-hleOCNsStAkVItSpdTa7SNxtNXxAa4LR4Kq0QFOd-EyeXHhsD_2z2lZV0b1\n5.7.14 OEc6ny3eF_6pQBb0AGo1JusZqnzliUpGZw8j28UBE-pai2JoBQL2tGjn1Eb5e4nu6rMnPd\n5.7.14 BrxWQPVHzK2s0Mcdd037rexFHg9dlSMPzkhCqCV5GORw5TeyPjNbu-FQ46apeMwbGF4RAI\n5.7.14 KL7OOgdu1rjdO0HH_siIo4Ai77qZs> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 10sm44725582pfo.69 - gsmtp')
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
Traceback (most recent call last):
  File "/home/ec2017b210/sendingstuff.py", line 12, in <module>
    s.login("pravesh368@gmail.com", "back@street")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbsN\n5.7.14 Uqr1g9SmMNYlvF6p_ODCxO9puIgkDLIgjOJExnpVXC4VZjIhFGOouar2tsWnsPF4RQDUa0\n5.7.14 tfpChKCYgjeEIVEWADjMG7X9lo0CkoXzQLZvho9haDAlH8jKVZpKBGypoQ1WZ-O1DKa2Wr\n5.7.14 Tn5R_k4g8JryhqPqxGJ31oQAZhqlotDisRNxAUISasNbEXanwCHGj_FRexhKgrMLgeWAWx\n5.7.14 QQn9lVdjRWAdcoaO0Y_WQdJP-6Uq4> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 c23sm55382130pfc.172 - gsmtp')
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
Traceback (most recent call last):
  File "/home/ec2017b210/sendingstuff.py", line 12, in <module>
    s.login("pravesh368@gmail.com", "back@street")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbvF\n5.7.14 fMn1XT6NcLu28_BtHrKZ_gHbsDVADBG1R0gbaXLBxC2iEIT3OIdpb2ANcEzVEwvp_Za7ZS\n5.7.14 TWRLlYvVoYLOLEPXPdD-_nf59a0PPu206ONDmIfnSacARjzfCiesH7bYxdCaSSoBCveMqA\n5.7.14 sh462hEqKGtHnH-wky_nq8NJdsJwfGI2l5JDIdwxRVFY3uhOwBW0Vzj_DjbkXYGnnGuzZY\n5.7.14 cJomrK97Kdv83dOZPMZ1O7PhrHTZM> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 t25sm68808020pfk.162 - gsmtp')
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
Traceback (most recent call last):
  File "/home/ec2017b210/sendingstuff.py", line 12, in <module>
    s.login("pravesh368@gmail.com", "Back@street")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials p4sm51103114pgn.81 - gsmtp')
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
Traceback (most recent call last):
  File "/home/ec2017b210/sendingstuff.py", line 12, in <module>
    s.login("pravesh368@gmail.com", "back@street")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbsY\n5.7.14 VNyy62VONbFHnkwqfoJdaEO-4bJyIZ10CuEi9HA6Zrkn0O1Z-c6ibGnDon5QrgvYUjz9Br\n5.7.14 4opTAZl8IvFj3ZCZ8X7GkRs6amN7sLpr135aLQH4NK68zxxzKHgjT3msQjid_YMInlHS4w\n5.7.14 -Ezatbvga3wynNNtOMvy1WSV3d3zP8tK59owW5301DNSX0vNLlc9aQ_xBPp4x_6-h7bkRI\n5.7.14 d6v9lPQYgKim7SCazOhw3-r7Zk5KY> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 h186sm17308599pfg.15 - gsmtp')
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
Traceback (most recent call last):
  File "/home/ec2017b210/sendingstuff.py", line 12, in <module>
    s.login("pravesh368@gmail.com", "back@street")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbuP\n5.7.14 c2xo38QHknkbBAMYuZaBIEztncwt6ZRqVhZTIQkT_lQ9vfkwTzqMnOXpiqgHNaW_6rk47N\n5.7.14 _TQZZPCAHsv09ZShUw5TYnGvV-0AqsHC880QYiuE7xF4QZPOie8HvTXffkrxxPVnRU_aCl\n5.7.14 Sj7qpT3UKXO_7rsaz5wx6lRgk8_nH61CYFwmyhpZZB-KF5NfNU_Uv-D1pCQse0fCWmdKJp\n5.7.14 b5Lz4xCmNbZ31zG3s90hxBFkVWOYo> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 x86sm62431734pfa.164 - gsmtp')
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
sssuccess
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
sssuccess
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
sssuccess
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
sssuccess
>>> 
================= RESTART: /home/ec2017b210/sendingstuff.py =================
sssuccess
>>> 
=============== RESTART: /home/ec2017b210/rockpaperscisors.py ===============
Traceback (most recent call last):
  File "/home/ec2017b210/rockpaperscisors.py", line 1, in <module>
    Python
NameError: name 'Python' is not defined
>>> 
=============== RESTART: /home/ec2017b210/rockpaperscisors.py ===============
Traceback (most recent call last):
  File "/home/ec2017b210/rockpaperscisors.py", line 1, in <module>
    Python
NameError: name 'Python' is not defined
>>> 
=============== RESTART: /home/ec2017b210/rockpaperscisors.py ===============
Rock, Paper, Scissors?rock
That's not a valid play. Check your spelling!
Rock, Paper, Scissors?Rock
You win! Rock smashes Scissors
Rock, Paper, Scissors?rock
That's not a valid play. Check your spelling!
Rock, Paper, Scissors?
=============== RESTART: /home/ec2017b210/rockpaperscisors.py ===============
Rock, Paper, Scissors?
=============== RESTART: /home/ec2017b210/rockpaperscisors.py ===============
Rock, Paper, Scissors?
