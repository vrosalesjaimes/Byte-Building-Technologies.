$(document).ready(function () {
    const $initial_form = $('.initial_form');
    const $form_admin = $('.form_admin');
    const $form_tablet = $('.form_tablet');
    const $admin_button = $('#admin');
    const $encargado_button = $('#encargado');
    const $return_encargado = $('.return_initial_form:first')
    const $return_admin = $('.return_initial_form:last')


    $initial_form.addClass('active');

    $admin_button.click(function () {
        $initial_form.fadeTo(500, 0, function () {
            $initial_form.removeClass('active');
            $form_admin.addClass('active');
            $initial_form.css('opacity', 1);
        });
    });

    $encargado_button.click(function () {
        $initial_form.fadeTo(500, 0, function () {
            $initial_form.removeClass('active');
            $form_tablet.addClass('active');
            $initial_form.css('opacity', 1);
        });
    });

    $return_encargado.click(function () {
        $form_tablet.fadeTo(500, 0, function(){
            $form_tablet.removeClass('active');
            $initial_form.addClass('active');
            $form_tablet.css('opacity', 1);
        })
    });

    $return_admin.click(function () {
        $form_admin.fadeTo(500, 0, function(){
            $form_admin.removeClass('active');
            $initial_form.addClass('active');
            $form_admin.css('opacity', 1);
        })
    });
})
