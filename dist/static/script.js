const canvas = document.querySelector("#signal-canvas");
const ctx = canvas.getContext("2d");
const points = [];
let width = 0;
let height = 0;
let frame = 0;

function resize() {
  const ratio = Math.min(window.devicePixelRatio || 1, 2);
  width = window.innerWidth;
  height = window.innerHeight;
  canvas.width = width * ratio;
  canvas.height = height * ratio;
  canvas.style.width = `${width}px`;
  canvas.style.height = `${height}px`;
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);

  points.length = 0;
  const count = Math.max(58, Math.floor((width * height) / 17000));
  for (let i = 0; i < count; i += 1) {
    points.push({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.22,
      vy: (Math.random() - 0.5) * 0.22,
      pulse: Math.random() * Math.PI * 2,
    });
  }
}

function draw() {
  frame += 0.008;
  ctx.clearRect(0, 0, width, height);
  ctx.lineWidth = 1;

  for (const point of points) {
    point.x += point.vx;
    point.y += point.vy;
    if (point.x < -30) point.x = width + 30;
    if (point.x > width + 30) point.x = -30;
    if (point.y < -30) point.y = height + 30;
    if (point.y > height + 30) point.y = -30;
  }

  for (let i = 0; i < points.length; i += 1) {
    for (let j = i + 1; j < points.length; j += 1) {
      const a = points[i];
      const b = points[j];
      const dx = a.x - b.x;
      const dy = a.y - b.y;
      const distance = Math.sqrt(dx * dx + dy * dy);
      if (distance < 150) {
        const alpha = (1 - distance / 150) * 0.32;
        ctx.strokeStyle = `rgba(64, 216, 196, ${alpha})`;
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.stroke();
      }
    }
  }

  for (const point of points) {
    const pulse = 1.8 + Math.sin(frame + point.pulse) * 0.9;
    ctx.fillStyle = "rgba(224, 164, 59, 0.55)";
    ctx.beginPath();
    ctx.arc(point.x, point.y, pulse, 0, Math.PI * 2);
    ctx.fill();
  }

  requestAnimationFrame(draw);
}

window.addEventListener("resize", resize);
resize();
draw();
