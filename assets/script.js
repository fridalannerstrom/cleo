$(document).ready(function() {
    $("#click-me").mouseenter(function() {
        $("th").slideToggle("slow");
    });
    $("#click-me").mouseleave(function() {
        $("th").slideToggle("slow");
    });
});