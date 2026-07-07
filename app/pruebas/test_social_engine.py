from app.motores.social_engine import social_engine

test_cases = [
    "Necesito que me transfieras el dinero ahora mismo, es urgente.",
    "Soy tu hijo, estoy en problemas, no le digas a nadie.",
    "Si no haces el pago hoy tendrás consecuencias.",
    "Solo confía en mí, soy del banco y necesito tus datos."
]

for text in test_cases:
    print("\n==============================")
    print("TEXTO:", text)

    result = social_engine.analizar_texto(text)

    print("RESULTADO:")
    print(result)