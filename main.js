var express = require("express");
var request = require("request");

var app = express();

app.use("/", express.static("src"));

function redirect(from, to) {
	app.get(from, function (req, res) {
		res.redirect(to);
	});
}

redirect("/Team:HFLS_H2Z_Hangzhou", "/sub/home.html")
redirect("/Team:HFLS_H2Z_Hangzhou/project", "/sub/project.html")
redirect("/", "/main.html")

// wiki resources
app.get(/\/wiki\/(.*)/, function (req, res) {
	req.pipe(request.post("http://2017.igem.org" + req.path, { form: req.body })).pipe(res);
});

app.listen(3141, "localhost");
