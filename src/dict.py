"""
author: hxc
date: 2023/8/25
"""

from xToolkit import xfile

a=xfile.read("test.xls").excel_to_dict()

for i in a:
    print(i)

"""
好好好
"""
