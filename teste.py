import Algorithmia

input = {
  "articleName": "celular",
  "lang": "pt"
}
client = Algorithmia.client('simpH1sdB8f0kKgeKK+zp5KfmEE1')
algo = client.algo('web/WikipediaParser/0.1.2')
algo.set_options(timeout=300) # optional
result = algo.pipe(input).result
print(result['content'])