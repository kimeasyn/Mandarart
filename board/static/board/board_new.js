$(document).ready(function(){
    startpage();
});

function startpage() {
    $('#sub1_toggle_btn').click(function(){
        $('#sub_input').toggle("slide");
    })
}