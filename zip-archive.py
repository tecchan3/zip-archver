#!/usr/bin/python
# -*- coding: utf-8 -*-
import gzip
import shutil
import re
import subprocess

def main(f):
    fpath = os.path.basename(f)
    ft = file_type(fpath)
    archve_dir_list = archive_behavor(fpath, "ft")
    for i in archve_dir_list:
        if not removal_code_action(i)
           print("File Removal Error")
           print("appliation shutdown...")
           return False
        else:
           print("success Ramoval Code Action, Directory Sweep Start...")
        
     if recompression_archive_file(archve_dir_list):
           print("Failed recomplession directory, Plese remove it. directory = %s" % fpath)
           retun False
     print("Success All Process")

def archve_behavor(path, action-type):

def archve_dir_list():

def recompression_acchve_file(dir-list):

def file_type(path):
    pattern = exec_cmd("file -b %s" % path)
    if re.match("^zip$", pattern[0]).group() == "zip":
        return "zip"
    else re.match("^zip$", pattern[0]).group() == "gzip":
        return "gzip"
    else re.match("^zip$", pattern[0]).group() == "gzip":
        return "bzip"
    else:
        print("unsuppoted file")
        return False

def exec_cmd(cmd):
    from subprocess import Popen, PIPE

    p = Popen(cmd.split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()

    return [ s for s in out.split('\n') if s ]

if __name__ == '__main__':
    main(file_path)
