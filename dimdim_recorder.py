#!/usr/bin/env python

# Red5 Recorder
# Author: Wagner Spirigoni
# email: wagnerspi@gmail.com

import time, os, string, datetime, commands


# Adiciona o path do arquivo de log e do destino dos videos
caminho_log = "/usr/local/dimdim/red5/log/"
caminho_destino = "/root/"


# Pega o arquivo mais recente
arquivo = commands.getoutput("ls -lht " + caminho_log + " | grep 'red5'")
arquivo = string.split(arquivo, "\n")
arquivo = string.split(arquivo[0])
arquivo = caminho_log + arquivo[8]
file = open(arquivo,'r')

# Pega o tamanho do arquivo e move para o final dele, afinal so queremos entradas novas
st_results = os.stat(arquivo)
st_size = st_results[6]
file.seek(st_size)

while 1:
    where = file.tell()
    line = file.readline()
    # se nao tem linha nova, espera 1 segundo e volta ao inicio do while
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
    # linha nova, verifica se e a linha que precisamos
	entra_usuario = line.find("getVODProviderFile")
        if entra_usuario > -1:
        	inicio = string.split(str(line))
                id_video = inicio[11]
                id_sala = string.split(inicio[9], '/')
                id_sala = id_sala[1]
		ARQUIVO = caminho_destino + str(datetime.datetime.now().day) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().year) + "_" + id_sala + "_" + id_video + ".flv"
		if (os.path.isfile(ARQUIVO) != True):	
	                 os.system("/usr/bin/rtmpdump -r rtmp://webclass.4linux.com.br:1935/dimdimPublisher/" + id_sala + "/" + id_video + " --live -o " + ARQUIVO + " > /dev/null 2>&1 &")


