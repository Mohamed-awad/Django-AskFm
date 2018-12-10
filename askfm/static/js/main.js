$(document).ready(function(){
    $(".nn i").click(function(){
      $(".nn i").removeClass("active");
      $(this).addClass("active");
    });

    $(".nav-item button").click(function(){
      $(".set-menu").toggle();
    });
});