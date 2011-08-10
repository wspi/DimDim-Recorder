#!/usr/bin/env python

# DimDim Recorder
# Author: Wagner Spirigoni
# email: wagner@wspi.com

import time, os, string, datetime, commands


# Log path and destination directory
log_path = "/usr/local/dimdim/red5/log/"
destination_directory = "/var/"

host="YOUR-HOST"
port="1935"

log = commands.getoutput("ls -lht " + log_path + " | grep 'red5'")
log = string.split(log, "\n")
log = string.split(log[0])
log = log_path + log[8]
file = open(log,'r')

st_results = os.stat(log)
st_size = st_results[6]
file.seek(st_size)

while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
	new_user = line.find("getVODProviderFile")
        if new_user > -1:
        	start = string.split(str(line))
                id_video = start[11]
                id_room = string.split(start[9], '/')
                id_room = id_room[1]
		video = destination_directory + str(datetime.datetime.now().day) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().year) + "_" + id_sala + "_" + id_video + ".flv"
		if (os.path.isfile(video) != True):	
	                 os.system("/usr/bin/rtmpdump -r rtmp://" + host + ":" + port + "/dimdimPublisher/" + id_room + "/" + id_video + " --live -o " + video + " > /dev/null 2>&1 &")


