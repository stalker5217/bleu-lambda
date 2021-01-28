import json
import nltk.translate.bleu_score as bleu

def lambda_handler(event, context):
    candidate = event['queryStringParameters']['candidate']
    references = event['multiValueQueryStringParameters']['references']

    print(candidate)
    print(references)

    # NLTK 패키지 구현되어져 있는 코드로 계산한 BLEU 점수
    score = bleu.sentence_bleu(list(map(lambda ref: ref.split(), references)), candidate.split())

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": score,
        }),
    }