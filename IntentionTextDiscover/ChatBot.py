import nltk
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class ChatBot:
	def __init__(self, context="", lastDialog="", lastQuestion=""):
		self.context = context
		self.dialog = lastDialog
	def getResponse(self, question):
		return "aguarde..."

	def RemoveStopWords(self, instancia):
		stopwords = set(nltk.corpus.stopwords.words('portuguese'))
		palavras = [i for i in instancia.split() if not i in stopwords]
		return (" ".join(palavras))

	def Stemming(self, instancia):
		stemmer = nltk.stem.RSLPStemmer()
		palavras = []
		for w in instancia.split():
			palavras.append(stemmer.stem(w))
		return (" ".join(palavras))

	def prepareTexts(self, texto):
	  #texto = RemoveStopWords(texto)
	  #texto = Stemming(texto)
	  return texto

	def showResults(self, valor):
		frase, resultado = valor
		#resultadoT = "Frase positiva" if resultado[0] == '1' else "Frase negativa"
		print(frase, ":", " se refere ao intenção: "+ resultado[0])
		#print(frase, ":", resultado[0])

	def analizer(self, classificador, vetorizador, frase):
		return frase, classificador.predict(vetorizador.transform([frase]))

	def generate_test_texts(self):
        # ['..text', 'CATEGORY']
        
		dados =  [
		['My xyz teste text', 'A_XYZ_TEST']
	   ]
		return dados

	def prepareAllData(self, dados):
		dados_tratados = []

		for dado in dados:
		  dado[0] =  self.prepareTexts(dado[0])
		  #print(dado[0])
		  dados_tratados.append(dado)
		  
		return dados_tratados

	def splitData(self, dados):
		quantidade_total = len(dados)
		percentual_para_treino = 0.75
		treino = []
		validacao = []

		for indice in range(0, quantidade_total):
			if indice < quantidade_total * percentual_para_treino:
				treino.append(dados[indice])
			else:
				validacao.append(dados[indice])

		return treino, validacao

	def prepare_text(self):
		dados = self.generate_test_texts()
		dados_tratados = self.prepareAllData(dados)

		return self.splitData(dados_tratados)


	def training(self, registros_de_treino, vetorizador):
		treino_comentarios = [registro_treino[0] for registro_treino in registros_de_treino]
		treino_respostas = [registro_treino[1] for registro_treino in registros_de_treino]

		treino_comentarios = vetorizador.fit_transform(treino_comentarios)

		return MultinomialNB().fit(treino_comentarios, treino_respostas)

	def simple_execute(self, registros_para_avaliacao):
		avaliacao_comentarios = [registro_avaliacao[0] for registro_avaliacao in registros_para_avaliacao]
		avaliacao_respostas   = [registro_avaliacao[1] for registro_avaliacao in registros_para_avaliacao]

		total = len(avaliacao_comentarios)
		acertos = 0
		for indice in range(0, total):
			resultado_analise = analizer(classificador, vetorizador, avaliacao_comentarios[indice])
			frase, resultado = resultado_analise
			acertos += 1 if resultado[0] == avaliacao_respostas[indice] else 0

		return acertos * 100 / total

	def execute(self, registros_para_avaliacao):
		avaliacao_comentarios = [registro_avaliacao[0] for registro_avaliacao in registros_para_avaliacao]
		avaliacao_respostas   = [registro_avaliacao[1] for registro_avaliacao in registros_para_avaliacao]

		total = len(avaliacao_comentarios)
		verdadeiros_positivos = 0
		verdadeiros_negativos = 0
		falsos_positivos = 0
		falsos_negativos = 0

		for indice in range(0, total):
			resultado_analise = analizer(classificador, vetorizador, avaliacao_comentarios[indice])
			frase, resultado = resultado_analise
			if resultado[0] == '0':
				verdadeiros_negativos += 1 if avaliacao_respostas[indice] != '1' else 0
				falsos_negativos += 1 if avaliacao_respostas[indice] == '1' else 0
			else:
				verdadeiros_positivos += 1 if avaliacao_respostas[indice] == '1' else 0
				falsos_positivos += 1 if avaliacao_respostas[indice] != '1' else 0

		return ( verdadeiros_positivos * 100 / total, 
				 verdadeiros_negativos * 100 / total,
				 falsos_positivos * 100 / total,
				 falsos_negativos * 100 / total
			   )
	def getItent(self, texto):
		registros_de_treino, registros_para_avaliacao = self.prepare_text()
		vetorizador = CountVectorizer(binary = 'false')
		classificador = self.training(registros_de_treino, vetorizador)
		return str(classificador.predict(vetorizador.transform([texto]))).replace("[",'').replace("]",'').replace("'",'')
		

	def getItentProba(self, texto, termo):
		registros_de_treino, registros_para_avaliacao = self.prepare_text()
		vetorizador = CountVectorizer(binary = 'false')
		classificador = self.training(registros_de_treino, vetorizador)
		ps  = pd.DataFrame(classificador.predict_proba(vetorizador.transform([texto])), columns=classificador.classes_)
		return ps.loc[0,termo]
	