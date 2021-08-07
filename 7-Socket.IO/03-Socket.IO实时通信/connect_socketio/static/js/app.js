(function () {
    let socket = io();
    let output = document.querySelector('#output');

    // 向服务器发送my_event事件
    document.querySelector('.btn_my_event').onclick = e => {
        socket.emit('my_event', {});
    };

    // 侦听服务器返回的my_event_callback事件
    socket.on('my_event_callback', e => {
        output.innerHTML += `[${Date.now()}] my_event_callback from server<br>`;
    });

    // 向服务器发送login事件，并通过回调函数显示返回数据
    document.querySelector('.btn_login').onclick = e => {
        socket.emit('login', {name: 'xh'}, result => {
            output.innerHTML += `[${Date.now()}] ${result}<br>`;
        });
    };
})();
