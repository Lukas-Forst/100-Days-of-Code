import yagmail

yag = yagmail.SMTP('*', '*')

to = 'kanuspeter@gmail.com'
subject = 'This is obviously the subject'
body = 'This is obviously the body'
html = '<a href="https://pypi.python.org/pypi/sky/">Click me!</a>'
img = 'foo.png'

yag.send(to = to, subject = subject, contents = [body, html, img])