#!/usr/bin/env python3
import requests
def find_files():
    files=[]
    with open("temp.txt","r") as f:
        temp=f.readlines()
        for file in temp:
            files.append(file.strip())
    return files

def get_info(file):
    with open(file,"r") as f:
        title=f.readline().strip()
        name=f.readline().strip()
        date=f.readline().strip()
        feedback=f.read().strip()
    user_review={"title":title,"name":name,"date":date,"feedback":feedback}
    return user_review

def send_reviews(dict):
    r=requests.post("https://httpbin.org/",data=dict)
    print(r.text)
    if r.ok:
        print("Successfully sent review...")
    else:
        print(r.text)

def main():
    for file in find_files():
        send_reviews(get_info(file))

if __name__=="__main__":
    main()