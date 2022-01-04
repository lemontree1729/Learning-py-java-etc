"use strict";
const userList = document.getElementById("user-list");
const userInfo = document.querySelectorAll(".user-info");
function addUser() {
    const temp = [];
    userInfo.forEach(v => {
        const input = v;
        if (input.value) {
            temp.push(`<div class="user">${input.id.replace("user-", "")}: ${input.value}</div>`);
            input.value = "";
        }
    });
    if (temp.length === 3)
        userList.innerHTML += temp.join("");
}
document.getElementById("user-add").addEventListener("click", addUser);
