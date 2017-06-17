
from html.parser import HTMLParser

import sys
import re
import os

def expand(path):
	file = open(path)
	cont = file.read()

	href_reg = re.compile(r"href=['\"]([^'\"]*)['\"]")
	src_reg = re.compile(r"src=['\"]([^'\"]*)['\"]")

	css_reg = re.compile(r"<link[^>]*>")
	script_reg = re.compile(r"<script[^>]*>[^<]*</script>")

	base = os.path.dirname(path)
	abs_base = os.path.realpath(os.path.dirname(sys.argv[0]))

	def rep_css(m):
		tag = m.group(0)
		href = href_reg.search(tag)

		if href:
			href = href.group(1)

			if href[:4] != "http":
				if href[0] == "/":
					path = abs_base + href
				else:
					path = base + href

				with open(path) as f:
					return "<style>" + f.read() + "</style>"

		return tag

	def rep_js(m):
		tag = m.group(0)
		js = src_reg.search(tag)

		if js:
			js = js.group(1)

			if js[:4] != "http":
				if js[0] == "/":
					path = abs_base + js
				else:
					path = base + js

				with open(path) as f:
					return "<script>" + f.read() + "</script>"

		return tag

	cont = css_reg.sub(rep_css, cont)
	cont = script_reg.sub(rep_js, cont)

	# print(cont)

	return cont

if len(sys.argv) >= 3:
	res = expand(sys.argv[1])
	with open(sys.argv[2], "w") as output:
		output.write(res)
else:
	print("wrong argument")
