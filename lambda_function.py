import boto3

def get_slot_value(event, slot_name):
    slots = event.get('sessionState', {}).get('intent', {}).get('slots', {})
    slot = slots.get(slot_name)
    if slot and slot.get('value') and slot['value'].get('interpretedValue'):
        return slot['value']['interpretedValue'].strip()
    return None

def lambda_handler(event, context):
    try:
        input_text = get_slot_value(event, 'text')
        language_slot = get_slot_value(event, 'language')

        if not input_text:
            # Ask Lex to elicit the 'text' slot
            return {
                "sessionState": {
                    "dialogAction": {
                        "type": "ElicitSlot",
                        "slotToElicit": "text"
                    },
                    "intent": {
                        "name": "TranslationIntent",
                        "state": "InProgress",
                        "slots": event['sessionState']['intent']['slots']
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": "What text would you like me to translate?"
                    }
                ]
            }

        if not language_slot:
            # Ask Lex to elicit the 'language' slot
            return {
                "sessionState": {
                    "dialogAction": {
                        "type": "ElicitSlot",
                        "slotToElicit": "language"
                    },
                    "intent": {
                        "name": "TranslationIntent",
                        "state": "InProgress",
                        "slots": event['sessionState']['intent']['slots']
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": "Which language should I translate to?"
                    }
                ]
            }

        # Language mapping
        language_codes = {
            'French': 'fr',
            'Japanese': 'ja',
            'Chinese': 'zh',
            'Spanish': 'es',
            'German': 'de'
        }

        if language_slot not in language_codes:
            raise ValueError(f"Unsupported language: {language_slot}")

        target_language_code = language_codes[language_slot]

        # Translate
        translate_client = boto3.client('translate')
        response = translate_client.translate_text(
            Text=input_text,
            SourceLanguageCode='auto',
            TargetLanguageCode=target_language_code
        )

        translated_text = response['TranslatedText']

        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": "TranslationIntent",
                    "state": "Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": translated_text
                }
            ]
        }

    except Exception as error:
        error_message = f"Lambda execution error: {str(error)}"
        print(error_message)
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": "TranslationIntent",
                    "state": "Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": error_message
                }
            ]
        }
