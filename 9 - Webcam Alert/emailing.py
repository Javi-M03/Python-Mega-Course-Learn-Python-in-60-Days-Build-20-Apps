import smtplib, imghdr
from email.message import  EmailMessage
from credentiales import SENDER,PASSWORD


def send_email(image_path):
    print("Send Email Start")
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer showed up!"
    email_message.set_content("Hey! we just saw a new customer")

    with open(image_path, "rb") as file:
        content = file.read()
    
    email_message.add_attachment(content,maintype='image', subtype=imghdr.what(None,content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)

    #Sender, Reciever, message
    gmail.sendmail(SENDER, SENDER, email_message.as_string())

    print("Send email ended")
if __name__ == "__main__":
    send_email(image_path="images/36.png")