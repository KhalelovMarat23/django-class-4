function getPost(slug) {
    $('#edit-img').val('')
    $('#edit-post').attr('action', `/post/${slug}/update`)
    $.ajax({
        url: `/post/${slug}/json`
    }).done(function(res){
        setPostVal(res)
    })
}


function setPostVal(post) {
    $('#edit-title').val(post.title)
    $('#edit-desc').val(post.description)  
    $('#edit-img').attr('src', `/media/${post.image}`)

    const categories = $('#edit-category option')

    for (const category of categories) {
        if ($(category).val() == post.category) {
            $(category).attr('selected', true)
        }
    }  
    
    const tags = $('#edit-tags option')

    for (const tag of tags) {
        if ($(tag).val() == post.tag) {
            $(tag).attr('selected', true)
        }
    }
}