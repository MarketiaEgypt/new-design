$(function($) {

  "use strict";


/*=========================== scroll background ===========================*/

  $(window).scroll(function(){

    var wScroll = $(this).scrollTop();

    // Activate menu
    if (wScroll >50) {
      $('.navbar').addClass('active_sc');
    }
    else {
      $('.navbar').removeClass('active_sc');
    };
        
  });

  /*=========================== close scroll background ===========================*/
 

  /*=========================== click to section ===========================*/
 //smooth scrool
   // Add scrollspy to <body>
  $('body').scrollspy({target: ".navbar", offset: 50});   

  // Add smooth scrolling on all links inside the navbar
  $("#xeronav a").on('click', function(event) {
    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    }  // End if
  });
  /*=========================== click to section ===========================*/

 

    // Back to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
    } else {
      $('.back-to-top').fadeOut('slow');
    }
  });
  $('.back-to-top').click(function(){
    $('html, body').animate({scrollTop : 0},1500, 'easeInOutExpo');
    return false;
  });


  /*=========================== preloader ===========================*/
  // Wait for window load
  // $(window).on('load', function() {
  //    $(".se-pre-con").fadeOut("slow");;
  // });


  $(window).on('load', function () {
    if ($('.se-pre-con').length) {
      $('.se-pre-con').delay(1).fadeOut('slow', function () {
        $(this).remove();
      });
    }
  });
  /*=========================== preloader ===========================*/
  
  // Initiate the wowjs animation library
  new WOW().init();

  /*=========================== slick slider testimonial ===========================*/
  
  
 $('.slider-single').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.slider-nav',
	 autoplay: false,
});
$('.slider-nav').slick({
  slidesToShow: 5,
  slidesToScroll: 1,
  asNavFor: '.slider-single',
  dots: false,
  centerMode: true,
  focusOnSelect: true,
  centerPadding:50,
    arrows: true,
            prevArrow:"<button type='button' class='slick-prev pull-left'><i class='fas fa-arrow-left' aria-hidden='true'></i></button>",
            nextArrow:"<button type='button' class='slick-next pull-right'><i class='fas fa-arrow-right' aria-hidden='true'></i></button>",
    responsive: [{
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
      }
    }, {
      breakpoint: 640,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
      }
    }, {
      breakpoint: 420,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
    }
    }]

});
		

  /*=========================== slick slider testimonial ===========================*/




/*=========================== gallery js ===========================*/
var owls = $("#gallerys-owl");
    owls.owlCarousel({

        autoplay: true,
        autoplayTimeout:5000,
        autoplayHoverPause:true,
        items: 3,
        rtl:true,
        loop: true,
        center: false,
        margin: 30,
        stagePadding: 0,
        dots:false,
        nav:false,


        merge: false,
        mergeFit: true,
        autoWidth: false,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },
            600: {
                items: 2,
                nav: false
            },
            768: {
                items: 3,
                nav: false,
                loop: true
            }
        },
    });
/*=========================== gallery js ===========================*/




});


$(".slider").owlCarousel({
    rtl:true,
    loop: true,
    autoplay: true,
    autoplayTimeout: 2000, //2000ms = 2s;
    autoplayHoverPause: true,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true
        },
        600:{
            items:1,
            nav:false
        },
        1000:{
            items:3,
            nav:true,
            loop:false
        }
    }

});

$(document).ready(function () {
  let exist_script = $(".append-after-script");
  exist_script.after('<script src="https://apps.elfsight.com/p/platform.js" defer></script>');
})