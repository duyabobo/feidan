$(document).ready(function(){
    $('body > div.container > div > div:nth-child(1)').addClass('active');
    third_shopping_list();
});
function third_shopping_list() {
    $.get(
        '/shopping/list/third/' + $('body > div.container > div > div.active > a').attr('class'),
        function(data, status) {
            $('body > div.third_shopping_list').html(data);
        }
    );
}
