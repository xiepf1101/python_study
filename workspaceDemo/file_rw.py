#coding=utf-8

#文件读写

#文件读取

try:
    # r 表示读取UTF编码的文本文件
        # rb 表示读取二进制文件，例如图片和视频    
    
    f = open('D:/Python/workspace/python_study_file/filerw.txt','r')
    print(f.read())
except:
    system.exit(0)
finally:
    if f:
        f.close()

# 用with更简单，不用写close
#with open('/path/to/file', 'r') as f:
#    print(f.read())

#文件写入
with open('D:/Python/workspace/python_study_file/filerw.txt','w') as f:
    f.write('python to write hello world')