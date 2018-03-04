def parsedict_kw(data):
    text=[data ["keywords"][i]["text"] for i in range(len(data["keywords"]))]

def parsedict_emotion(data):
    emotion_data=[data ["keywords"][i]["emotion"] for i in range(len(data["keywords"]))]
