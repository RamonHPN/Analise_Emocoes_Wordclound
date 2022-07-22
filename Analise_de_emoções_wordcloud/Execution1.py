import pandas as pd
import tweepy
import matplotlib.pyplot as plt

# Para ter acesso a API do twitrer:
# Será necessário ter uma conta no twitter, entrar no twitter developer portal
# e obter as chaves da API e o bearer token

# Usei o token aqui
bearertoken = 'AAAAAAAAAAAAAAAAAAAAAGgofAEAAAAAc3WYAe04BtJapfxF2JOlEzZczOE%3DQyVbp0nqlQTmm3CRnOTbxgFNy72wAQZUe4ka6rRGhNoquKRY2I'
# É necessário inicializar o Client passando o seu token 
client = tweepy.Client(bearertoken)

# Nessa query definimos o que queremos buscar com o search_recent_tweets
query = client.search_recent_tweets("Covid19 lang:pt -is:retweet", max_results=100)

# Coleto os dados dessa query
tweets = query.data

# Dou um print no texto desses dados
for tweet in tweets:
    print(tweet.text)

# Aqui é agrupado os tweets em um dataframe
tweets_list = [[tweet.text] for tweet in tweets]
df = pd.DataFrame(tweets_list,columns=['Texto'])
pd.options.display.max_colwidth = 130 
print(df.head())

# Aqui eu junto todos esses tweets em uma string
string = pd.Series(df['Texto'].values).str.cat(sep = " " )
print(string)

# Defino alguns caracteres que não são importantes
caracteres = "#@-"

# Retiro eles da string
for i in range(len(caracteres)):
    string = string.replace(caracteres[i],"")
print(string)

# Começo o processo para a criação da nuvem de palavras
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)
# Essas são as palavras que eu não quero que apareçam
stopwords.update(["será","foi","até","nas","entre","aos","Eleicoes2022",'cada','fim',
                  "Eleições2022","RT","das","está","há","por","de",'dar','tô','era',
                  'pois','em','um','da','ser','aqui','vou','dos','ter','não','Nem','gente',
                  'ao','sou','seu','à','n','se','esse','uma','mais','ele','dessa', 'hora',
                  'fazendo','você','pode','essa','é','mas','segue','pra','estou','já',
                  'isso','vez','para','muito','pelo','pela','são', 'na','abixo','nem',
                  'vamos','https','t','co','c','New','eu','seis','retweets','área','teve',
                  'ano','pessoa','likes','vai','que','ou','anos','7dias','tirou','sendo',
                  'tem','q','0','O','e','os','assim','só','mesmo','tá','pro','votar',
                  'pessoas','vc',"indo",'tudo','link','nos','varios','como','indo','dia',
                  'quem','faltam','horas','sabe','estão','dias','votou','tinha','bem','então',
                  'Leia','ainda','deve','acima','próxima','desde','às','desta','nosso',
                  'queria','diz','fica','usa','sobre','vcs','COVID19','também','sem','nada',
                  'vão','hoje','eles','faz','têm','toda','seus','PORQUE','além','sua','contra',
                  'pedindo'])

# Defino as configurações como tamanho, cor, fonte
wordcloud = WordCloud(width=1600, stopwords=stopwords,height=800,
                      max_font_size=200, collocations=False, 
                      background_color='black').generate(string)
# Por fim, gero a word cloud
plt.figure(figsize=(40,30))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

