import time
import random


def generate_random_number():  # 随机数生成工具
    # 生成一个范围在100到999之间的随机整数
    random_number = random.randint(100000, 999999)
    return random_number


def generate_order_number():  # 批号生成工具
    # 获取当前时间
    current_time = time.localtime()

    # 格式化为 YYYYMMDD
    date_str = time.strftime("%Y%m%d", current_time)

    # 生成一个序列号（这里假设为001，可以根据需要修改）
    sequence_number = "001"

    # 拼接成最终的订单号
    order_number = f"{date_str}{sequence_number}"

    return order_number


def create_date_time():  # 时间生成工具
    from datetime import datetime, timedelta

    # 获取今天的日期
    today = datetime.now()

    # 获取明天的日期
    tomorrow = today + timedelta(days=1)

    # 格式化日期为 YYYY-MM-DD
    today_str = today.strftime('%Y-%m-%d')
    tomorrow_str = tomorrow.strftime('%Y-%m-%d')
    return {"today_str": today_str, "tomorrow_str": tomorrow_str}
