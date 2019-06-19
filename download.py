import xml.dom.minidom
import os
from subprocess import call

# downloaded source path
tag = "android-9.0.0_r41"
mirror = "https://aosp.tuna.tsinghua.edu.cn/"
origin = "https://android.googlesource.com/"
rootdir = "D:/Android/Aosp/" + tag

# git program path
git = "C:/Program Files/Git/bin/git.exe"
dom = xml.dom.minidom.parse("D:/Android/Aosp/" + tag + "/manifest/default.xml")
root = dom.documentElement

prefix = git + " clone -b " + tag + " --single-branch " + mirror
suffix = ".git"

Launcher2 = "platform/packages/apps/Launcher2"
base = "platform/frameworks/base"
native = "platform/frameworks/native"
core = "platform/system/core"
bionic = "platform/bionic"
libcore = "platform/libcore"
# art = "platform/art"
msm = "kernel/msm"

if not os.path.exists(rootdir):
    os.mkdir(rootdir)

for node in root.getElementsByTagName("project"):
    os.chdir(rootdir)
    d = node.getAttribute("path")
    last = d.rfind("/")
    name = node.getAttribute("name")

    if name != Launcher2:
        print "name != Launcher2-->" + name
        if name != base:
            print "name != base-->" + name
            if name != native:
                print "name != native-->" + name
                if name != core:
                    print "name != core-->" + name
                    if name != bionic:
                        print "name != bionic-->" + name
                    if name != libcore:
                        print "name != libcore-->" + name
                        # if name != art:
                        #     print "name != art-->" + name
                        if name != msm:
                            print "name != msm-->" + name
                            continue
    print "final-->" + name

    if last != -1:
        d = rootdir + "/" + d[:last]
        if not os.path.exists(d):
            os.makedirs(d)
            os.chdir(d)
    cmd = prefix + name + suffix
    print cmd
    call(cmd)
