import speech_recognition as sr
import openai

openai.api_key = ""

def generate_text(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        max_tokens = 2048,
        n = 1,
        stop = None,
        temperature =0.5,
    )
    message = completions.choises[0].text
    return message.strip()

# Cria uma instância da classe Recognizer
r = sr.Recognizer()

# Define o microfone como fonte de áudio
with sr.Microphone() as source:
    print("Fale alguma coisa:")
    # Escuta o áudio da fonte
    audio = r.listen(source)
# Usa o reconhecedor de fala do Google para transcrever o áudio
try:
    text = r.recognize_google(audio, language='pt-BR') 
    print(generate_text(text))
except sr.UnknownValueError:
    print("Não entendi o que você disse.")
except sr.RequestError as e:
    print(f"Não foi possível se comunicar com o serviço de reconhecimento de fala; {e}")
