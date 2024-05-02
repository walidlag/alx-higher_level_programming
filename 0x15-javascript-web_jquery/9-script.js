// script that fetches and displays the value of hello from that fetch in the HTML tag

$('document').ready(
    ()=>{
        $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data)=>{
            $('DIV#hello').text(data.hello);
        });
    });
