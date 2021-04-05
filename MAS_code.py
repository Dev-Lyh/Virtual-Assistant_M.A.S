#region IMPORT
import speech_recognition as sr #o "as" é um renome de algo. Usamos para facilitar a escrita do programa;
import pyttsx3 
import pywhatkit
from googletrans import Translator
import wikipedia
from falas import * #o 'from' é para importar outros scripts para esse (basicamente o <link> do html);
from random import choice
from datetime import datetime
#endregion IMPORT

wikipedia.set_lang('pt')
engine = pyttsx3.init()
engine.setProperty('rate', 150)

voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)

#region WindowUi
 #--LAYOUT

 #--WINDOW

#endregion WindowUi

#region DEFS

def reproduz_voz(frase):
    engine.say(frase)
    engine.runAndWait() #runAndWait é um comando "executar"

def processar_voz(): #def são as funções;
    rec = sr.Recognizer() #e as váriaveis são escritas sem um préfixo antes;

#endregion DEFS

#region FRASES
    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        while True:

            try:
                voz = rec.listen(s)
                entrada = rec.recognize_google(voz, language='pt')
                print(f'Você disse: {entrada}') #f=string
                entrada = entrada.lower()
            #region RESPOSTAS
                if entrada == 'oi' or entrada == 'olá':
                    resposta = choice(cumprimentar)
                    print(resposta)
                    reproduz_voz(resposta)

                elif entrada == 'como vai' or entrada == 'como você está':
                    resposta = choice(como_esta)
                    print(resposta)
                    reproduz_voz(resposta)
                
                elif entrada == 'sim estou bem' or entrada == 'estou bem também':
                    resposta = choice(humano_bem)
                    print(resposta)
                    reproduz_voz(resposta)
                
                elif entrada == 'horas' or entrada == 'que horas são' or entrada == 'quais são as horas':
                    now = datetime.now()
                    hora_de_agora = (f'{now.hour}:{now.minute}')
                    print(hora_de_agora)
                    reproduz_voz(hora_de_agora)
                
                elif entrada == 'que dia é hoje' or entrada == 'dia de hoje' or entrada == 'você sabe que dia é hoje' or entrada == 'data':
                    now = datetime.now()
                    dia_de_hoje = (f'{now.day}/{now.month}/{now.year}')
                    print(dia_de_hoje)
                    reproduz_voz(dia_de_hoje)
                
                elif entrada == 'obrigado' or entrada == 'obrigada':
                    resposta = choice(dnd)
                    print(resposta)
                    reproduz_voz(resposta)
            #endregion RESPOSTAS
            #region PIADAS KK
                elif entrada == 'conte me uma piada' or entrada == 'me conte uma piada' or entrada == 'conte uma piada' or entrada == 'piada':
                    resposta = choice(piadas)
                    print(resposta)
                    reproduz_voz(resposta)
                
                elif entrada == 'conte me mais uma piada' or entrada == 'me conte mais uma piada':
                    resposta = choice(outra_piada)
                    print(resposta)
                    reproduz_voz(resposta)
                
                elif entrada == 'me conte mais uma' or entrada == 'conte me mais uma' or entrada == 'outra por favor':
                    resposta = choice(mais_piada)
                    print(resposta)
                    reproduz_voz(resposta)
            #endregion
            #region linksDePesquisa
                elif 'wikipédia' in entrada:

                    termo = entrada.split('wikipédia')
                    termo_da_pesquisa = termo[1]
                    reproduz_voz(f'Pesquisando por {termo[1]} na wikipedia')
                    pesquisa = wikipedia.page(termo_da_pesquisa)
                    reproduz_voz(f'Achamos a pagina {pesquisa.title} no wikipedia')
                    reproduz_voz('Agora estamos buscando o conteúdo')
                    print(f'Fonte: {pesquisa.url}')
                    reproduz_voz(pesquisa.content)

                elif 'youtube' in entrada:
                    termo = entrada.split('youtube')
                    termo_da_pesquisa = termo[1]
                    pywhatkit.playonyt(termo_da_pesquisa)
                
                elif 'buscar' in entrada:
                    termo = entrada.split('buscar')
                    termo_da_pesquisa = termo[1]
                    reproduz_voz(f'Buscando por {termo[1]} no google')
                    pywhatkit.search(termo_da_pesquisa)

                elif 'google' in entrada:
                    termo = entrada.split('google')
                    termo_da_pesquisa = termo[1]
                    reproduz_voz(f'Pesquisando por {termo[1]} no google')
                    pywhatkit.search(termo_da_pesquisa)
            #endregion linksDePesquisa
            
            except sr.UnknownValueError:
                resposta = choice(dont_understand)
                print(resposta)
                reproduz_voz(resposta)
#endregion FRASES

assistente_virtual = processar_voz() #até aqui, o programa consegue entender o que a gente fala e consegue, também, transcrever o que nós falamos.
