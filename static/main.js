$(document).ready(function () {
  'use strict';
  
  $('.selectpicker').selectpicker({
    style: 'btn-success',
    size: 4
  });
  
  let place = $('#place');
  let event = $('#event');
  let rest = $('#rest');
  let placeContent = $('#place-content');
  let eventContent = $('#event-content');
  let restContent = $('#rest-content');
  
  place.click(function () {
    eventContent.removeClass('my-display');
    restContent.removeClass('my-display');
    eventContent.addClass('my-hide');
    restContent.addClass('my-hide');
    placeContent.removeClass('my-hide');
    placeContent.addClass('my-display');
  });
  
  event.click(function () {
    placeContent.removeClass('my-display');
    restContent.removeClass('my-display');
    placeContent.addClass('my-hide');
    restContent.addClass('my-hide');
    eventContent.removeClass('my-hide');
    eventContent.addClass('my-display');
  });
  
  rest.click(function () {
    eventContent.removeClass('my-display');
    placeContent.removeClass('my-display');
    eventContent.addClass('my-hide');
    placeContent.addClass('my-hide');
    restContent.removeClass('my-hide');
    restContent.addClass('my-display');
  });
  
  function setCookie(name, value) {
    document.cookie = name + "=" + encodeURIComponent(value) + "; ";
  }
  
  function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
  }
  
  $(".interest").click(function () {
    var interest_front = this.getAttribute("name");
    var city_front = getCookie("city");
    console.log(city_front);
    setCookie('interest', interest_front);
    
    var interestObj = {
      city: city_front,
      interest: interest_front
    };
    var url = 'http://localhost:8080/interest';
    var options = {
      "method": "POST",
      "mode": "cors",
      "headers": {
        "Content-Type": "application/json;charset=UTF-8"
      },
      "body": JSON.stringify(interestObj)
    };
    fetch(url, options);
  });
  
  
});




