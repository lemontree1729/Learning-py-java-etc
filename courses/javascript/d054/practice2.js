$("#file-button").on("click", () => {
    $("#file-input").click()
})
$("#file-input").on("change", (e) => {
    Array.from(e.target.files).forEach(file => {
        console.log(file.type)
        if (file.type.startsWith("image"))
            $("#container").append(`<div id='img-box'><img src=${URL.createObjectURL(file)}></div>`)
    })
})