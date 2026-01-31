a = ["Texas", "California", "Florida"] # states
b = ["Austin", "Sacramento", "Tallahassee"] # capital

res = {state:capital for state, capital in zip(a, b)}

print(res)