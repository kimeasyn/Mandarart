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

    //click event bind 부분 간소화 필요
    $('#sub_toggle_btn1').click(function(){
        $('#sub_input1').toggle("slide");
        $('#sub_input2').hide("slide");
        $('#sub_input3').hide("slide");
        $('#sub_input4').hide("slide");
        $('#sub_input5').hide("slide");
        $('#sub_input6').hide("slide");
        $('#sub_input7').hide("slide");
        $('#sub_input8').hide("slide");
    });
    $('#sub_toggle_btn2').click(function(){
        $('#sub_input1').hide("slide");
        $('#sub_input2').toggle("slide");
        $('#sub_input3').hide("slide");
        $('#sub_input4').hide("slide");
        $('#sub_input5').hide("slide");
        $('#sub_input6').hide("slide");
        $('#sub_input7').hide("slide");
        $('#sub_input8').hide("slide");
    });
    $('#sub_toggle_btn3').click(function(){
        $('#sub_input1').hide("slide");
        $('#sub_input2').hide("slide");
        $('#sub_input3').toggle("slide");
        $('#sub_input4').hide("slide");
        $('#sub_input5').hide("slide");
        $('#sub_input6').hide("slide");
        $('#sub_input7').hide("slide");
        $('#sub_input8').hide("slide");
    });
    $('#sub_toggle_btn4').click(function(){
        $('#sub_input1').hide("slide");
        $('#sub_input2').hide("slide");
        $('#sub_input3').hide("slide");
        $('#sub_input4').toggle("slide");
        $('#sub_input5').hide("slide");
        $('#sub_input6').hide("slide");
        $('#sub_input7').hide("slide");
        $('#sub_input8').hide("slide");
    });
    $('#sub_toggle_btn5').click(function(){
        $('#sub_input1').hide("slide");
        $('#sub_input2').hide("slide");
        $('#sub_input3').hide("slide");
        $('#sub_input4').hide("slide");
        $('#sub_input5').toggle("slide");
        $('#sub_input6').hide("slide");
        $('#sub_input7').hide("slide");
        $('#sub_input8').hide("slide");
    });
    $('#sub_toggle_btn6').click(function(){
        $('#sub_input1').hide("slide");
        $('#sub_input2').hide("slide");
        $('#sub_input3').hide("slide");
        $('#sub_input4').hide("slide");
        $('#sub_input5').hide("slide");
        $('#sub_input6').toggle("slide");
        $('#sub_input7').hide("slide");
        $('#sub_input8').hide("slide");
    });
    $('#sub_toggle_btn7').click(function(){
        $('#sub_input1').hide("slide");
        $('#sub_input2').hide("slide");
        $('#sub_input3').hide("slide");
        $('#sub_input4').hide("slide");
        $('#sub_input5').hide("slide");
        $('#sub_input6').hide("slide");
        $('#sub_input7').toggle("slide");
        $('#sub_input8').hide("slide");
    });
    $('#sub_toggle_btn8').click(function(){
        $('#sub_input1').hide("slide");
        $('#sub_input2').hide("slide");
        $('#sub_input3').hide("slide");
        $('#sub_input4').hide("slide");
        $('#sub_input5').hide("slide");
        $('#sub_input6').hide("slide");
        $('#sub_input7').hide("slide");
        $('#sub_input8').toggle("slide");
    });

}

function setInputTagChangeEvent(){

    setChangeEvent("#id_main_goal", "#main_goal_cell");

    var source_id = "";
    var target_id = "";
    for(var i = 1; i < 9; i++){
        source_id = "#id_sub_goal" + i.toString();
        target_id = ".sub_goal_cell" + i.toString();
        setChangeEvent(source_id, target_id);

        for(var j = 1; j < 9; j++){
            source_id = "#id_ach_way" + i.toString() + j.toString();
            target_id = "#ach_way" + i.toString() + j.toString();
            setChangeEvent(source_id, target_id);
        }
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