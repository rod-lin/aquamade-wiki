# upload tool for iGEM wiki

import urllib.request
import urllib

import http.cookiejar

from bs4 import BeautifulSoup

import config

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

	open("log.html", "w").write(post(url, dat, cookie).read().decode());

def uploadImage(file, cookie = GLOBAL_COOKIE):
	url = "http://" + config.IGEM_YEAR + ".igem.org/Special:Upload"
	dat = {
		
	}
