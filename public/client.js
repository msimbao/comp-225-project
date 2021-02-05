// client-side js
// run by the browser each time your view template is loaded

// by default, you've got jQuery,
// add other scripts at the bottom of index.html

$(function() {
  console.log('hello world :o');
  
  $.get('/news', function(news) {
    news.forEach(function(newsItem) {
      $('<li></li>').text(newsItem).appendTo('ul#news');
    });
  });

  $('form').submit(function(event) {
    event.preventDefault();
    newsItem = $('input').val();
    $.post('/news?' + $.param({'newsItem': newsItem}), function() {
      
      //"POST /newsItem?newsItem=Hello HTTP/1.1" 
      $('<li></li>').text(newsItem).appendTo('ul#news');
      $('input').val('');
      $('input').focus();
    });
  });

});
