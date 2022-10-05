console.log("Sashinha")


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