apk_path = "/Users/shiwenbin/Downloads/app-global-debug.apk"  # apk环境
# apk_path = "/Users/shiwenbin/Downloads/app-oem-release.apk"  # apk环境
max_number = 3  # 最大重试次数
userID = '1503593264@qq.com'  # 国际EN账号
# userID = '19970246880'
userPassword = '123456'  # 密码
# PeopleID = 12104  # 好友ID
PeopleID = 39784  # 好友ID 国际测试环境 lzc
# PeopleID = 12104  # 好友ID
# PeopleID = 12104  # 好友ID
# PeopleID = 12104  # 好友ID
# PeopleID = 12104  # 好友ID
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'test01',
    # 国际版APP
    'newCommandTimeout': 6000,
    # 更换底层驱动
    'automationName': 'UiAutomator2',
    'noReset': False,
    'autoGrantPermissions': True
    # 'unicodeKeyboard': False,  # 修改手机的输入法
    # 'resetKeyboard': False
}

# TODO IOS部分配置需加判断，对安卓与IOS需分离元素，逻辑可大同小异
