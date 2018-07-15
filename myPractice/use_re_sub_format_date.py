log = open('/var/log/dpkg.log'
)
import re
re.sub?
re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)
log
log.read()
log.read()
log.seek(0)
log = log.read()
log
re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)
print re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)
print re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',log)
%hist
%hist -f use_re_sub_format_date.py
