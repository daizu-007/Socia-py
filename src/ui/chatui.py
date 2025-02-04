# チャット画面
# Sociaにおいてメイン画面となる
import flet
import os
import sys
sys.path.append(os.pardir)
from ..logic import model

def main(page: flet.Page):
    page.title = "Socia"
    is_bot_generating_response = False
    llm = model.Model()
    chat = []

    # 送信ボタンがクリックされたときの処理
    def send_button_click(e):
        if is_bot_generating_response:
            return
        question = input_field.value
        chat_history.controls.append(flet.Text("You: " + question))
        input_field.value = ""
        page.update()
        llm.add_user_message(chat, question)
        answer = llm.google_chat_completion(chat)
        chat_history.controls.append(flet.Text("Bot: " + answer))
        page.update()
        llm.add_bot_message(chat, answer)

    # ページ要素の定義
    chat_history = flet.ListView(expand=True, auto_scroll=True, spacing=10)
    input_field = flet.TextField(
        autofocus=True,
        shift_enter=True,
        filled=True,
        expand=True,
        hint_text="Type a message...",
        on_submit=send_button_click,
    )
    send_button = flet.IconButton(icon=flet.icons.SEND_ROUNDED, tooltip="send" ,on_click=send_button_click)

    page.add(
        flet.Container(
            content=chat_history,
            expand=True,
            border=flet.border.all(1, flet.Colors.OUTLINE),
            border_radius=5,
            padding=10
        ),
        flet.Row([input_field, send_button]),
    )