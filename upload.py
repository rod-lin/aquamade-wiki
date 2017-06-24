# upload tool for iGEM wiki

import urllib.request
import urllib

import http.cookiejar


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

# file e.g. Template:HFLS_H2Z_Hangzhou/js
def upload(file, data):
	url = "http://2017.igem.org/wiki/index.php?title=" + file + "&action=submit"
	
	dat = urllib.parse.urlencode({
		"wpTextbox1": data,
		"wpEditToken": "a526864ae8c423139cb9a8bf4d6e2e66+\\",
		"wpUltimateParam": "1"
	}).encode("ascii")

	cookie = http.cookiejar.MozillaCookieJar()

	cookie.set_cookie(pair("2017_igem_orgToken", "53dc4c8c8058b531b2c7e58bf7fce72c"))
	cookie.set_cookie(pair("2017_igem_orgUserID", "2042"))
	cookie.set_cookie(pair("2017_igem_orgUserName", "Matt+Gerrard"))
	cookie.set_cookie(pair("2017_igem_org_session", "n89t14do6hpc5hunm0rd081374"))

	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)

	req = urllib.request.Request(url, dat)
	resp = opener.open(req)
