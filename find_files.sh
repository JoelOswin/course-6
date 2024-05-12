#!/usr/bin/env bash
ls | grep ".*\.txt" > temp.txt
python3 run.py
rm temp.txt