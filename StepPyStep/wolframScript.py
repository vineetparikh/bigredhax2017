import wolframalpha
client = wolframalpha.Client("L7QYU9-K6EXU2794L")
mekaInput = "integrate(x^2,x)" #this will later be what the network returns
res = client.query(mekaInput) #this is the query to wolframalpha

print(next(res.results).text) #test: prints plaintext of all results
