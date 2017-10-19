
from html.parser import HTMLParser

import base64
import sys
import re
import os

import upload

import config

# upload.upload("Template:HFLS_H2Z_Hangzhou/test_upload", "attack!attack!")

def expand(path):
	file = open(path)
	cont = file.read()

	href_reg = re.compile(r"href=['\"]([^'\"]*)['\"]")
	src_reg = re.compile(r"src=['\"]([^'\"]*)['\"]")
	
	img_reg = re.compile(r"/img/.*\.jpg")

	css_reg = re.compile(r"<link[^>]*>")
	script_reg = re.compile(r"<script[^>]*>[^<]*</script>")

	base = os.path.dirname(path)
	file_name = path[len(base) + 1:].split(".")[0]
	abs_base = config.ABS_BASE

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
						jsurl = "Template:" + config.TEAM_NAME + "/" + base + "/" + file_name + "/js"
						return "<script src='/" + jsurl + "?action=raw&ctype=text/javascript'></script>"

		return tag
		
	def rep_img(m):
		img = m.group(0)

		with open(abs_base + img, "rb") as f:
			url = "data:image/jpeg;base64," + bytes.decode(base64.b64encode(f.read()))
			# print(url[:100])
			return url

	cont = css_reg.sub(rep_css, cont)
	cont = script_reg.sub(rep_js, cont)
	# cont = img_reg.sub(rep_img, cont)

	# print(cont)

	return ("{{Template:" + config.TEAM_NAME + "}}" + cont, alljs, jsurl)

if len(sys.argv) >= 2:
	print("merging...", end = "")
	(res, alljs, jsurl) = expand(sys.argv[1])
	print("finished")

	print("writing result...", end = "")
	with open(sys.argv[1] + ".merged", "w") as output:
		output.write(res)
	print("finished")

	print("uploading js ball...", end = "")
	upload.upload(jsurl, alljs)
	print("finished")

	if len(sys.argv) >= 3:
		print("uploading page...", end = "")
		upload.upload(sys.argv[2], res)
		print("finished")
else:
	print("wrong argument")
	print("usage: " + sys.argv[0] + " <html source file> [target url]")
