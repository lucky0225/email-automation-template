import smtplib

sender_email = ""
receiver_email = ""
password = ""
message = ""

# varies depending on your email provider
server = smtplib.SMTP("smtp.gmail.com", 587)
# connecting to the server of your email provider
server.starttls()
server.login(sender_email, password)
print("Login successful")

server.sendmail(sender_email, receiver_email, message)
print("You email has successfully been sent to: ", receiver_email)

# notice: "Exception has occurred: SMTPAuthenticationError 535, b'5.7.8 Username and Password not accepted"
# problem with the security settings (e.g. 2-fa, accepting unsecure apps for login, etc.) of your googlemail account, etc.
