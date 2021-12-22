import smtplib, ssl
import loguru


class MAilDeco:
    # loguru.logger.remove()
    # @loguru.logger.catch()
    def __init__(self,host,port,username,password,from_addr,to_addr,subject):
        self.subject=subject
        self.from_addr=from_addr
        self.to_addr=to_addr
        # loguru.logger.add(self.send_email)
        self.server=smtplib.SMTP_SSL(host=host,port=port)
        self.server.set_debuglevel(1)
        self.server.connect(host,port)
        self.server.login("bokon2014@yandex.ru","ohtzcwosnfwttfzj")


    def EDeco(self,function_to_decorate):
        def the_wrapper(*args,**kwargs):
            with loguru.logger.catch():
                function_to_decorate(*args,**kwargs)
        return the_wrapper

    def send_email(self,body_text):
        BODY = "\r\n".join((
            f"From: {self.from_addr}" ,
            f"To: {self.to_addr}",
            f"Subject: {self.subject}",
            f"{body_text}",
        ))

        self.server.sendmail(self.from_addr, [self.to_addr], BODY.encode("utf-8"))

    def __del__(self):
        pass
        # self.server.quit()


if __name__ == "__main__":
    host = "smtp.yandex.ru"
    password="ohtzcwosnfwttfzj"
    port = 465
    subject = "Test email from Python"
    to_addr = "vrktorbom@gmail.com"
    from_addr= "bokon2014@yandex.ru"

    m=MAilDeco(host,port,from_addr,password,from_addr,to_addr,subject)
