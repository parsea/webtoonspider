import requests
from bs4 import BeautifulSoup
import re

def has_data(tag):
    return tag.has_attr('data-title-no')

def get_name(name):
	fo = open(name,"r",encoding="UTF-8")
	lists = []
	for line in fo.readlines():
		lists.append(line.strip())
	return lists

def save_name(name,sets):
	fo = open(name,"w")
	for up in sets:
		fo.write(up+"\n")

def get_bs(lists):
	sets = set([]);
	r = requests.get("https://www.dongmanmanhua.cn/genre")
	soup = BeautifulSoup(r.text,"html.parser")
	for tag in soup.find_all(has_data):
		if tag.p.string in lists:
			# temp = tag.find_all("span",class_="icon_area")
			for up_names in tag.select(".txt_ico_up"):
				if up_names.string == "UP":
					sets.add(tag.p.string)
	return sets

lists = get_name("name.txt")
sets = get_bs(lists)
save_name("up.txt",sets)
print("更新的漫画是",sets)