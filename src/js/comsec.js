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
				$(".comsec-main .float-menu").parent().css({
					"position": "absolute",
					"bottom": "0",
					"height": "auto",
					"z-index": "100"
				});
			}
		});

		$(".comsec-main .passage").css({
			"min-height": $(".comsec-main .float-menu").outerHeight(true)
		});
	}

	setTimeout(function () {
		bindSticky(true);
	}, 1000);

	function refresh() {
		var top = $(".main.cont-wrap").scrollTop();
		gradScroll(top + $(".comsec-main .passage.shown").offset().top - 115);

		setTimeout(function () {
			if (window.imgview) {
				imgview.refresh();
			}

			bindSticky();
		}, 100);
	}
	
	function showPassage(name) {
		$(".comsec-main .passage.shown").removeClass("shown");
		$(".comsec-main .passage.passage-" + name).addClass("shown");

		refresh();
	}
	
	function setUniqueActive(dom) {
		$(".comsec-main .active.passlink").removeClass("active");

		// $(dom).siblings(".active").removeClass("active");
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

	var doms = $(".comsec-main.comsec-use-exnav .passage")
	
	function showPassageNo(no) {
		if (no >= 0) {
			if (no < doms.length) {
				setUniqueActive($(".comsec-main.comsec-use-exnav .passlink")[no]);

				$(".comsec-main .passage.shown").removeClass("shown");
				$(doms[no]).addClass("shown");
				refresh();
			}
		}
	}
	
    doms.each(function (i, dom) {
        dom = $(dom);

        var op_bar = $("<div style='margin-top: 3rem;'> \
            <button class='ui right floated primary button next-btn'>Next</button> \
            <button class='ui button prev-btn'>Prev</button> \
        </div>");
		
		if (i + 1 >= doms.length) {
			op_bar.find(".next-btn").addClass("disabled");
		}

		if (i - 1 < 0) {
			op_bar.find(".prev-btn").addClass("disabled");
		}

		var top_op_bar = op_bar.clone();
		
		top_op_bar.css({
			"margin-top": "0",
			"margin-bottom": "3rem"
		});

		dom.prepend(top_op_bar);
		dom.append(op_bar);

		op_bar.find(".next-btn").click(function () {
            showPassageNo(i + 1);
		});
		
		op_bar.find(".prev-btn").click(function () {
            showPassageNo(i - 1);
		});

		top_op_bar.find(".next-btn").click(function () {
            showPassageNo(i + 1);
		});
		
		top_op_bar.find(".prev-btn").click(function () {
            showPassageNo(i - 1);
		});
    });
});