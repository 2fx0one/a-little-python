import os
import sys
import shutil
import re


def filter_file_content_2(file_path):
    # 多行注释 需要回写到文件后， 再去除一次
    content = ''.join(filter(lambda s: len(s.strip()) != 0, open(file_path, 'r').readlines()))
    open(file_path, 'w').write(content)
    return file_path


def filter_file_content_1(file_path):
    map_func = [
        lambda s: re.sub(r'^import .*$', '', s),  # package
        lambda s: re.sub(r'^package .*$', '', s),  # import
        lambda s: re.sub(r'//.*$', '', s),  # 去除单行注释
    ]

    lines = open(file_path, 'r').readlines()
    for f in map_func:
        lines = map(f, lines)

    # 去除多行 文档注释
    content = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", ''.join(lines))

    open(file_path, 'w').write(content)
    return file_path


def clean_file(file_path):
    filter_file_content_2(filter_file_content_1(file_path))


def code_cleanup(in_dir, out_dir):
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)

    shutil.copytree(in_dir, out_dir)

    for f in walk_dir(out_dir):
        if f.endswith(".java"):
            print(f)
            clean_file(f)
        else:
            os.remove(f)

    allText = ''.join([open(f, 'r').read() for f in walk_dir(out_dir)])

    open(out_dir + os.path.sep + 'all', 'w').write(allText)


def walk_dir(dir):
    all = []
    for fpath, dirname, fnames in os.walk(dir):
        if len(fnames) != 0:
            for n in fnames:
                all.append(fpath + os.path.sep + n)

    return all


if __name__ == '__main__':
    print('code cleaner! welcome')
    print(len(sys.argv))
    # if (len(sys.argv)==2) and os.path.isdir(sys.argv[1]):
    #     target = sys.argv[1]
    #     code_cleanup(target, './cleanUp')
    # else:
    #     print("usage: %s [target_dir]" % sys.argv[0])
    input_dir = 'target'
    output_dir = 'cleanUp'

    code_cleanup(input_dir, output_dir)


