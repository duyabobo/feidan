function third_shopping_list() {
    $.get(
        '/shopping/list/third/' + $('body > div.container > div > div.active > a').attr('class') + '/',
        function(data, status) {
            $('body > div.third_shopping_list').html(data);
        }
    );
}
$(document).on("click", ".second_shopping_item", function () {
    $('body > div.container > div > div').removeClass('active');
    $(this).addClass('active');
    third_shopping_list();
});
