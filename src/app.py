# エントリーポイント
# このファイルを実行することで、アプリケーションが起動する
from src.ui import chatui
import flet

def main():
    flet.app(target=chatui.main)