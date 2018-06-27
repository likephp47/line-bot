from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('uamN7aeae6Dta+O+vaU1OB8CBkhkBhKAsY4By3jI+cwQHUgvRzxQdldH4lLKNWJA4h+CkxkXUVx2AALw+vLhI8KpgQTGSkGIIQ0Xs8lpEir83I+GfdrBTRi9UHgktjlgTuxI+J7BuzgAfMjFbystNAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0d0344e9e2891965027c50b4b5cdbd60')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s= '你吃飯了嗎'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=))


if __name__ == "__main__":
    app.run()