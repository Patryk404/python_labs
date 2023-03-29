import glob
import os

files = glob.glob("zadanie1/*")

for file in files:
    # os.makedirs((file.split("zadanie1/")[1])[0],exist_ok=True) # it can be used with this exist_ok=True to avoid errors
    try: 
        os.rename(file,(file.split("zadanie1/")[1])[0]+"/"+ file.split("zadanie1/")[1]) # zadanie1/BKBQLTII => zadanie1/BKBQLTII , B/BKBQLTII
    except FileNotFoundError:
        os.makedirs((file.split("zadanie1/")[1])[0],exist_ok=False) 
        os.rename(file,(file.split("zadanie1/")[1])[0]+"/"+ file.split("zadanie1/")[1])
