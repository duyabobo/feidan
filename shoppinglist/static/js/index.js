function third_shopping_list() {
    $.get(
        '/shopping/list/third/' + $('body > div.container > div > div.active > a').attr('class') + '/',
        function(data, status) {
            $('body > div.container > div.third_shopping_list').html(data);
        }
    );
}
function third_shopping_list_tag() {
    $.get(
        '/shopping/list/second_tag/' + $('body > div.container > div > div.active > a').attr('class') + '/',
        function(data, status) {
            $('body > div.container > div.second_shopping_tag_list').html(data)
        }
    )
}
function get_pager() {
    $.get(
        '/shopping/list/get_pager/' + $('body > div.container > div > div.active > a').attr('class') + '/',
        function(data, status) {
            $('body > div.container > div.page_info').html(data)
        }
    )
}
function click_second_or_tag() {
    third_shopping_list();
    third_shopping_list_tag();
    get_pager();
}
// todo 增加 tag 点击事件
$(document).on("click", ".second_shopping_item", function () {
    $('body > div.container > div > div').removeClass('active');
    $(this).addClass('active');
    click_second_or_tag();
});
