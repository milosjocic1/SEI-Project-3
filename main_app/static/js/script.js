console.log("Sashinha e Milinhos são muito legais")

// WEATHER API
function info() {
    let apiKey = "3abe670647c3058ae4966e63fc9dbb50";
    let unit = "metric";
    let city = document.getElementById("city");
    city = city.innerText;
    console.log(city);
    let apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=${unit}`;
    
    axios.get(apiUrl).then(updateApp);
}
function updateApp(response) {
    // celsiusTemperature = response.data.main.temp;
    let city = document.getElementById("city")
    city = city.innerText;
    console.log(city)
    let currentTemperature = Math.round(response.data.main.temp);
    let temperature = document.querySelector("#weather-temp");
    temperature.innerHTML = `${currentTemperature}°C`;
    let currentFeel = Math.round(response.data.main.feels_like);
    let feel = document.querySelector("#weather-feel");
    feel.innerHTML = `${currentFeel}°C`;
    let currentDescription = response.data.weather[0].description;
    let description = document.querySelector("#weather-desc");
    description.innerHTML = `${currentDescription.charAt(0).toUpperCase() + currentDescription.slice(1)}`;
    let iconElement = document.querySelector("#icon");
    iconElement.setAttribute("src", `/static/images/weather-icons/${response.data.weather[0].icon}.svg`)
}
info()

// MAP
function initMap() {
  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 8,
    center: { lat: -34.397, lng: 150.644 },
  });
  var geocoder = new google.maps.Geocoder();
geocodeAddress(geocoder, map);
};

function geocodeAddress(geocoder, resultsMap) {
  var address = document.getElementById("city");
  address = address.innerText;
  geocoder.geocode({ address: address }, function (results, status) {
    if (status === "OK") {
      resultsMap.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
        map: resultsMap,
        position: results[0].geometry.location,
      });
    } else {
      alert("Geocode was not successful for the following reason: " + status);
    }
  });
}

function quiz()