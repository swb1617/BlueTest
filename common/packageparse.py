from androguard.core.bytecodes.apk import APK
from config import apk_path


def get_apkname(apk):
    a = APK(apk, False, "r")
    return a.get_package()


def get_apk_lautc(apk):
    a = APK(apk, False, "r")
    return a.get_main_activity()


if __name__ == '__main__':
    apkname = get_apkname(apk_path)
    apkactivity = get_apk_lautc(apk_path)
    print(apkname)
    print(apkactivity)
