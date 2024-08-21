import smtplib
from email.mime.text import MIMEText
from email.header import Header
import csv

# 发送者邮件
sender = '1459772368@qq.com'
# 在邮箱网站申请授权码，不是自己的登录密码
secret = 'pllevfltdijzbabd'


def send(receiver, title, content):
    smtpObj = smtplib.SMTP('smtp.qq.com', 25)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender, secret)
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = sender  # 设置邮件的发送者
    message['To'] = receiver  # 设置邮件的接收者
    message['Subject'] = Header(title, 'utf-8')  # 设置邮件标题
    smtpObj.sendmail(sender, receiver, message.as_string())
    smtpObj.quit()


def read_emails_from_csv(file_path):
    emails = []
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # 检查是否缺少必要信息
            if 'receiver_email' not in row or 'email_title' not in row or 'email_content' not in row:
                # 如果缺少必要信息，跳过该行并打印警告信息
                print("Warning: Missing necessary information in row, skipping:", row)
                continue
            receiver = row['receiver_email']
            title = row['email_title']
            content = row['email_content']
            emails.append((receiver, title, content))
    return emails


if __name__ == '__main__':
    # 从CSV文件中读取邮件列表
    emails = read_emails_from_csv('emails.csv')
    # 发送邮件
    for email in emails:
        receiver, title, content = email
        send(receiver, title, content)
