
import requests
import robobrowser 

def main():
    # 获取对象
    b = robobrowser.RoboBrowser(parser='lxml')
    # 打开表单的网址
    b.open('http://jxjyxx.xidian.edu.cn/cesp/index_backup.jsp')
    # 获得要提交的哪个表单
    f = b.get_form()
    

    f['loginName'].value='610115199504167264'
    f['loginPassword'].value = '19950416'

    b.submit_form(f)

    print(b.response)

    print(b.parsed)
    # #用户类型
    # f. .value =1
    # # 登录的账号
    # f['login_loginName'].value =610115199504167264
    # # 登录的密码
    # f['loginPassword'].value = '19950416'
    # # 提交表单
    # b.submit_form(f)
    # 获取提交成功后主页的数据

    # for a_tag in b.select('a[href]'):
    #     print(a_tag.attrs['href'])


if __name__ == '__main__':
    main()