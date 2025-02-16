import flet as ft

class ChatMessage(ft.UserControl):
    def __init__(self, text, is_sender):
        super().__init__()
        self.text = text
        self.is_sender = is_sender

    def build(self):
        md_text = self.text
        msg_container = ft.Container(
            content=ft.Markdown(
                md_text,
                selectable=True,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                md_style_sheet=ft.MarkdownStyleSheet.a_text_style,
            ),
            border_radius=ft.border_radius.all(12),
            padding=ft.padding.all(12),
            bgcolor=ft.colors.BLUE_50 if self.is_sender else ft.colors.GREY_50,
            border=ft.border.all(1, ft.colors.BLACK26),
        )
        if self.is_sender:
            msg_container.alignment = ft.alignment.center_right
        else:
            msg_container.alignment = ft.alignment.center_left
        return msg_container