# エントリーポイント
# このファイルを実行することで、アプリケーションが起動する
from ui import chat
import flet

flet.app(target=chat.main)