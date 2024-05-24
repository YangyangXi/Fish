import csv

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

# 测试读取CSV文件
file_path = 'emails.csv'  # 替换成你的CSV文件路径
emails = read_emails_from_csv(file_path)
print(emails)