import smtplib, ssl


def contact(message):
    host = "smtp.gmail.com"
    port = 465

    username = "helloworld21895@gmail.com"
    password = "btgovgxrmcrivugg"

    receiver = "helloworld21895@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

if __name__ == "__main__":
    send_email()