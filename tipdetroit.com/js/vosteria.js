/* =================================================================


  Template Name: Vosteria
  Description: Vosteria - Creative Agency & Portofolio OnePage HTML Template
  Author: Qoorasa
  Author URI: https://themeforest.net/user/qoorasa
  Version: 1.0

  Table of Content:
  01. Preloader / Window Load
  02. Icons
  03. Scrollspy Navbar
  04. Owl Carousel 2
  05. AJAX Contact Form


==================================================================== */

/* =================================================================
    01. Preloader / Window Load
==================================================================== */

$(window).on('load', function () {
    'use strict'

    // Fadeout Preloader
    $('#preloader').fadeOut();

    // Add Attribute for Hero Content Animation
    $('.qoo__hero__content__inner').attr('uk-scrollspy', 'cls: uk-animation-slide-bottom-small; target: .animation; delay: 100;');
});


$(function(){
    'use strict'

/* =================================================================
    02. Icons
==================================================================== */

    // Feather Icons
    feather.replace();

/* =================================================================
    03. Scrollspy Navbar
==================================================================== */

    $(window).scroll(function (event) {
        // Get scroll top offset
        var scrollTop = $(this).scrollTop();
        if(scrollTop >= 500) {
            // Enable navbar scroll spy
            UIkit.scrollspyNav('#navbar-scrollspy', {
                closest: 'li',
                scroll: true,
                overflow: false,
                offset: 60
            });
        }
    })

/* =================================================================
    04. Owl Carousel 2
==================================================================== */

    // Works Sections Owl Carousel 2 Options
    $('.qoo__works .owl-carousel').owlCarousel({
        loop: false,
        margin: 20,
        nav: false,
        autowidth: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 3
            }
        }
    });


    // Clients Sections Owl Carousel 2 Options
    $('.qoo__clients .owl-carousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        autowidth: false,
        autoplay: true,
        autoplayTimeout: 2000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 3
            },
            600: {
                items: 4
            },
            1000: {
                items: 5
            }
        }
    });

    // Testimonials Sections Owl Carousel 2 Options
    $('.qoo__testimonials .owl-carousel').owlCarousel({
        loop: false,
        margin: 10,
        nav: false,
        autowidth: false,
        autoplay: false,
        autoplayTimeout: 2000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 3
            }
        }
    });

/* =================================================================
    05. AJAX Contact Form
==================================================================== */

    $('form').on('submit', function (e) {

        e.preventDefault();

        $.ajax({
          type: 'post',
          url: 'php/mail.php',
          data: $('form').serialize(),
          beforeSend: function() {
            $("#button_submit").addClass('uk-hidden');
            $("#button_sending").removeClass('uk-hidden');
         },
          success: function () {
            $('#contact_form_success').removeClass('uk-hidden');
            $("#button_submit").removeClass('uk-hidden');
            $("#button_sending").addClass('uk-hidden');
            document.getElementById('contact_form').reset();
          }
        });

      });

})

/* =================================================================
    06. Google Sheets
==================================================================== */

/*!
 *
 * Google Sheets To HTML v0.9a
 *
 * To use, simply replace the "tq?key=" value in the
 * URL below with your own unique Google document ID
 *
 * The Google document's sharing must be set to public
 *
 */

google.load('visualization', '1', {
    packages: ['table']
});
var visualization;

function drawVisualization() {
    var query = new google.visualization.Query('https://docs.google.com/spreadsheets/d/1xdssiofwisVcTyAmUtyN5sfd94zBDxChSNwOJAyY7IQ/edit?usp=sharing');
    query.setQuery('SELECT  B, C, D, G, H, I, J, K');
    query.send(handleQueryResponse);
}

function handleQueryResponse(response) {
    if (response.isError()) {
        alert('There was a problem with your query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
    }
    var data = response.getDataTable();
    visualization = new google.visualization.Table(document.getElementById('table'));
    visualization.draw(data, {
        allowHtml: true,
        legend: 'bottom'
    });
}
google.setOnLoadCallback(drawVisualization);
