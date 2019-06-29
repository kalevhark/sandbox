$.ajax({
    url:  '/feedback/list',
    type:  'get',
    dataType:  'json',
    success: function  (data) {
        let rows =  '';
        data.feedbacks.forEach(feedback => {
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
    $('[#myTable] > tbody').append(rows);
    $('.deleteBtn').each((i, elm) => {
        $(elm).on("click",  (e) => {
            deleteFeedback($(elm))
        })
    })
    }
});

function  deleteFeedback(el){
    feedbackId  =  $(el).data('id')
    $.ajax({
        url:  `/feedback/delete/${feedbackId}`,
        type:  'post',
        dataType:  'json',
        success:  function (data) {
            $(el).parents()[1].remove()
        }
    });
}