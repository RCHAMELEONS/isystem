$(document).ready(function () {
    $('input[name="phone_number"]').mask("8 (999) 999-9999");

    $('input[name="date"]').datepicker();

    $('input[name="date_birth"]').datepicker();

    $('input[name="date_document"]').datepicker();

    $("select").chosen();

    $('.fancy').fancybox();

    $('.q-answers__head').click(function(e){
        e.preventDefault();

        $('.q-answers__head').removeClass('q-answers__head_active');
        $(this).addClass('q-answers__head_active');

        var curBlock = $(this).siblings('.q-answers__body');
        $('.q-answers__body').not(curBlock).hide();
        curBlock.fadeToggle('fast');
    });

    $('.lk-element__head').click(function(e){
        e.preventDefault();

        $('.lk-element__head').removeClass('lk-element__head_active');
        $(this).addClass('lk-element__head_active');

        var curBlock = $(this).siblings('.lk-element__body');
        $('.lk-element__body').not(curBlock).hide();
        curBlock.fadeToggle('fast');
    });
});