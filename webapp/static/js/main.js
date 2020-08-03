$(function(){
    let socket = io.connect('https://social-calculator.herokuapp.com/');
    
    function appendOperation(operation){
        let op = '<li>' + operation + '</li>';
        let resultList = $('#result');
        resultList.children().last().remove();
        resultList.prepend(op);
    };

    socket.on('message', function(msg) {
        appendOperation(msg);
    });

    function sendToSocketio(msg){
        socket.send(msg);
    };

    function sendToFlask(i, operation, ii){
        $.ajax({
            type: "POST",
            url: "/send",
            data: {'i': i, 'operation': operation, 'ii': ii},
            success: function(data, textStatus, jqXHR){
                console.log(data);
                if (data.isValid) {
                    sendToSocketio(data.result)
                } else {
                    alert(data.result)
                };
            },
        });
    };

    $('#calculate').on('click', function() {
        let i = $('#i').val();
        let operation = $('#operation').val();
        let ii = $('#ii').val();
        sendToFlask(i, operation, ii);
    });
});