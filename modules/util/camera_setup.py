import subprocess
import modules.util.const as const


def get_cameras():
    """CameraFinder.exeを使用して利用可能なカメラのIDと名前を取得する"""
    result = subprocess.run([const.CAMERA_FINDER_PATH], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    cameras = []
    for line in lines:
        if "[" in line and "]" in line:
            idx = line.index("[")
            id_end = line.index("]")
            cam_id = int(line[idx + 1 : id_end])
            cam_name = line[id_end + 2 :].strip()
            cameras.append((cam_id, cam_name))
    return cameras


if __name__ == "__main__":
    print(get_cameras())
