from transformers import pipeline

# Modelos a comparar
models = {
    "BART": "facebook/bart-large-mnli",
    "mDeBERTa": "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"
}

# Etiquetas base del sistema
labels = [
    "urgencia o presión para actuar inmediatamente",
    "solicitud de dinero o transferencia",
    "suplantación de identidad",
    "amenaza o intimidación",
    "manipulación emocional",
    "chantaje emocional",
    "autoridad",
    "culpa",
    "aislamiento o secreto",
    "falsa emergencia"
]

# Casos de prueba reales (ingeniería social)
tests = [
    "Necesito que me transfieras el dinero ahora mismo, es urgente.",
    "Soy tu hijo, estoy en problemas, no le digas a nadie.",
    "Si no haces el pago hoy, tendrás consecuencias.",
    "Solo confía en mí, soy del banco y necesito tus datos.",
]

def run_model(name, model_id):
    print(f"\n\n================ {name} ================")
    
    classifier = pipeline(
        "zero-shot-classification",
        model=model_id
    )

    for text in tests:
        result = classifier(text, labels, multi_label=True)

        print(f"\nTexto: {text}")
        for label, score in zip(result["labels"][:3], result["scores"][:3]):
            print(f" - {label}: {round(score*100, 2)}%")


for name, model in models.items():
    run_model(name, model)