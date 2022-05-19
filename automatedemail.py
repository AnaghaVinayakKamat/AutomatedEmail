import smtplib as s
ob = s.SMTP("smtp.gmail.com", 587)
ob.starttls()
ob.login("sender@gmail.com", "password")
subject = "sending email using python"
body = "I sent you email via python. Reply to my email saying very good. Additional praises are whole heartedly welcomed."
message = "Subject:{}\n\n{}".format(subject, body)
listofadresses = ["receiver1.com", "receiver2@gmail.com"]
ob.sendmail("sender@gmail.com", listofadresses, message)
print ("email sent successfully")
ob.quit()
