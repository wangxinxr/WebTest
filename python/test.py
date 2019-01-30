#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

import os

def all_path(dirname):
    filelistlog = dirname + r"/filelistlog.txt"  # 保存文件路径
    postfix = set(['xml'])  # 设置要保存的文件格式
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir,filename)
            # if True:        # 保存全部文件名。若要保留指定文件格式的文件名则注释该句
            if apath.split('.')[-1] in postfix:   # 匹配后缀，只保存所选的文件格式。若要保存全部文件，则注释该句
                try:
                    with open(filelistlog, 'a+') as fo:
                        fo.writelines(apath)
                        fo.write('\n')
                except:
                    pass    # 所以异常全部忽略即可


if __name__ == '__main__':
    dirpath = "/Users/wangxin"  # 指定根目录
    all_path(dirpath)
