$(function () {
	
	function bindSticky(first) {
		$(".comsec-main .float-menu").sticky("destroy").sticky({
			scrollContext: $(".main.cont-wrap"),
			context: $(".comsec-main"),
			offset: 100,

			onStick: function () {
				$(".comsec-main .float-menu").css("display", "");
			},

			onBottom: function () {
				$(".comsec-main .float-menu").css("display", "none");
			}
		});
	}

	setTimeout(function () {
		bindSticky(true);
	}, 1000);
	
	function showPassage(name) {
		$(".comsec-main .passage.shown").removeClass("shown");
		$(".comsec-main .passage.passage-" + name).addClass("shown");

		var top = $(".main.cont-wrap").scrollTop();
		gradScroll(top + $(".comsec-main .passage.shown").offset().top - 115);

		setTimeout(function () {
			if (window.imgview) {
				imgview.refresh();
			}

			bindSticky();
		}, 100);
	}
	
	function setUniqueActive(dom) {
		$(dom).siblings(".active").removeClass("active");
		$(dom).addClass("active");
	}
	
	$(".comsec-main .passlink").each(function (i, dom) {
		dom = $(dom);
		
		dom.click(function () {
			var passage = dom.data("passage"); 
			
			if (passage)
				showPassage(passage);
		
			setUniqueActive(dom);
			
			$(".comsec-main .passlink").each(function (i, dom) {
				dom = $(dom);
				
				if (dom.data("passage") == passage) {
					setUniqueActive(dom);
				}
			});
		});
	});
});