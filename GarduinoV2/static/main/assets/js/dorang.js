/*!
=========================================================
* Dorang Landing page
=========================================================

* Copyright: 2019 DevCRUD (https://devcrud.com)
* Licensed: (https://devcrud.com/licenses)
* Coded by www.devcrud.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

 // toggle 
$(document).ready(function(){
    
    $('.search-toggle').click(function(){
        $('.search-wrapper').toggleClass('show');
    });

    $('.modal-toggle').click(function(){
        $('.modalBox').toggleClass('show');
    })

    $('.modalBox').click(function(){
        $(this).removeClass('show');
    });

    $('.spinner').click(function(){
        $(".theme-selector").toggleClass('show');
    });
    $('.light').click(function(){
        $('body').addClass('light-theme');
        $('body').removeClass('dark-theme');
    });
    $('.dark').click(function(){
        $('body').toggleClass('dark-theme');
        $('body').removeClass('light-theme');
    });
});



// smooth scroll
$(document).ready(function(){
    $(".navbar .nav-link").on('click', function(event) {

        if (this.hash !== "") {

            event.preventDefault();

            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 700, function(){
                window.location.hash = hash;
            });
        } 
    });
}); 

function get_api_data() {
    let response = fetch("http://127.0.0.1:8000/home/api/1")
    response.then(response => response.json())
        .then(data => {
            console.log(data);
            // Calculating percentages on dials
            let temp = (data["temp"]/50)*360;
            let humidity = (data["humidity"]/100)*360;
            let fertilizer = (data["fertilizer_level"]/100)*360;
            let intensity = (data["led_intensity"]/100)*360;
            console.log("Fertilizer: " + fertilizer);
            console.log(temp)

            // Assigning API data to webpage
            document.querySelector("#temp").innerHTML = `TEMP: ${data["temp"]}&#8451`;
            document.querySelector("#temp-dial").style.background = `radial-gradient(black 50%, transparent 51%), conic-gradient(transparent 0deg ${temp}deg, gainsboro ${temp}deg 360deg),conic-gradient(orange 0deg, yellow 140deg, red 240deg)`;

            document.querySelector("#humidity").innerHTML = `HUMIDITY: ${data["humidity"]}%`;
            document.querySelector("#humidity-dial").style.background = `radial-gradient(black 50%, transparent 51%), conic-gradient(transparent 0deg ${humidity}deg, gainsboro ${humidity}deg 360deg),conic-gradient(white 0deg, lightblue 90deg, blue 240deg)`;

            document.querySelector("#fertilizer").innerHTML = `FERTILIZER: ${data["fertilizer_level"]}%`;
            document.querySelector("#fertilizer-dial").style.background = `radial-gradient(black 50%, transparent 51%), conic-gradient(transparent 0deg ${fertilizer}deg, gainsboro ${fertilizer}deg 360deg),conic-gradient(white 0deg, lightgreen 90deg, green 240deg)`;

            document.querySelector("#intensity").innerHTML = `INTENSITY: ${data["led_intensity"]}%`;
            document.querySelector("#intensity-dial").style.background = `radial-gradient(black 50%, transparent 51%), conic-gradient(transparent 0deg ${intensity}deg, gainsboro ${intensity}deg 360deg),conic-gradient(white 0deg, lightyellow 90deg, yellow 240deg)`;
            
            // Changing text
            document.querySelector("#text-plant-type").innerHTML = `Plant type: ${data["name"]}`;
            document.querySelector("#text-next-spray-time").innerHTML = `Next Spray Time: ${data["next_spray"]}`;
            document.querySelector("#text-sundown-time").innerHTML = `Sundown Time: ${data["time_to_sundown"]}`;
            // callback(data);
        })
        .catch(error => {
            console.log("Error: "+error);
        });
}

document.addEventListener('DOMContentLoaded', () => {
    setInterval(get_api_data, 1000);
})