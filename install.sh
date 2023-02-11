#!/bin/bash

bashrc=$(echo $HOME)'/.bashrc'
zshrc=$(echo $HOME)'/.zshrc'

str="alias google='python3 $(pwd)/google.py'"
#check per bashrc
if [ -f $bashrc ]; then
    echo $str >> ~/.bashrc
fi

if [ -f $zshrc ]; then
    echo $str >> ~/.zshrc
fi
