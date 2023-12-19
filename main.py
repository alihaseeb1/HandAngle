import os
import const

from modules.window.main_window import MainWindow


def is_already_running():
    lock_file_path = os.path.join(os.getcwd(), const.LOCK_FILE_NAME)

    # ロックファイルがすでに存在する場合、アプリケーションは既に実行中
    if os.path.exists(lock_file_path):
        return True

    # ロックファイルを作成
    with open(lock_file_path, "w") as lock_file:
        lock_file.write(const.LOCK_FILE_CONTENT)
    return False


def main():
    if is_already_running():
        print(const.ALREADY_RUNNING_MSG)
        return

    app = MainWindow()
    app.mainloop()

    # アプリケーション終了後、ロックファイルを削除
    os.remove(os.path.join(os.getcwd(), const.LOCK_FILE_NAME))


if __name__ == "__main__":
    main()
