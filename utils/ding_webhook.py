import requests
import json


def webhook_dingding(message):
    # 钉钉机器人Webhook URL
    webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=65d54ed9f20a4ea01c7fc02bda39a21a49bccbe746b20be9a074d281b0828167"

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
