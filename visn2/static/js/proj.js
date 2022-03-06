$(function(){
    function create_content(datas){
        var content = $('<ul></ul>');
        $.each(datas['task_texts'], function(index, item){
            content.append($('<li>' + item + '</li>'));
        });
        $('#tasks').children().remove();
        $('#tasks').append(content);
    };
    function create_content2(datas){
        var content = $('<ul></ul>');
        $.each(datas['file_infos'], function(index, item){
            content.append($('<li>' + item + '</li>'));
        });
        $('#updates').children().remove();
        $('#updates').append(content);
    };

    $("body").on('click', '#proj_disp .row .col', function(){
        // alert($(this).attr('project_id'));
        project_id = $(this).attr('project_id');
        $.ajax({url: "/dashboard/project_view/" + project_id + '/', 
                dataType: "json",
                success: function(datas){
                                console.log(datas);
                                $('.project_name').text(datas['name']);
                                $('.project_deadline').text(datas['deadline']);
                                $('.project_discription').text(datas['discription']);
                                $('.file_number').text(datas['file_number']);
                                $('.create_user').text(datas['create_user']);
                                create_content(datas);
                                create_content2(datas);
                            },
                error: function(xhr, type){alert("'Ajax Error!'");}}
            );
    });

    $('#proj_disp .row .col').eq(0).trigger('click');

    // $("body").on('click', '#chat_ui', function(){
    //     $('#chat_li').css('display', 'block');
    //     $('#chatback').css('display', 'block');
    // });

    // $("body").on('click', '#x', function(){
    //     $('#chat_li').css('display', 'none');
    //     $('#chatback').css('display', 'none');
    // });

});