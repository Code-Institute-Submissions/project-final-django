
function initMap() {
    let map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: {
            lat: 52.014733,
            lng: 4.706523
        }
    });

    let labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    let locations = [
        { lat: 52.014733, lng: 4.706523},
    ];

    let markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    let markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
}