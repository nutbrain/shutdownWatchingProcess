import psutil,os,time
def isExisting(procname):
    procs=list({p.pid:p.info for p in psutil.process_iter(['name'])}.values())
    ps=list(filter(lambda p:p['name']==procname,procs))
    return len(ps)>0
n=0
while isExisting('HandBrakeCLI.exe'):
    print('converting:%d'%(n))
    n=n+1
    time.sleep(60)
os.system('shutdown -s -t 600')
