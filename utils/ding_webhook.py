import requests
import json


def webhook_dingding(message):
    # 钉钉机器人Webhook URL
    webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=68d863053791195253f49bbea50fb4d698a2624000da64d662f630420b01db47"

    # 要发送的消息内容
    message = {
        "msgtype": "text",
        "text": {
            "content": "test结果："
        }
    }

    # 发送POST请求到钉钉机器人Webhook URL
    response = requests.post(webhook_url, json.dumps(message), headers={"Content-Type": "application/json"})
    return response.status_code
