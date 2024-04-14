window.onload = function () {
    // 요소를 찾아서 변수에 저장
    let messageTimeout = document.getElementById('message-timer');

    // 요소가 존재하는지 확인
    if (messageTimeout) {
        // 요소가 존재하면 5초 후에 숨김
        setTimeout(() => {
            messageTimeout.style.display = 'none';
        }, 5000);
    }
};
