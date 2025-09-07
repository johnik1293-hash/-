import wikipediaapi

wiki = wikipediaapi.Wikipedia('ru')

def explain(topic: str):
    page = wiki.page(topic)
    if not page.exists():
        return None
    summary = page.summary
    # очень кратко
    bullets = []
    for sec in page.sections:
        if len(bullets) >= 6:
            break
        bullets.append(f"<b>{sec.title}</b>: {sec.text[:180]}…")
    return summary[:400] + ('…' if len(summary) > 400 else ''), bullets
