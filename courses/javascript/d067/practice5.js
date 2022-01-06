"use strict";
const commentInput = document.getElementById('user-comment-input'); // 사용자 댓글 입력창
const userComments = document.getElementById('user-comments'); // 사용자 댓글 리스트 출력
const submitBtn = document.getElementById('user-comment-add'); //  사용자 댓글 추가 버튼
const comments = []; // 사용자 댓글목록 배열
const insults = ['shit', 'fuck', 'poo', 'dumb', 'ass'];
function buildElement(comment) {
    const element = document.createElement("div");
    element.className = "comment";
    element.innerHTML = comment;
    return element;
}
function displayComments(comments) {
    userComments.innerHTML = '';
    comments.forEach(value => userComments.appendChild(buildElement(value)));
}
function initInput() {
    commentInput.value = '';
}
function addComment() {
    let comment = commentInput.value;
    if (comment !== '') {
        insults.forEach(value => comment = comment.replace(new RegExp(value, "g"), "♥"));
        comments.push(comment);
        displayComments(comments);
        initInput();
    }
    else {
        alert('You need to give a comment !');
    }
}
submitBtn.addEventListener('click', addComment);
