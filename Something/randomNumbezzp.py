import pandas as pd
import numpy as np
import random
import string

# 生成随机字母列
def random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))

# 生成数据
num_rows = 10010
data = {
    'Number': np.random.randint(1, 100000, num_rows),
    'Letters': [random_string(5) for _ in range(num_rows)],
    'Phone': np.random.randint(1, 90000000, num_rows),
    'Adress': [random_string(10) for _ in range(num_rows)],
    'fruits': [random_string(3) for _ in range(num_rows)],
    'blood': [random_string(1) for _ in range(num_rows)],
}

# 创建DataFrame并保存到Excel
df = pd.DataFrame(data)
df.to_excel('10010条数据父对象导入.xlsx', index=False)
