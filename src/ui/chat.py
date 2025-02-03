# チャット画面
# Sociaにおいてメイン画面となる
import flet

def main(page: flet.Page):
    page.title = "Socia"
    is_bot_generating_response = False

    # 送信ボタンがクリックされたときの処理
    def send_button_click(e):
        if is_bot_generating_response:
            return
        chat_history.controls.append(flet.Text("You: " + input_field.value))
        input_field.value = ""
        page.update()

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