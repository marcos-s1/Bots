# Bots

## AUTOMAÇÃO DA CRIAÇÃO DE VIDEOS COM PYTHON

### Ola pessoal ! Passando aqui pra mostrar meu novo projeto.

**Acompanhando o canal do Filipe Deschamps no youtube, me deparei com o projeto dele de desenvolver 4 robôs em JavaScript para a automatização da produção de videos. Dessa forma, resolvi implementar 3 desses robôs da minha forma e em Python. Implementei 
algumas mudanças na maneira como cada robô exerce sua função**

1. O primeiro Robô faz uma busca de um termo no Wikipedia e retorna tudo aquilo que for achado, limpa esses dados brutos e utiliza NLP para extrair sentenças e palavras chaves.
  1. Input do termo pelo usuario
  2. Pesquisa do termo na Wikipedia
  3. Retorno da pesquisa e limpeza dos dados
  4. Utilização de NLP para extração de sentenças e palavras-chave
  5. Salva os arquivo

2. O segundo robô faz uma busca no Google Images com as sentenças e keywords fornecidas pelo primeiro robô e, em seguida, seu respectivo download. Alem disso, faz um tratamento básico na imagem para que todas estejam de acordo para posterior montagem e renderização de vídeo.
  1. Carrega os arquivos salvos pelo primeiro robô
  2. Utiliza as sentenças, palavras-chave e termo para pesquisar Imagens no google
  3. Faz Download dessas Imagens
  4. Trata as imagens baixadas
  4. Formula as sentenças que aparecerão no video
  3. Salva os Arquivos

3. O  terceiro robô é responsável por utilizar o After Effects para montar o template pre-estabecido e renderizar o vídeo. 
  1. Carrega os arquivos salvos pelo segundo Robô
  2. Retorna as imagens baixadas e tratadas, alem das sentenças que aparecerão
  3. Monta o video com um template pre-estabelecido
  4. renderiza o video 
