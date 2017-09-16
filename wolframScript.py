import wolframalpha
client = wolframalpha.Client(L7QYU9-K6EXU2794L)

mekaInput = "x^2==x+1" #this will later be what the network returns
res = client.query(mekaInput) #this is the query to wolframalpha
img = "empty image"
for pod in res.pods:
    if (pod.title=="Result"):
        for (sub in pod.subpod)
            if (sub.title==1):
                
jnk = WolframAlpha["x^2==x+1",IncludePods->{"Solution"},PodStates->{"Solution__Step-by-step solution"}]
