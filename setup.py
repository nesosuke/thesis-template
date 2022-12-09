#!/usr/bin/python3
import glob
import shutil
import os

# ファイル名とディレクトリの置換: _sampleを削除したコピーを作成する
for fd in glob.glob('./*_sample*'):
    if os.path.isdir(fd):
        newfilename = fd.replace('_sample', '_copy')
        try:
            shutil.copytree(fd, newfilename)
        except FileExistsError:
            continue
    else:  # ファイルの場合
        newfilename = fd.replace('_sample', '_copy')
        try:
            shutil.copy(fd, newfilename)
        except FileExistsError:
            continue

# ファイルの中の文字列を置換する: _sampleを削除する
for f in glob.glob('./*_copy*'):
    try:
        with open(f, 'r', encoding='utf-8') as f:
            s = f.readlines()
        with open(f, 'w', encoding='utf-8') as f:
            for line in s:
                f.write(line.replace('_sample', ''))
    except:
        continue

# ファイル名を置換する: _copyを削除する
for fd in glob.glob('./*_copy*'):
    if os.path.isdir(fd):
        newfilename = fd.replace('_copy', '')
        try:
            shutil.copytree(fd, newfilename)
        except FileExistsError:
            continue
    else:  # ファイルの場合
        newfilename = fd.replace('_copy', '')
        try:
            shutil.move(fd, newfilename)
        except FileExistsError:
            continue

# 複数回実行するとサブディレクトリに_copyが残るので削除する
for fd in glob.glob('./*_copy*'):
    if os.path.isdir(fd):
        shutil.rmtree(fd)
    else:  # ファイルの場合
        os.remove(fd)
for fd in glob.glob('./*/*_copy*'):
    if os.path.isdir(fd):
        shutil.rmtree(fd)
    else:  # ファイルの場合
        os.remove(fd)
