// Uses the jQuery API to add red class to header tag and turn it
// red when the div#red_header tag is clicked

$('div#red_header').click(function () {
    $('header').addClass('red');
  });
