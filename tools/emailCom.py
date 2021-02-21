# # encoding: utf-8
import time
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os.path
import re
from bs4 import BeautifulSoup


class SendEmail(object):
    def __init__(self):
        self.log_path = self.get_log_path('log.html')
        self.report_path = self.get_log_path('report.html')
        self.head = '''
        <head><style type="text/css">
        .report_style{margin:20px 10%}        
        .header{text-align:center;width:100%;font-family:"Times New Roman"}    
        .report_table {text-align:center; width:100%; font-family:"Times New Roman"}        
        .report_table_title  {height:40px; text-align:center; width:100%; font-weight: bold; font-size:24px} 

        .report_table_content {background-color:#99CCFF; width:27%; text-align:center; padding:0 10px;} 
        .report_table_total {background-color:#CCFFFF; width:18%; text-align:center; padding:0 10px;}
        .table_content_success {background-color: #6bff8f; width:16%; text-align:center; padding:0 10px;}        
        .table_content_fail {background-color: #ff6c6d; width:15%; text-align:center; padding:0 10px;}
        .table_elapsed_time {background-color:#99CCFF; width:24%; text-align:center; padding:0 10px;}
        .table_head {background-color: #66CCFF; text-align:center; font-weight:bold; padding:0 10px;} 
        .table_path {background-color:#FFCC99; width:0%; text-align:center; padding:0 10px;}
        </style></head> 
         <div class="header"><h1>自动化测试报告</h1></div>
         <div class="header"><h4>PS:详情附件不支持预览，请下载后查看</h4></div>
        '''

        self.table_head = '''<div class="report_style"><table class="report_table">
        <tr><th colspan="6" class="report_table_title">table_title_name</th></tr>
        <br>
        <tr><td class="table_head">name</td><td class="table_head">Total</td><td class="table_head">Pass</td><td class="table_head">Fail</td><td class="table_head">Elapsed Time</td></tr>
        '''
        self.table_content = '<tr><td class="report_table_content">replace0</td><td class="report_table_total">replace1</td><td class="table_content_success">replace2</td><td class="table_content_fail">replace3</td><td class="table_elapsed_time">replace4</td></tr>'

    def set_value_to_html(self):
        """
        组装新的html格式文件
        :return:
        """
        content_dict = self.get_value_from_html()
        table_tile = ['全局统计', '根据标签统计', '根据套件统计']
        table_head_html = ''
        for a in range(len(content_dict)):
            table_dict = content_dict[a]
            table_head_html = table_head_html + '\r\n' + self.table_head.replace('table_title_name', table_tile[a])
            table_content_html = ''
            for b in range(len(table_dict)):
                table_content_html = table_content_html + '\r\n' + self.table_content
                # print(table_dict[b])
                name = table_dict[b]['label']
                total_num = table_dict[b]['pass'] + table_dict[b]['fail']
                pass_num = table_dict[b]['pass']
                fail_num = table_dict[b]['fail']
                elapsed_time = table_dict[b]['elapsed']
                table_list = [name, str(total_num), str(pass_num), str(fail_num), elapsed_time]
                # print(table_list)

                for c in range(5):
                    table_content_html = table_content_html.replace('replace' + str(c), table_list[c])
                # print(table_content_html)
            table_head_html = table_head_html + '\r\n' + table_content_html + '</table></div>'

        all_html = self.head + table_head_html
        return all_html

    def get_log_path(self, file_name):
        """
        获取log.html文件的路径
        :param file_name: 文件名
        :return:
        """
        # current_path = os.getcwd()
        current_path = os.path.dirname(os.path.abspath(__file__))
        current_path = current_path.split(r"\tools")[0]
        # current_path = r"D:\Project\autotest_ywwlrobot"
        # join_path = os.path.join(current_path, '../..')
        # above_path = os.path.abspath(join_path)
        config_path = os.path.join(current_path, file_name)
        return config_path

    def get_value_from_html(self):
        """
        读取log.html，使用正则获得所需数据内容
        :return:
        """
        soup = BeautifulSoup(open(self.log_path, 'rb+'), "html.parser")
        content = re.findall(r'stats\"] = (.+);', soup.decode())
        content_dict = eval(content[0])
        return content_dict

    def send_mail(self):
        """
        使用163邮箱发送邮件，具体方法可自行百度
        :return:
        """
        log_path = self.log_path
        report_path = self.report_path

        mail_host = "smtp.exmail.qq.com"
        mail_user = 'maxiao@ywwl.com'
        mail_pass = "Qq542085264"  # 不是用户名对应的密码，而是163给的授权码
        sender = "maxiao@ywwl.com"  # 发件人

        # receivers = ['gylxmz@ywwl.com', 'sunqin@ywwl.com', 'xiyao@ywwl.com']  # 收件人
        receivers = ['maxiao@ywwl.com']  # 收件人
        mail_postfix = "qq.com"
        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        detail_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
        send_header = "SRM供应商-自动化测试报告 " + today + " " + detail_time  # 邮件标题
        msg = MIMEMultipart()
        msg['Subject'] = send_header
        msg['From'] = sender
        msg['To'] = ",".join(receivers)
        # 发送html格式正文
        content = self.set_value_to_html()
        msg.attach(MIMEText(content, _subtype='html', _charset='utf-8'))
        # 发送log.html附件
        log_file = MIMEApplication(open(log_path, 'rb').read())
        log_file.add_header('Content-Disposition', 'attachment', filename='log.html')
        msg.attach(log_file)
        # 发送report.html附件
        report_file = MIMEApplication(open(report_path, 'rb').read())
        report_file.add_header('Content-Disposition', 'attachment', filename='report.html')
        msg.attach(report_file)

        try:
            server = smtplib.SMTP_SSL(mail_host, 465)
            server.login(sender, mail_pass)
            server.sendmail(sender, receivers, msg.as_string())
            server.close()
            print('邮件发送成功')
            return True
        except Exception as e:
            print('邮件发送失败', str(e))
            return False


if __name__ == '__main__':
    test = SendEmail()
    # test.get_log_path()
    test.send_mail()