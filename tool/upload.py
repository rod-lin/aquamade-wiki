# upload tool for iGEM wiki

import urllib.request
import urllib

import http.cookiejar

from bs4 import BeautifulSoup

import config
import imgmap

import requests

def pair(name, value):
	return http.cookiejar.Cookie(
		version = 0,
		name = name,
		value = value,
		port = None,
		port_specified = False,
		domain = "2017.igem.org",
		domain_specified = True,
		domain_initial_dot = False,
		path = "/",
		path_specified = True,
		secure = False,
		expires = None,
		discard = False,
		comment = None,
		comment_url = None,
		rest = None
	)

# return cookie
def login():
	cookie = http.cookiejar.MozillaCookieJar()

	cookie.set_cookie(pair(config.IGEM_YEAR + "_igem_orgToken", "53dc4c8c8058b531b2c7e58bf7fce72c"))
	cookie.set_cookie(pair(config.IGEM_YEAR + "_igem_orgUserID", "2042"))
	cookie.set_cookie(pair(config.IGEM_YEAR + "_igem_orgUserName", "Matt+Gerrard"))
	cookie.set_cookie(pair(config.IGEM_YEAR + "_igem_org_session", "n89t14do6hpc5hunm0rd081374"))

	return cookie

GLOBAL_COOKIE = login()

def post(url, dat, cookie = GLOBAL_COOKIE):
	dat = urllib.parse.urlencode(dat).encode("ascii")
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)

	req = urllib.request.Request(url, dat)
	resp = opener.open(req)

	return resp

def postmulti(url, dat, cookie = GLOBAL_COOKIE):
	return requests.post(url, files = dat, cookies = cookie).text

def getEditToken(cookie = GLOBAL_COOKIE):
	url = "http://" + config.IGEM_YEAR + ".igem.org/Team:" + config.TEAM_NAME + "?action=edit"
	resp = post(url, {}).read().decode()

	bs = BeautifulSoup(resp, "html5lib")

	# print(bs)

	return bs.find(attrs = { "name": "wpEditToken" })["value"]

# file e.g. Template:HFLS_H2Z_Hangzhou/js
def upload(file, data, cookie = GLOBAL_COOKIE):
	url = "http://" + config.IGEM_YEAR + ".igem.org/wiki/index.php?title=" + file + "&action=submit"
	dat = {
		"wpTextbox1": data,
		"wpEditToken": getEditToken(cookie),
		"wpUltimateParam": "1"
	}

	with open("log.html", "w") as fp:
		fp.write(post(url, dat, cookie).read().decode());

def saveImageMap():
	with open(config.ABS_TOOL_BASE + "/imgmap.py", "w") as fp:
		fp.write("UPLOADED = " + repr(imgmap.UPLOADED));

# assuming fname is /img/.*
def formatFileName(fname):
	return "T--HFLS_H2Z_Hangzhou--img_" + fname[5:].replace("/", "_")

def getFinalUrl(res):
	bs = BeautifulSoup(res, "html5lib")
	# print(bs.find(attrs = { "class": "fullMedia" }))
	return list(bs.find(attrs = { "class": "fullMedia" }).children)[0]["href"]

def getContentType(fname):
	conttype = {
		"jpg": "image/jpeg",
		"png": "image/png"
	}
	
	suf = fname[::-1].split(".")[0][::-1]
	
	if suf in conttype:
		return conttype[suf]
	else:
		return "image/jpeg"

# fname must be in the form "/img/.*"
def uploadImage(fname, cookie = GLOBAL_COOKIE):
	if fname in imgmap.UPLOADED:
		print("image " + fname + " already in cache as " + imgmap.UPLOADED[fname])
		return imgmap.UPLOADED[fname]
	else:
		# do the uploading
		
		with open(config.ABS_BASE + fname, "rb") as fp:
			url = "http://" + config.IGEM_YEAR + ".igem.org/Special:Upload"
			dat = {
				"wpUploadFile": ("don't tell you", fp, getContentType(fname)), # fp.read(),
				"wpDestFile": (None, formatFileName(fname)),
				"wpUploadDescription": (None, ""),
				
				"wpLicense": (None, ""),
				"wpWatchthis": (None, "1"),
				"wpIgnoreWarning": (None, "1"),
				"wpEditToken": (None, getEditToken(cookie)),
				"wpUpload": (None, "Upload file"),
				
				"wpDestFileWarningAck": (None, ""),
				"title": (None, "Special:Upload")
			}
			
			print("uploading " + fname + " as " + formatFileName(fname))
			res = postmulti(url, dat, cookie)
			
			with open("upload-img-log.html", "w") as fp:
				fp.write(res);
			
			final = getFinalUrl(res)
			
			imgmap.UPLOADED[fname] = final
			saveImageMap()
			
			print("finished " + final)
			
			return final
