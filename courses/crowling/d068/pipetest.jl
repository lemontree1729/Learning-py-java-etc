using Pipe
using Base: Fix1
@pipe "123" |> parse(Int, _) |> println
@pipe (Int, "123") |> parse(_...) |> println
@macroexpand @pipe "123" |> parse(Int, _) |> println
# x -> parse(Int, x), Base.Fix1(parse, Int), x -> parse(Int, _)(for Pipe)
@macroexpand @pipe (Int, "123") |> parse(_...) |> println
@macroexpand @assert 1 == 1.0
@pipe readline() |> split(_, " ") |> map(Fix1(parse, Int), _) |> filter(>(1), _) |> println
# input: 1 2 3 => output: [2, 3]
using Chain
@chain readline() begin
    split(" ")
    map(Fix1(parse, Int), _)
    filter(>(1), _)
    print
end

macroexpand(Main, :(@pipe "123" |> parse(Int, _) |> println))
# macroexpand not worK????