"use strict";
const canvas = document.getElementById('graph');
const dx = 1;
const maxwidth = parseFloat(window.getComputedStyle(canvas).width);
const maxheight = parseFloat(window.getComputedStyle(canvas).height);
function drawPoint(surface, x, y) {
    const pointEl = document.createElement('div');
    pointEl.className = 'dot';
    pointEl.style.left = `${x}px`;
    pointEl.style.top = `${maxheight / 2 - y}px`;
    surface.appendChild(pointEl);
}
function getPoint(div) {
    return [parseFloat(div.style.left), parseFloat(div.style.top)];
}
function drawGraph(surface, graph, startx = 0, starty = 0) {
    surface.innerHTML = "";
    while (surface.childNodes.length < maxwidth)
        drawPoint(surface, surface.childNodes.length, graph(surface.childNodes.length + startx) - starty);
}
function movePoint(div, dx, dy) {
    div.style.left = `${parseFloat(div.style.left) + dx}px`;
    div.style.top = `${parseFloat(div.style.top) + dy}px`;
}
function moveGraph(surface, graph, dx = 0, dy = 0) {
    while (dx-- > 0)
        surface.removeChild(surface.firstChild);
    let x = surface.childNodes.length;
    surface.childNodes.forEach(v => movePoint(v, dx, dy));
    // while (x < maxwidth)
    //     drawPoint(surface, x, graph(surface.childNodes.length))
    // // graph
}
let c = 0;
let myfunction = (x) => Math.sin(x * Math.PI / 180) * 100;
drawGraph(canvas, myfunction);
setInterval(() => moveGraph(canvas, myfunction, 1), 10);
