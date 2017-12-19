$(document).ready(function(){
    startpage();
    setEvent();
    setInputTagChangeEvent();

});

function setEvent(){

    $("#delete_button").click(function(){
        $("form").each(function(){
            var input = $(this).find(':input')
            input.val('');
        });
    });
    $('#sub_toggle_btn1').click(function(){
        $('#sub_input1').toggle("slide");
    });
    $('#sub_toggle_btn2').click(function(){
        $('#sub_input2').toggle("slide");
    });
    $('#sub_toggle_btn3').click(function(){
        $('#sub_input3').toggle("slide");
    });
    $('#sub_toggle_btn4').click(function(){
        $('#sub_input4').toggle("slide");
    });
    $('#sub_toggle_btn5').click(function(){
        $('#sub_input5').toggle("slide");
    });
    $('#sub_toggle_btn6').click(function(){
        $('#sub_input6').toggle("slide");
    });
    $('#sub_toggle_btn7').click(function(){
        $('#sub_input7').toggle("slide");
    });
    $('#sub_toggle_btn8').click(function(){
        $('#sub_input8').toggle("slide");
    });

}

function setInputTagChangeEvent(){

    setChangeEvent("#id_main_goal", "#main_goal_cell");

    for(var i = 1; i < 9; i++){
        var source_id = "#id_sub_goal" + i.toString();
        var target_id = ".sub_goal_cell" + i.toString();
        setChangeEvent(source_id, target_id);
    }

}
function startpage() {

    // $("#id_main_goal").change(function () {
    //     var str = $(this).val();
    //     $("#main_goal_cell").text(str);
    // });
    //
    // setChangeEvent("#id_main_goal", "#main_goal_cell");
    //
    // for(var i = 1; i < 9; i++){
    //     var source_id = "#id_sub_goal" + i.toString();
    //     var target_id = "#sub_goal_cell" + i.toString();
    //     setChangeEvent(source_id, target_id);
    // }

}

function setChangeEvent(source_id, target_id){
    $(source_id).change(function () {
        var str = $(source_id).val();
        $(target_id).text(str);
    });
}