$('form').submit(function(event) {
    event.preventDefault();
    $.ajax({
        url: "/choose_book",
        method: "POST",
        data: $(this).serialize()
    }).then(function(res) {
        $('#book_insert').html(res);
    })
})

counter_start = 0;
$('#start').click(function(){
    if(counter_start == 0){
        book_slot();
        counter_start ++;
    }
})

book_running = false;
function book_slot(){
    run_book = setInterval(choose_book, 70);
    book_running = true;
}

function choose_book(){
    $('#form_sub').trigger('click');
}

$('#stop').click(function(){
    stop_slot();
})

counter_stop = 0;
function stop_slot() {
    if(counter_stop == 0){
        book_running = false;
        clearInterval(run_book);
        chapter_slot();
        counter_stop ++;
    }
    else if(counter_stop == 1){
        chapter_running = false;
        clearInterval(run_chapter);
        verse_slot();
        counter_stop ++;
    }
    else if(counter_stop == 2){
        verse_running = false;
        clearInterval(run_verse);
        $('#get_link').trigger('click');
    }
}

$('#choose_chapter').click(function(event) {
    event.preventDefault();
    $.ajax({
        url: "/choose_chapter",
        method: "GET",
    }).then(function(res) {
        $('#chapter_insert').html(res);
    })
})

chapter_running = false;
function chapter_slot(){
    run_chapter = setInterval(choose_chapter, 70);
    chapter_running = true;
}

function choose_chapter(){
    $('#choose_chapter').trigger('click');
}


$('#choose_verse').click(function(event) {
    event.preventDefault();
    $.ajax({
        url: "/choose_verse",
        method: "GET",
    }).then(function(res) {
        $('#verse_insert').html(res);
    })
})

verse_running = false;
function verse_slot(){
    run_verse = setInterval(choose_verse, 70);
    verse_running = true;
}

function choose_verse(){
    $('#choose_verse').trigger('click');
}


$('#clear').click(function(){
    if(book_running == true){
        clearInterval(run_book);
        book_running = false;
        $('#book_insert').html('&nbsp;');
        }
    else if(chapter_running == true){
        clearInterval(run_chapter);
        chapter_running = false;
        $('#chapter_insert').html('&nbsp;');
    }
    else if(verse_running == true){
        clearInterval(run_verse);
        verse_running = false;
        $('#verse_insert').html('&nbsp;');
    }
    setTimeout(clear_results, 30);
    counter_stop = 0;
    counter_start = 0;
    $.ajax({
        url: "/clear_session",
        method: "GET",
    })
})

function clear_results(){
    $('#book_insert').html('&nbsp;');
    $('#chapter_insert').html('&nbsp;');
    $('#verse_insert').html('&nbsp;');
    $('#link_insert').html('&nbsp;');
}

$('#get_link').click(function(event) {
    event.preventDefault();
    $.ajax({
        url: "/verse_link",
        method: "GET",
    }).then(function(res) {
        $('#link_insert').html(res);
    })
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}