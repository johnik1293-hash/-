import wikipediaapi
import random

wiki = wikipediaapi.Wikipedia('ru')

STOPWORDS = set("в во на и или но что как это эта этот которые которые из от для по над под при без со из-за из-под через между также тоже т.д. т.п.".split())

def make_quiz(topic: str, n: int = 5):
    page = wiki.page(topic)
    if not page.exists():
        return []
    text = page.summary
    sentences = [s.strip() for s in text.split('.') if len(s.split()) > 6]
    random.shuffle(sentences)
    quiz = []
    for s in sentences[:n]:
        words = [w.strip(',;:()«»\"').lower() for w in s.split()]
        words = [w for w in words if len(w) > 4 and w not in STOPWORDS]
        if not words:
            continue
        answer = random.choice(words)
        # маскируем слово
        question = s.replace(answer, '____')
        # дистракторы — похожие слова из того же текста
        pool = list({w for w in words if w != answer})
        random.shuffle(pool)
        options = [answer] + pool[:3]
        random.shuffle(options)
        quiz.append({
            'q': question.strip()+'.',
            'options': options,
            'answer': answer
        })
    return quiz
