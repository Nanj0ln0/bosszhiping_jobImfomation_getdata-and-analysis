import uuid
import random
import datetime,time
import os
import psutil
import re

def extractNum(val):
    num = 0
    if val:
        try:
            extract_val = re.findall(r'\d+', val)
            if len(extract_val) > 0:
                num = int(extract_val[0])
        except:pass

    return num
def filterFieldSummarys(summarys):

    value = ",".join(summarys)


    value = value.replace("\"", "")
    value = value.replace("\\", "")
    value = value.replace("'", ",")
    extract_val = re.findall(r'(\[\d+.{0,10}])', value)
    for v in extract_val:
        value = value.replace(v, "")

    return value
def cleanFieldValue(value):
    value = value.replace(":", "")
    value = value.replace("：", "")

    return value


def filterFieldKey(key):
    return key
def filterFieldValue(value):
    value = value.replace("\"", "")
    value = value.replace("\\", "")
    value = value.replace("'", ",")
    return value

def getMachineMemoryInfo():
    """
    获取机器内存实况
    :return:
    """

    phy_mem = psutil.virtual_memory()
    mem_percent = phy_mem.percent # （float类型）已用内存占比 54.5
    mem_used = int(phy_mem.used / 1024 / 1024) # 已用内存容量，单位M 8789
    mem_total = int(phy_mem.total / 1024 / 1024)# 共计内存容量，单位M 16125
    mem_left = mem_total - mem_used

    return mem_percent,mem_used,mem_left,mem_total

def generateFileDir(path):
    purpose_path = os.path.join(path, time.strftime("%Y"))
    purpose_path = os.path.join(purpose_path, time.strftime("%m"))
    purpose_path = os.path.join(purpose_path, time.strftime("%d"))
    purpose_path = os.path.join(purpose_path, time.strftime("%H%M"))

    if not os.path.exists(purpose_path):
        os.makedirs(purpose_path)

    return purpose_path
def generateName(prefix='', suffix=''):
    r = "%d%d" % (random.randint(1000, 9999), random.randint(1000, 9999))
    return prefix+r+suffix

def removeFile(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path) # 删除文件

def removeDir(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        file_path = os.path.join(dir_path, file)
        removeFile(file_path) # 删除文件夹内部的文件
    os.removedirs(dir_path) # 删除空文件夹

def generateCode(prefix=""):
    """
    生产永远不重复的随机数
    :param prefix: 编码前缀
    :return:
    """
    # d= self.get_datetime_format("%Y%m%d%H%M%S")
    # d = time.strftime("%Y%m%d%H%M%S")
    d = str(random.randint(100000,999999))+str(random.randint(100000,999999))

    val = str(uuid.uuid5(uuid.uuid1(), str(uuid.uuid1())))
    a = val.split("-")[0]
    code = "%s%s%s%d" % (prefix, d, a, random.randint(1000, 9999))

    return code


def GenDateListByStartAndEnd(start, end):
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)

    result = []

    curr_date = start_date
    while curr_date != end_date:
        # t="%04d-%02d-%02d" % (curr_date.year, curr_date.month, curr_date.day)

        result.append({
            "ym": "%04d-%02d" % (curr_date.year, curr_date.month),
            "ymd": curr_date
        })

        curr_date += datetime.timedelta(1)
    # result.append("%04d%02d%02d" % (curr_date.year, curr_date.month, curr_date.day))

    return result

