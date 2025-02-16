# チャットのメッセージを表示するUI部品
import flet

class ChatMessage(flet.UserControl):
    def __init__(self, text, is_sender):
        super().__init__()
        self.text = text
        self.is_sender = is_sender

    def build(self):
        md_text = self.text
        msg_container = flet.Container(
            content=flet.Markdown(
                md_text,
                selectable=True,
                extension_set=flet.MarkdownExtensionSet.GITHUB_WEB,
                md_style_sheet=flet.MarkdownStyleSheet(
                    p_text_style=flet.TextStyle(color=flet.colors.BLACK87, height=1.5),
                )
            ),
            border_radius=flet.border_radius.all(12),
            padding=flet.padding.all(12),
            bgcolor=flet.colors.BLUE_50 if self.is_sender else flet.colors.GREY_50,
            border=flet.border.all(1, flet.colors.BLACK26),
        )
        if self.is_sender:
            msg_container.alignment = flet.alignment.center_right
        else:
            msg_container.alignment = flet.alignment.center_left
        return msg_container