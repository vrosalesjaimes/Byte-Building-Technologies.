$(document).ready(function () {
    const $body = $('body');
    const $entrada = $('#category_entrada');
    const $platillo_fuerte = $('#category_plato');
    const $bebida = $('#category_bebida');
    const $postre = $('#category_postre');
    const $entrada_block = $('.entradas');
    const $platos_block = $('.platos_fuertes');
    const $bebidas_block = $('.bebidas');
    const $postres_block = $('.postres');
    const $categories = $('.content:first');

    $entrada.click(function () {
        $body.removeClass('body_initial');
        $categories.css('display', 'none');
        $entrada_block.css('margin-top','0%')
        $entrada_block.css('display', 'flex');
    })

    $platillo_fuerte.click(function () {
        $body.removeClass('body_initial');
        $categories.css('display', 'none');
        $platos_block.css('margin-top','0%')
        $platos_block.css('display', 'flex');
    })

    $bebida.click(function () {
        $body.removeClass('body_initial');
        $categories.css('display', 'none');
        $bebidas_block.css('margin-top','0%')
        $bebidas_block.css('display', 'flex');
    })

    $postre.click(function () {
        $body.removeClass('body_initial');
        $categories.css('display', 'none');
        $postres_block.css('margin-top','0%')
        $postres_block.css('display', 'flex');
    })
})