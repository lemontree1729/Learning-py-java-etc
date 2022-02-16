### A Pluto.jl notebook ###
# v0.18.0

using Markdown
using InteractiveUtils

# ╔═╡ 3c60e95e-fda6-42c5-b13d-18c7ec827b0a
buffer = IOBuffer();

# ╔═╡ fee4c1e2-b39f-45f7-a80b-04e71e72e42e
begin
	k=0
	for i in 1:10
		k += i
		println(buffer, k)
	end
	take!(buffer) |> String |> Text
end

# ╔═╡ 64d12d96-70d9-4845-8f60-c40e9b7d1193
k

# ╔═╡ cd5f8883-3b0a-4b4d-8fe8-7e472ac85aec
a = [1,2,3]

# ╔═╡ 8e73abb5-a3c2-4ce1-a15f-65d9b03b4ea5
b = [2,3,4]

# ╔═╡ e253d42c-6fd3-49fd-a4ba-d7250bc07f58
a.*b

# ╔═╡ e6209883-4db7-4503-b2cf-ea0b0053d80d
cost(x, y) = sum((x.-y).^2)

# ╔═╡ 6c874941-9058-4c75-8c47-828d08a231ee
x=[2,1];y=[2,0];

# ╔═╡ Cell order:
# ╠═3c60e95e-fda6-42c5-b13d-18c7ec827b0a
# ╠═fee4c1e2-b39f-45f7-a80b-04e71e72e42e
# ╠═64d12d96-70d9-4845-8f60-c40e9b7d1193
# ╠═cd5f8883-3b0a-4b4d-8fe8-7e472ac85aec
# ╠═8e73abb5-a3c2-4ce1-a15f-65d9b03b4ea5
# ╠═e253d42c-6fd3-49fd-a4ba-d7250bc07f58
# ╠═e6209883-4db7-4503-b2cf-ea0b0053d80d
# ╠═6c874941-9058-4c75-8c47-828d08a231ee
