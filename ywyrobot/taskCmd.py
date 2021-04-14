import subprocess
from Framwork.taskSDK import taskResult

class CMD():
    '''注意：此模块需要在项目中任意py文件from com.route.job.taskDemo import taskDemo，否则SDK动态动态初始化对象会报错'''

    def cmd_run(self, **kwargs):
        '''
        接入SDK的函数，在任务调度平台，保存以下信息：
        {
            "classfile": "com.route.job.taskDemo", #目录
            "className": "taskDemo", #类名
            "funcName": "insideDemo", #方法名
            "param": {"len": "10"} #方法传参
            "actionId": "23232323" #任务日志ID,自动生成传入
        }
        '''
        actionId = kwargs['actionId']
        params = kwargs['params']
        cmd1 = "git pull"
        cmd2 = params
        result = ""
        (status, output) = subprocess.getstatusoutput(cmd1)
        if status == 0:
            result = result + "git pull执行成功：\n" + str(output)
        else:
            result = result + "git pull执行失败：\n" + str(output)
        # (status, output) = subprocess.getstatusoutput(cmd2)
        # if status == 0:
        #     result = result + "\n" + cmd2 + "执行成功：\n" + str(output)
        # else:
        #     result = result + "\n" + cmd2 + "执行失败：\n" + str(output)
        p = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = result + "\n" + cmd2 + "执行结果：\n"
        for line in p.stdout.readlines():
            print(line)
        retval = p.wait()
        if retval == 0:
            result = result + "执行成功"
        else:
            result = result + "执行失败"
        print(result)
        # 调用taskSDK的respResult方法，将执行结果传过去
        sdk = taskResult()
        ret = sdk.respResult(actionId, result)
        return "执行完毕"

