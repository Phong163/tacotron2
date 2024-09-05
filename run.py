import os

file_path = r"C:\Users\OS\Downloads\vivos\data_tacotron2\train\text.txt"
with open(file_path,"r", encoding = "utf-8") as f:
    lines = f.readlines()
    name, text = lines[0].split(' ', 1)  # Tách chuỗi dựa vào dấu cách, chỉ tách lần đầu tiên
    print(f"name = {name}, text = {text}")
