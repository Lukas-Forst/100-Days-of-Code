from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
import ssl
to = 'kanuspeter@gmail.com'
subject = 'This is obviously the subject'
body = 'This is obviously the body'
html = '<a href="https://pypi.python.org/pypi/sky/">Click me!</a>'
img = 'foo.png'


ctx = ssl.create_default_context()
password = "knavxlfjoxzeamuy"    # Your app password goes here
sender = "kanuspeter@gmail.com"    # Your e-mail address
receiver = "kanuspeter@gmail.com" # Recipient's address
message = MIMEMultipart("alternative")
message["Subject"] = "Hello Multipart World!"
message["From"] = sender
message["To"] = receiver
html = open("template.html")

"""
html = \
<html>
  <body>
    <p>
        <i>Hello</i>
        <u>from</u>
        <b>Python</b>.
    </p>
    <p>
        Try out the APIs at
        <a href="https://www.abstractapi.com/">Abstract API</a>.
        <img src="cid:image1">
    </p>
  </body>
</html>
"""

plain = """\
Hello from Python.
Try out the APIs at Abstract API.
"""
#fp = open('foo.png', 'rb') #Read image
#msgImage = MIMEImage(fp.read())
#fp.close()

# Define the image's ID as referenced above
#msgImage.add_header('Content-ID', '<image1>')
#message.attach(msgImage)

#message.attach(MIMEText(plain, "plain"))
message.attach(MIMEText(html.read(), "html"))
with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
    server.login(sender, password)
    server.send_message(message,from_addr=sender, to_addrs=receiver )
