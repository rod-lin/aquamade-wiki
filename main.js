var express = require("express");

var app = express();

app.use("/", express.static("src"));

function redirect(from, to) {
	app.get(from, function (req, res) {
		res.redirect(to);
	});
}

redirect("/Team:HFLS_H2Z_Hangzhou", "/sub/home.html")
redirect("/Team:HFLS_H2Z_Hangzhou/project", "/sub/project.html")

app.listen(3141, "localhost");
