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
    new = []
    person = None
    for line in chat:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue  
        if person:
            new.append(person + ': '+ line)
    return new

def write_file(filename_w, chat):
    with open(filename_w, 'w', encoding = 'utf-8-sig') as file:
        for dialogue in chat:
            file.write(dialogue + '\n')

def main():
    filename_r = '/Users/yuanke.tsai/Desktop/coding/chat/chat_file/chat1/input拷貝.txt'
    if os.path.isfile(filename_r):
        print('檔案存在，執行中', '\n') 
    chat = read_file(filename_r)
    chat = convert(chat)
    write_file('output.txt', chat)


main()


