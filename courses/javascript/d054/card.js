$("#prev").on("click", () => { $(".card").last().after($(".card").first()) })
$("#next").on("click", () => { $(".card").first().before($(".card").last()) })