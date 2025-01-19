# send email to user
# vnyu lian cfbk uvew

# send email to user
# pip install secure-smtplib
import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("arpitparekh9@gmail.com","vnyuliancfbkuvew")
message = "hello from python"
s.sendmail("arpitparekh9@gmail.com","darshanrawat016@gmail.com",message)
print("Email has been sent")
s.quit()
