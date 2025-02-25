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
            width=None,  # コンテンツに合わせて自動調整
        )
        
        # コンテナをColumnで包み、最大幅を制限し適切な配置にする
        wrapper = flet.Container(
            content=msg_container,
            width=None,  # 子要素のサイズに合わせる
            alignment=flet.alignment.center_right if self.is_sender else flet.alignment.center_left,
            expand=True,  # 親の幅に合わせて拡大
        )
        
        # 横幅制約を設定したColumnで囲む
        constrained_column = flet.Column(
            [wrapper],
            expand=True,  # 親の幅に合わせて拡大
        )
        
        # 全体の幅を制御するRow
        return flet.Row(
            [
                constrained_column
            ],
            alignment=flet.MainAxisAlignment.END if self.is_sender else flet.MainAxisAlignment.START,
            expand=True,
        )