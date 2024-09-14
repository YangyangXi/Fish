import pandas as pd
import numpy as np
import random
import string

# 生成随机字母列
def random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))

# 生成数据
num_rows = 60000
data = {
    'Number': np.random.randint(1, 100000, num_rows),
    'Letters': [random_string(5) for _ in range(num_rows)]
}

# 创建DataFrame并保存到Excel
df = pd.DataFrame(data)
df.to_excel('6000条数据.xlsx', index=False)
