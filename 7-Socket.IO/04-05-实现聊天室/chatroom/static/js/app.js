(function () {
    let input, output, btnSend, nameInput;
    let socket;

    function sendMessage() {
        let name = nameInput.value;
        let msg = input.value;
        if (msg) {
            // 向服务器发送消息
            socket.emit('msg', {
                username: name,
                content: msg
            });
            // 清空输入框
            input.value = '';
        }
    }

    /*
    * 处理msg事件
    * @param {string} msg - 服务器发来的消息
    * */
    function socketMessageHandler(msg) {
        output.innerHTML += `${msg.from}: ${msg.content}<br>`

        // 将文字滚动到底端
        output.scrollTop = output.scrollHeight
    }

    function inputKeyupHandler(e) {
        // 当按下回车键时发送数据
        if (e.key === 'Enter') {
            sendMessage();
        }
    }

    function btnSendClickedHandler() {
        sendMessage();
    }

    function findElements() {
        input = document.querySelector('#input');
        output = document.querySelector('#output');
        btnSend = document.querySelector('#btn-send');
        nameInput = document.querySelector('#username');
    }

    function connectServer() {
        // 通过指定路径连接服务器
        socket = io({path: '/chatroom'});
    }

    function addListeners() {
        input.onkeyup = inputKeyupHandler;
        btnSend.onclick = btnSendClickedHandler;

        // 侦听服务器发来的msg事件
        socket.on('msg', socketMessageHandler);
    }

    function main() {
        findElements();
        connectServer();
        addListeners();
    }

    main();
})();
