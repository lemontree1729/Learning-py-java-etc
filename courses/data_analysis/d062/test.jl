a = Dict(:a => "b", :b => "c")
foreach(println, [1, 2, 3])
a |> x -> println, x |> foreach
foreach(println, a)
print([1, 2, 3])
for i in a
    print(i)
end