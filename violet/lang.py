"""Language detection module. Currently not used, as langdetect is too inaccurate!"""

import langdetect

LANGS = {
    'en': 'en-US',
    'de': 'de-DE',
    'fr': 'fr-FR',
    'es': 'es-ES'
}

def detect(text: str):
    # detected = langdetect.detect(text)
    
    # for lang in LANGS:
    #     if lang == detected:
    #         return [lang, LANGS[lang]]

    return 'en-US'
