
# 成功状态码
OK = 200

# 登录的状态码
DATA_NOT_COMPLETE = {'code': 1001, 'msg': '内容不完全'}
PHONE_ERROR = {'code': 1002, 'msg': '手机号码格式错误'}
USERNAME_FORMAT_ERROR = {'code': 1003, 'msg': '用户名格式错误'}
USER_EXISTS = {'code': 1004, 'msg': '用户已存在'}
PASSWORD_FORMAT_ERROR = {'code': 1005, 'msg': '密码格式不正确'}

PASSWORD_NOT_SAME = {'code': 1006, 'msg': '密码输入不一致'}

USER_NOT_EXISTS = {'code': 1007, 'msg': '该用户不存在'}
USERNAME_OR_PASSWORD_ERROR = {'code': 1008, 'msg': '用户名或密码错误'}

USER_NOT_LOGIN = {'code': 1009, 'msg': '用户未登录'}


# 个人中心
THE_SAME_PASSWORD = {'code': 1010, 'msg': '新密码与旧密码不能一致'}

