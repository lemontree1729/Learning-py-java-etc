colors.sort()
$(() => { colors.forEach(color => $(".color-list").append("<div class='color-item'>" + color + "</div>")) })
$("#color-input").on("propertychange change keyup paste input", (e) => {
    $(".color-list").html("")
    colors.forEach(color => {
        if (color.includes($(e.target).val()))
            $(".color-list").append("<div class='color-item'>" + color + "</div>")
    })
})
$("#color-input").on({
    focus: (e) => { $(".color-list").addClass("show") },
    blur: (e) => {
        if (!$(e.target).hasClass("color-item"))
            $(".color-list").removeClass("show")
    }
})
$(".color-list").on({
    mousedown: (e) => {
        if ($(e.target).hasClass("color-item")) {
            $("#color-input").val($(e.target).text())
            $(".color-box").css("background", $(e.target).text())
            $(".color-list").removeClass("show")
        }
    }
})