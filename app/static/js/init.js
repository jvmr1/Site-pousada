(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space

/*
$(document).ready(function(){
  $('.carousel').carousel();
});

$('.carousel.carousel-slider').carousel({
  fullWidth: true
});
*/

  $(document).ready(function () {
    $('.dropdown-button').dropdown({
      constrainWidth: false,
      hover: true,
      belowOrigin: true,
      alignment: 'left'
    });

    // JAVASCRIPT START HERE //
     $('.carousel').carousel({indicators: true});


    //$('.carousel-slider').carousel({ fullWidth: true });
  });


   // move next carousel
   $('.moveNextCarousel').click(function(e){
      e.preventDefault();
      e.stopPropagation();
      $('.carousel').carousel('next');
   });

   // move prev carousel
   $('.movePrevCarousel').click(function(e){
      e.preventDefault();
      e.stopPropagation();
      $('.carousel').carousel('prev');
   });

   document.addEventListener('DOMContentLoaded', function() {
var elems = document.querySelectorAll('select');
var instances = M.FormSelect.init(elems, options);
});

// Or with jQuery

$(document).ready(function(){
$('select').formSelect();
});


       document.addEventListener('DOMContentLoaded', function() {
         var elems = document.querySelectorAll('.datepicker');
         var instances = M.Datepicker.init(elems, options);
       });

       // Or with jQuery

       $(document).ready(function(){
         $('.datepicker').datepicker({
           showClearBtn: true
         });
       });

       document.addEventListener('DOMContentLoaded', function() {
         var elems = document.querySelectorAll('.modal');
         var instances = M.Modal.init(elems, options);
       });

       // Or with jQuery

       $(document).ready(function(){
         $('.modal').modal();
       });


           $(document).ready(function () {
             $('.dropdown-button').dropdown({
               constrainWidth: false,
               hover: true,
               belowOrigin: true,
               alignment: 'left'
             });

             // JAVASCRIPT START HERE //
             $('.slider').slider({
               indicators: true,
               height: 400,
               transition: 500,
               interval: 6000
             });



           });


           document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.materialboxed');
    var instances = M.Materialbox.init(elems, options);
  });

  // Or with jQuery

  $(document).ready(function(){
    $('.materialboxed').materialbox();
  });

  $(document).ready(function() {
    $('input#input_text, textarea#textarea2').characterCounter();
  });
