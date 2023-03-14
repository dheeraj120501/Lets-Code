// Creating a Scene(Container where we put our actors, lights, camera etc.)
const scene = new THREE.Scene();

// Creating a Cube Mesh
const cubeGeometry = new THREE.BoxGeometry(1, 1, 1);
const cubeMaterial = new THREE.MeshBasicMaterial({
  color: "#ff0000",
});
const cubeMesh = new THREE.Mesh(cubeGeometry, cubeMaterial);

// Adding the mesh to the scene
scene.add(cubeMesh);

// Sizes
const sizes = {
  width: 800,
  height: 600,
};

// Camera
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height);
camera.position.z = 3;
scene.add(camera);

// Selecting the canvas to draw
const canvas = document.querySelector("canvas.webgl");

// Renderer
const renderer = new THREE.WebGLRenderer({
  canvas: canvas,
});
renderer.setSize(sizes.width, sizes.height);
renderer.render(scene, camera);
