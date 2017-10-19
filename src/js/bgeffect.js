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
		renderer.setClearColor(0xfcfcfc);
		dom.append(renderer.domElement);
		
		this.renders = [];
		
		var light = new THREE.HemisphereLight(0xe9eff2, 0x01010f, 1);
		scene.add(light);
		
		var geometry = new THREE.SphereGeometry(2.5, 10, 10);
		var wireframe = new THREE.WireframeGeometry(geometry);
		var material = new THREE.LineBasicMaterial({
			color: 0xaaaaaa,
			linewidth: 1,
		});
		var circle = new THREE.Line(wireframe, material);
		scene.add(circle);
		
		camera.position.z = 10;
		
		this.renders.push(function () {
			circle.rotation.x += 0.01;
			circle.rotation.y += 0.01;
			circle.rotation.z += 0.01;
		});
		
		this.scene = scene;
		this.camera = camera;
		this.renderer = renderer;
		
		this.paused = true;
	}
	
	window.BGEffect = BGEffect;

	BGEffect.prototype = {};
	
	BGEffect.prototype.start = function () {
		var self = this;
		
		var animate = function () {
			if (self.paused) return;
			
			requestAnimationFrame(animate);

			for (var i = 0; i < self.renders.length; i++) {
				self.renders[i]();
			}

			self.renderer.render(self.scene, self.camera);
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
