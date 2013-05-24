import re
import ConfigParser
from datetime import datetime,timedelta

def transform_time(time_string,offset):
    t_src = datetime.strptime(time_string,"%H:%M:%S,%f")
    t = t_src - timedelta(seconds = offset)
    return t.strftime("%H:%M:%S,%f")[:-3]

def match_time_str(raw_time_string):
    pattern = re.compile("[0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9][0-9][0-9]")
    return pattern.findall(raw_time_string)

def process_line(line,offset):
    res = []
    match = match_time_str(line)
    if match:
        for time_str in match:
            res.append(transform_time(time_str,offset))
        return " --> ".join(res)+'\n'
    return line

def process_document(offset=0):
    processing = False
    f = open(FILE_NAME,'r')
    output = open('second_part.srt','a')
    i = 0
    for line in f.readlines(): 
        if not processing and PARTITION_MARK in line:
            processing = True
        if processing:
            new_line = process_line(line,offset)
            output.write(new_line)
            i+=1
            print str('Lines processed: ' + str(i))
    print "That's all folks! Check your second_part.srt file :) "

config = ConfigParser.RawConfigParser()
config.read('config.cfg')
OFFSET_IN_SECONDS = config.getint('All parameters','offset_to_substract_in_seconds')
FILE_NAME = config.get('All parameters','file_name')
PARTITION_MARK = config.get('All parameters','partition_mark')
process_document(offset=OFFSET_IN_SECONDS)
