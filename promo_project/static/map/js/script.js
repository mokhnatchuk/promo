function initMap() {
  let map = L.map("map").setView([48.3794, 31.1656], 6);
  let mapLayer = L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
  ).addTo(map);
}

document.addEventListener("DOMContentLoaded", initMap);
