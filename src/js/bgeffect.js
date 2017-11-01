"use strict";

(function () {
	function BGEffect(dom) {
		dom = $(dom);
		
		var scene = new THREE.Scene();
		var camera = new THREE.PerspectiveCamera(75, dom.innerWidth() / dom.innerHeight(), 0.1, 1000);
		
		var renderer = new THREE.WebGLRenderer({
			antialias: true
		});
		
		renderer.setSize(dom.innerWidth(), dom.innerHeight());
		renderer.setClearColor(0xfdfdfd);
		dom.append(renderer.domElement);
		
		this.renders = [];
		
		var light = new THREE.HemisphereLight(0xe9eff2, 0x01010f, 1);
		scene.add(light);
		
		var geometry = new THREE.SphereGeometry(10, 36, 36);
		var wireframe = new THREE.WireframeGeometry(geometry);
		var material = new THREE.LineBasicMaterial({
			color: 0xe3e3e3,
			linewidth: 1,
		});

		var circle = new THREE.Line(wireframe, material);
		scene.add(circle);
		
		camera.position.z = 10;

		var initx = circle.rotation.x = Math.random() * 2 - 1;
		var inity = circle.rotation.y = Math.random() * 2 - 1;
		var initz = circle.rotation.z = Math.random() * 2 - 1;
		
		this.renders.push(function () {
			var scroll = $(".main.cont-wrap").scrollTop();
			circle.rotation.x = initx + scroll / 1000;
			circle.rotation.y = inity + scroll / 1000;
			circle.rotation.z = initz + scroll / 2000;
		});
		
		this.scene = scene;
		this.camera = camera;
		this.renderer = renderer;
		
		this.paused = true;
	}
	
	window.BGEffect = BGEffect;

	BGEffect.prototype = {};
	
	BGEffect.prototype.oneFrame = function () {
		for (var i = 0; i < this.renders.length; i++) {
			this.renders[i]();
		}

		this.renderer.render(this.scene, this.camera);
	};
	
	BGEffect.prototype.start = function () {
		var self = this;
		
		var animate = function () {
			if (self.paused) return;
			
			requestAnimationFrame(animate);
			
			self.oneFrame();
		};
		
		if (!self.paused) return;
		self.paused = false;
		
		animate();
	};
	
	BGEffect.prototype.pause = function () {
		this.paused = true;
	};
	
	window.BGEffect = BGEffect;
})();
