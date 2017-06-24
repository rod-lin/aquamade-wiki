
from html.parser import HTMLParser

import sys
import re
import os

import upload

# upload.upload("Template:HFLS_H2Z_Hangzhou/js", "attack!attack!")

AQ_ABS_BASE = "src"

def expand(path):
	file = open(path)
	cont = file.read()

	href_reg = re.compile(r"href=['\"]([^'\"]*)['\"]")
	src_reg = re.compile(r"src=['\"]([^'\"]*)['\"]")

	css_reg = re.compile(r"<link[^>]*>")
	script_reg = re.compile(r"<script[^>]*>[^<]*</script>")

	base = os.path.dirname(path)
	file_name = path[len(base) + 1:].split(".")[0]
	abs_base = AQ_ABS_BASE

	def rep_css(m):
		tag = m.group(0)
		href = href_reg.search(tag)

		if href:
			href = href.group(1)

			if href[:4] != "http":
				if href[0] == "/":
					path = abs_base + href
				else:
					path = base + "/" + href

				with open(path) as f:
					return "<style>" + f.read() + "</style>"

		return tag

	alljs = ""
	jsurl = ""
	has_ins = 0

	def encpath(path):
		com = re.split(r"/|.", path)
		loc = "/".join(com)

		if com[-1] == "js":
			return "Template:HFLS_H2Z_Hangzhou/" + loc
		else:
			return "Team:HFLS_H2Z_Hangzhou/" + loc


	def rep_js(m):
		nonlocal alljs
		nonlocal has_ins
		nonlocal jsurl

		tag = m.group(0)
		js = src_reg.search(tag)

		if js:
			js = js.group(1)

			if js[:4] != "http":
				if js[0] == "/":
					path = abs_base + js
				else:
					path = base + "/" + js

				with open(path) as f:
					alljs += ";" + f.read() + ";"

					if has_ins:
						return "" # delete the original script
					else:
						has_ins = 1
						jsurl = "Template:HFLS_H2Z_Hangzhou/" + base + "/" + file_name + "/js"
						return "<script src='/" + jsurl + "?action=raw&ctype=text/javascript'></script>"

		return tag

	cont = css_reg.sub(rep_css, cont)
	cont = script_reg.sub(rep_js, cont)

	# print(cont)

	return (cont, alljs, jsurl)

if len(sys.argv) >= 2:
	(res, alljs, jsurl) = expand(sys.argv[1])
	
	with open(sys.argv[1] + ".merged", "w") as output:
		output.write(res)

	upload.upload(jsurl, alljs)
else:
	print("wrong argument")
