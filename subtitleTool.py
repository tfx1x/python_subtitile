#!/usr/bin/python
import sys
import time
import datetime
#reload(sys)

# 00:55:27,650 --> 00:55:29,500
def add_time(time_str, dlt):
        t=time.strptime(time_str,"%H:%M:%S")
        d=datetime.datetime(*t[:6]) + datetime.timedelta(seconds = dlt)
        return d.strftime("%H:%M:%S")

def format_timeline(line, dlt):
        start=line.split()[0].split(',')[0]
        end=line.split()[2].split(',')[0]
        return (add_time(start, 5) + " --> " + add_time(end,5))
        
        
print(sys.getdefaultencoding())
new_file=open('/Users/Chao/new.file', 'w',encoding='utf8')
#sys.setdefaultencoding('utf8')
i = 0


with open('/Users/chao/Desktop/American.Crime.Story.S01.720p.HDTV.x264-Scene/American.Crime.Story.S01E01.INTERNAL.720p.HDTV.x264-KILLERS.srt',encoding = 'utf8') as file_object:
        for line in file_object:
                if(line == '\n'):
                        i=0
                else:
                        i+=1
                if(i == 2):      
                        new_file.write(format_timeline(line,5))
                        
                else:
                        new_file.write(line)
	
file_object.close()
new_file.close()
