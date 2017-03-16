/**
 * Created by deonis on 13.03.17.
 */
$(document).ready(function () {
    if (window.location.hash == '#_=_') {
        history.pushState('',document.title,window.location.pathname)
    }

    var $form_comment_reply = $('#form_comment_reply');
    var $form_answer = $('#form_answer');

    load_content();

    $('#form_comment_reply').submit(function (event) {
        event.preventDefault();
        var msg = $(this).serialize();
        var url = $(this).attr('action');

         $.ajax({
          type: 'POST',
          url: url,
          data: msg,
          success: function(data) {

                $form_answer.hide();
                $form_answer.insertAfter('#form_parking');

                if (data['result'] == 'success') {
                    load_content();
                } else {
                    console.log(data['error']);
                }
          },
          error:  function(xhr, str){
	            alert('Возникла ошибка: ' + xhr.responseCode);
          }
        });

    });

    $('.container').on('click', '.comment-link', function (e) {
        e.preventDefault();
        var $replyLink = $(this);
        var message_id = $replyLink.attr('data-message-id');
        var parent_id = $replyLink.attr('data-parent-id');

        if (parent_id === undefined) parent_id = '';

        $form_comment_reply.trigger("reset");
        $form_comment_reply.find('input[name="message_id"]').val(message_id);
        $form_comment_reply.find('input[name="parent_id"]').val(parent_id);

        $form_answer.hide('slow', function () {
            $form_answer.insertAfter($replyLink.parent());
            $form_answer.show('slow');
        });
    });

    function load_content() {
        $.ajax({
            url: '/get_content/',
            success: function (data) {
                $('#content').html(data);
            }
        });
    }

});