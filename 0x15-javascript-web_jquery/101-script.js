$(document).ready(function () {
  $('DIV#add_item').on('click', function (event) {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', function (event) {
    $('UL.my_list li:last-child').last().remove();
  });
  $('DIV#clear_list').on('click', function (event) {
    $('UL.my_list').empty();
  });
});
