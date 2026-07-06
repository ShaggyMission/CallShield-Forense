from transformers import pipeline


# =========================
# CONFIGURACIÓN DEL MODELO
# =========================
MODEL_NAME = "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"


# =========================
# ETIQUETAS DEL SISTEMA
# =========================
SOCIAL_LABELS = [
    "urgencia o presión para actuar inmediatamente",
    "solicitud de dinero o transferencia",
    "suplantación de identidad",
    "amenaza o intimidación",
    "manipulación emocional",
    "chantaje emocional",
    "autoridad o institución",
    "culpa",
    "aislamiento o secreto",
    "falsa emergencia",
    "obtención de información confidencial"
]


# =========================
# MAPEO A SALIDA INTERNA
# =========================
LABEL_MAPPING = {
    "urgencia o presión para actuar inmediatamente": "urgencia",
    "solicitud de dinero o transferencia": "solicitud_economica",
    "suplantación de identidad": "suplantacion",
    "amenaza o intimidación": "amenaza",
    "manipulación emocional": "manipulacion_emocional",
    "chantaje emocional": "chantaje_emocional",
    "autoridad o institución": "autoridad",
    "culpa": "culpa",
    "aislamiento o secreto": "aislamiento",
    "falsa emergencia": "falsa_emergencia",
    "obtención de información confidencial": "info_confidencial"
}


# =========================
# ESTADO BASE (SI FALLA EL MODELO)
# =========================
def empty_result():
    return {
        "urgencia": 0,
        "solicitud_economica": 0,
        "suplantacion": 0,
        "amenaza": 0,
        "manipulacion_emocional": 0,
        "chantaje_emocional": 0,
        "autoridad": 0,
        "culpa": 0,
        "aislamiento": 0,
        "falsa_emergencia": 0,
        "info_confidencial": 0
    }


# =========================
# MOTOR PRINCIPAL
# =========================
class SocialEngine:

    def __init__(self):
        print("⏳ [IA] Inicializando Motor 3: Ingeniería Social (mDeBERTa)...")

        try:
            self.model_name = MODEL_NAME

            self.clasificador = pipeline(
                task="zero-shot-classification",
                model=self.model_name
            )

            print("✅ [IA] Motor 3 cargado correctamente.")

        except Exception as e:
            print(f"❌ [SocialEngine] Error al cargar modelo: {str(e)}")
            self.clasificador = None

    # =========================
    # ANÁLISIS PRINCIPAL
    # =========================
    def analizar_texto(self, texto: str) -> dict:

        if not self.clasificador or not texto or not texto.strip():
            return empty_result()

        try:
            resultado = self.clasificador(
                sequences=texto,
                candidate_labels=SOCIAL_LABELS,
                multi_label=True
            )

            desglose = empty_result()

            for label, score in zip(resultado["labels"], resultado["scores"]):

                key = LABEL_MAPPING.get(label)

                if key:
                    desglose[key] = int(score * 100)

            return desglose

        except Exception as e:
            print(f"❌ [SocialEngine] Error en inferencia: {str(e)}")
            return empty_result()


# =========================
# INSTANCIA GLOBAL
# =========================
social_engine = SocialEngine()