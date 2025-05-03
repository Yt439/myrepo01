import smtplib
from email.message import EmailMessage
#无需安装第三方库
key = 'tihlcqmbzmcldjic'      #换成你的QQ邮箱SMTP的授权码(QQ邮箱设置里)
EMAIL_ADDRESS = '2399426512@qq.com'      #换成你的邮箱地址
EMAIL_PASSWORD = key


smtp=smtplib.SMTP('smtp.qq.com', 25)

import ssl
context=ssl.create_default_context()
sender=EMAIL_ADDRESS



def sendemial(emial, content):
    subject = "提醒上线"
    body = content
    msg = EmailMessage()
    msg['subject'] = subject  # 邮件主题
    msg['From'] = sender
    msg['To'] = emial
    msg.set_content(body)  # 邮件内容

    with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as smtp:
        smtp.set_debuglevel(1)
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        try:
            smtp.quit()
        except smtplib.SMTPResponseException as e:
            print("忽略退出异常：", e)


if __name__ == '__main__':

    sendemial(emial='3289554185@qq.com',content='测试上线')