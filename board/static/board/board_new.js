$(document).ready(function(){
    startpage();
    setEvent();
    setInputTagChangeEvent();
    alert("!");
});

function setEvent(){

    $("#delete_button").click(function(){
        $("form").each(function(){
            var input = $(this).find(':input')
            input.val('');
        });
    });

    $('#sub1_toggle_btn').click(function(){
        $('#sub_input').toggle("slide");
    });

}

function setInputTagChangeEvent(){

    setChangeEvent("#id_main_goal", "#main_goal_cell");

    for(var i = 1; i < 9; i++){
        var source_id = "#id_sub_goal" + i.toString();
        var target_id = "#sub_goal_cell" + i.toString();
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