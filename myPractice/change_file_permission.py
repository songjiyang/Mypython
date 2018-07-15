vim
vi
%run ls.py
ls -l
import os, stat
os.listdir('.')
s = 'g.sh'
s.endswith('.sh')
s.endswith('.py')
s.endswith?
s.endswith(('.sh','.py'))
s.endswith(['.sh','.py'])
[for name in os.listdir('.') if name.endswith(('.sh',',py'))]
[name for name in os.listdir('.') if name.endswith(('.sh','.py'))]
os.sta
os.sta?
os.sta
os.stat
os.stat('List_util.py')
os.stat('List_util.py').st_mode
oct(os.stat('List_util.py').st_mode)
oct?
stat.S_IXUSR
 ls -l
os.chmod('List_util.py',os.stat('List_util.py').st_mode | stat.S_IXUSR)
ls -l
pwd
%hist -f mySplitAndChmod
