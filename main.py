import socket
from pprint import pprint
import json
dect = {}
list2 = []
def domin(text: list)->list:
    list2 = []
    for i in text:
        with open("result.txt", "a") as file:
            file.write(f"{json.dumps({'Domin': i, 'id': socket.gethostbyname(i)}, indent = 4)}\n" )
    print("Muvaffaqqiyatli amalga oshirildi. Natijani resutl.txt da ko`rishingiz mn")

with open('domains.txt', 'r') as f:
    list1 = (f.read()).split('\n')
    domin(list1)