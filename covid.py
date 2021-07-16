import speech_recognition as sr

recognizer = sr.Recognizer()

questions = [
    "Onset of sympton",
    "Severity of symptoms",
    "Length of symptoms",
    "Loss of smell and taste",
    "Shortness of breath",
    "Cough",
    "Sneezing",
    "Runny or stuffy nose",
    "Sore Throat",
    "Fever",
    "Fatigue",
    "Headaches",
    "Body aches",
    "Diarrhea"
]

covid = 0
cold = 0
flu = 0
allergy = 0

def recognize():
    global covid, cold, flu, allergy, is_recognize

    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio).title()

            if text == 'One':
                allergy += 1
                is_recognize = True
            elif text == 'Two':
                flu += 1
                is_recognize = True
            elif text == 'Three':
                cold += 1
                is_recognize = True
            elif text == 'Four':
                covid += 1
                is_recognize = True
            else:
                is_recognize = False
                print('Speech invalid: ', text)
            
            print('You said: ', text)
            
            return is_recognize

        except Exception as e:
            is_recognize = False
            print('Speech not recognize. Try again.')

            return is_recognize

    except Exception as e:
        is_recognize = False
        print('Speech not recognize. Try again.')

        return is_recognize


if __name__ == '__main__':
    print('''
        Say the number according to stage.
        1 (one) = Weak
        2 (two) = Mild
        3 (three) = Worsen
        4 (four) = Worst
    ''')

    is_recognize = True

    for number, question in enumerate(questions):
        print('{}.'.format(number + 1), question)
        
        request = recognize()
        if not request:
            failed = True

            while failed:
                is_true = recognize()
                if is_true:
                    failed = False
        print()

    results =[covid, cold, flu, allergy]
    highest_score = max(results)
    
    symptom = list()
    for id, result in enumerate(results):
        if highest_score == result:
            if id == 0:
                symptom.append('Covid')
            elif id == 1:
                symptom.append('Cold')
            elif id == 2:
                symptom.append('Flue')
            elif id == 3:
                symptom.append('Allergy')

    if len(symptom) > 1:
        print('You have either {}'.format(symptom))
    else:
        print('You have {}'.format(symptom))

