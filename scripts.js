// Movie data object with details for each movie
const movies = {
    1: {
        title: "Rajasaab",
        genre: "Comedy and Horror​.",
        releaseDate: "April 10, 2025",
        synopsis: "Rajasaab revolves around a young man inheriting a haunted mansion, where he encounters the ghost of his grandfather.The film explores themes of loyalty, corruption, and political dynamics​.",
        image: "Rajasaab.jpg",
        trailer: "L1zlE6B3F_c"
        
    },
    2: {
        title: "Salaar",
        genre: "Action, Drama, Friendship, Loyality and Power Struggles",
        releaseDate: "December 22, 2023",
        synopsis: "Salaar revolves around friendship and loyalty, as a man fights to help his exiled prince friend reclaim power in a ruthless kingdom.",
        image: "Salaar.png",
        trailer: "4GPvYMKtrtI"
    },
    3: {
        title: "Mirchi",
        genre: "Action, romance, family drama.",
        releaseDate: "February 8, 2013",
        synopsis: "Mirchi revolves around love and family, as a man strives to end violence and reunite two feuding families.",
        image: "Mirchi.png",
        trailer: "I6QLMyeC1n8"
    }
};

// Function to get URL parameters
//file:///C:/Users/bvraju/Desktop/FrontEndWebProject1/details.html?movie=2
function getQueryParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    //window.location.search: This part accesses the query string from the current URL
    return urlParams.get(param);
    //For instance, calling urlParams.get('movie') would return 2 if the URL was 
    //file:///C:/Users/bvraju/Desktop/FrontEndWebProject1/details.html?movie=2
}
//if the URL is details.html?movie=2, the function will return 2

// Populate movie details dynamically
document.addEventListener('DOMContentLoaded', () => {
    
    const movieId = getQueryParam('movie');  //eg: 2
    
    const movie = movies[movieId]; // if movieId is 2, it gives the details of "Baahubali"

    document.querySelector('h3').textContent = movie.title;
    
    // selecting an HTML element based on the combinationof bootstrap class and element name
    document.querySelector('.col-md-8 img').src = movie.image;

                                        //1st para
    document.querySelector('.col-md-4 p:nth-of-type(1)').innerHTML = `<strong>Genre:</strong> ${movie.genre}`;
                                        //2nd para
    document.querySelector('.col-md-4 p:nth-of-type(2)').innerHTML = `<strong>Release Date:</strong> ${movie.releaseDate}`;
                                        //3rd para
    document.querySelector('.col-md-4 p:nth-of-type(3)').textContent = movie.synopsis;
    
    //for debugging purpose
    //console.log(`Video URL: https://www.youtube.com/embed/${movie.trailer}`); // Check video URL
    document.querySelector('iframe').src = `https://www.youtube.com/embed/${movie.trailer}`;

});

/*
DOMContentLoaded Event: Once the browser has fully parsed the HTML content of details.html 
(but before external resources like images or stylesheets may be fully loaded), 
the DOMContentLoaded event is triggered. 
This is when your JavaScript, which is listening for this event, can execute and interact 
with the DOM (like filling in the dynamic content of the page, which in our case, 
    is the movie details).
*/

// Note: window.onload: This event is triggered when all the resources on the page 
// (HTML, CSS, JavaScript, images, etc.) are fully loaded.
//window.onload = function() {
    // Code to update movie details here
//};