# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s = smtplib.SMTP("smtp.gmail.com", 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("pravesh368@gmail.com", "topsecret")
 
# message to be sent
message = "gagaland vagabondfughu"
 
# sending the mail
s.sendmail("pravesh368@gmail.com", "paramjeetsingh070@gmail.com", message)
print("sssuccess")
 
# terminating the session
s.quit()
