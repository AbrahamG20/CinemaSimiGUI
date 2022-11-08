from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

#path = "C:\\Users\\Abraham\\Videos\\Captures\\prueba.mp4"

def load_model_checkpoint(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

model_checkpoint = 'model'
tokenizer, model = load_model_checkpoint(model_checkpoint)

def translate(sentences):
    result = []

    for i in range(len(sentences)):
        text = str(sentences[i])
        tokenized_text = tokenizer(text, return_tensors='pt')
        translation = model.generate(**tokenized_text)
        translated_text = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]
        result.append(translated_text)

    return result

#recog = recognize(path)
#s = sentences(recog)
