$("script").each(function (n, el) {
	el = $(el);
	el.html(el.html().replace(/&amp;/g, $("#raw-and").text()));
});
