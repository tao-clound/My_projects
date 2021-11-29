import jenkins
username = ''
password = ''
# jenkins服务器链接
server = jenkins.Jenkins('http://162.14.75.243:8080/', username=username, password=password, timeout=30)
# 构建job名
job_name = 'secondpipeline'
# 获取所有的job
jobs_list = server.get_all_jobs()
# 判断job是否存在
server.assert_job_exists(job_name)
# 构建job并且传入参数
server.build_job(name=job_name, parameters={'user_name':'auto_tao'})
# 获取构建的number
build_number = server.get_job_info(job_name)['lastCompletedBuild']['number']
# 根据number 和 jobname，获取构建的console
build_res = server.get_build_console_output(name=job_name, number=build_number)

if str(build_res).splitlines()[-1].split(':')[-1].strip() == 'SUCCESS':
    print(job_name,'：构建成功')
else:
    raise Exception('构建失败')