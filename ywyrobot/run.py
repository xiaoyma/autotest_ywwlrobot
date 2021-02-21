import os,sys,pprint
#print(sys.path)

print('\n根据环境变量Path，使用python解释器: %s\n' % sys.executable)

if sys.version_info.major != 3:
    print("黑羽robot只支持 Python 3 版本")
    exit()

from ywyrobot.core import reportHan,convert2RF,runRF,clearRobotFile
from tools.emailCom import SendEmail

host_all = ''

def main():

    # 运行结果存入字典
    result = {}

    # 只清除所有robot用例文件
    if '--delrf' in sys.argv:
        clearRobotFile()
        exit(0)

    # 只转化Python用例为robotframework格式用例
    if '--torf' in sys.argv:
        convert2RF()
        exit(0)

    # 只运行测试
    if '--runrf' in sys.argv:
        runRF()
        exit(0)        

    # 只汉化测试报告
    if '--hanrf' in sys.argv:
        reportHan()
        exit(0)

    #判断执行测试环境还是正式环境
    global host_all
    if '--TEST' in sys.argv:
        host_all = 'TEST'
        print("指定为测试环境，将执行测试环境的用例")
    elif '--PRD' in sys.argv:
        host_all = 'PRD'
        print("指定为正式环境，将执行正式环境的用例")
    else:
        print('未指定环境，将默认执行正式环境')
        host_all = 'PRD'

    is_send = ''
    if '--Email' in sys.argv:
        is_send = '0'

    # 所有步骤都执行
    convert2RF()

    ret = runRF()    
    print(f'-------- RF execute result code: {ret} --------')
    result['run_robot'] = ret

    # 如果运行成功，执行汉化
    if ret < 5: # 0 success, 1 faiure, 252 no matches found
        reportHan()
        os.system('log.html')

    # 发送测试报告邮件
    if is_send == '0':
        email_ret = SendEmail().send_mail()
        result['email'] = email_ret
    return result

if __name__ == '__main__':
    result = main()