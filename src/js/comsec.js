$(function () {
    
    function bindSticky() {
        $(".comsec-main .float-menu").sticky({
            scrollContext: $(".main.cont-wrap"),
            context: $(".comsec-main"),
            offset: 100,
            observeChanges: true
        });
    }

    setTimeout(bindSticky, 1000);
    
    function showPassage(name) {
        $(".comsec-main .passage.shown").removeClass("shown");
        $(".comsec-main .passage.passage-" + name).addClass("shown");

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