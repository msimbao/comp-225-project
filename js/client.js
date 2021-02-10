// client-side js
// run by the browser each time your view template is loaded

// by default, you've got jQuery,
// add other scripts at the bottom of index.html


$(function() {
  getNews();
  console.log('hello world :o');
  function getNews(){
      $.get('/news', function(news) {
        // console.log(news)
      news.forEach(function(newsItem) {
        console.log(newsItem['title'])
      // $('<li class="card newsItem"></li>').text(newsItem.title).appendTo('ul#news');
        $('<a href="'+newsItem.url+'"><li class="card newsItem"><img width="150px" src="'+newsItem.image+'"><div class="articleWords"><p>'+newsItem.title+'</p><h6>'+newsItem.authors+'</h6></div></li></a>').appendTo('ul#news');
    });
  });
  }


  $('form').submit(function(event) {
    $("ul#news").empty();
    event.preventDefault();
    newsItem = $('input').val();
    $.post('/news?' + $.param({'newsItem': newsItem}), function(news) {
      
      news.forEach(function(newsItem) {
        console.log(newsItem['title'])
        $('<a href="'+newsItem.url+'"><li class="card newsItem"><img width="150px" src="'+newsItem.image+'"><div class="articleWords"><p>'+newsItem.title+'</p><h6>'+newsItem.authors+'</h6></div></li></a>').appendTo('ul#news');
      });
      //"POST /newsItem?newsItem=Hello HTTP/1.1" 
      // $('<li></li>').text(newsItem).appendTo('ul#news');
      $('input').val('');
      $('input').focus();
    });

  });

});
