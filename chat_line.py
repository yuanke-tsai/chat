#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 12:20:28 2021

@author: yuanke.tsai
"""
import os
            
def read_file(filename_r):
    chat = []
    with open(filename_r, 'r', encoding = 'utf-8-sig') as file:
        for line in file:
            chat.append(line.strip())
    return chat


def convert(chat):
    person = None
    allen_count = 0
    viki_count = 0
    allen_sticker = 0
    viki_sticker = 0
    allen_pic = 0
    viki_pic = 0
    for line in chat:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker += 1
            elif s[2] == '圖片':
                allen_pic += 1
            else:
                for msg in s[2:]:
                    allen_count += len(msg)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker += 1
            elif s[2] == '圖片':
                viki_pic += 1
            else:
                for msg in s[2:]:
                    viki_count += len(msg)
    print('Allen 共說了 ', allen_count, '個字', allen_sticker, '個貼圖', allen_pic, '張圖片')
    print('Viki 共說了 ', viki_count, '個字', viki_sticker, '個貼圖', viki_pic, '張圖片')


def write_file(filename_w, chat):
    with open(filename_w, 'w', encoding = 'utf-8-sig') as file:
        for line in chat:
            file.write(line + '\n')


def main():
    filename_r = '/Users/yuanke.tsai/Desktop/coding/chat/chat_file/chat2/LINE-Viki.txt'
    if os.path.isfile(filename_r):
        print('檔案存在，執行中', '\n') 
    chat = read_file(filename_r)
    chat = convert(chat)
    #write_file('output_line.txt', chat)
    


main()


