function  deleteFeedback(el){
    feedbackId  =  $(el).data('id')
//    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    $.ajax({
//        beforeSend: function(xhr, settings) {
//            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//                xhr.setRequestHeader("X-CSRFToken", csrftoken);
//            }
//        },
        url:  `/feedback/delete/${feedbackId}`,
        type:  'post',
        dataType:  'json',
        success:  function (data) {
            $(el).parents()[1].remove()
        }
    });
}

$.ajax({
    url:  '/feedback/list/',
    type:  'get',
    dataType:  'json',
    success: function  (data) {
        let rows =  '';
        data.feedbacks.forEach(feedback => {
        console.log(feedback.feedback_name);
        rows += `
        <tr>
            <td>${feedback.feedback_name}</td>
            <td>${feedback.feedback_contact}</td>
            <td>${feedback.feedback_text}</td>
            <td>
                <button class="btn deleteBtn" data-id="${feedback.id}">Delete</button>
                <button class="btn updateBtn" data-id="${feedback.id}">Update</button>
            </td>
        </tr>`;
    });
    $('#myTable > tbody').append(rows);
    $('.deleteBtn').each((i, elm) => {
        $(elm).on("click",  (e) => {
            deleteFeedback($(elm))
        })
    })
    }
});

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});