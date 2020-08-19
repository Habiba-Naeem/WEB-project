/*Load the API from the specified URL
    * The async attribute allows the browser to render the page while the API loads
    * The key parameter will contain your own API key (which is not needed for this tutorial)
    * The callback parameter executes the initMap() function
*/
 // Initialize and add the map
const positionOptions = {
    enableHighAccuracy: true,
    maximumAge: 0,
    timeout:2000
}
function success( position ){
  var coord = {
    latitude: position.coords.latitude,
    longitude: position.coords.longitude
  }
  console.log("Lat:", coord.latitude);
  console.log("Long:", coord.longitude);
}

function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

function initMap() {
    var map = new google.maps.Map(document.getElementById('map'));
    
    var infoWindow = new google.maps.InfoWindow;

    // Try HTML5 geolocation.
    var  geo = navigator.geolocation;

    if ( geo ) {
      geo.getCurrentPosition( success, error, positionOptions, 
        
        function(){
          infoWindow.setPosition(success.coord);
          infoWindow.setContent('Location found.');
          infoWindow.open(map);
          map.setZoom(10);
          map.setCenter(success.coord);
        },
        function(){
          handleLocationError(true, infoWindow, map.getCenter());
        }
      )
    }
    else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
  

  function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
                          'Error: The Geolocation service failed.' :
                          'Error: Your browser doesn\'t support geolocation.');
    infoWindow.open(map);
  }
}
document.addEventListener('DOMContentLoaded', () => {
    initMap();
});