import email
import boto3

PUBLISH_TOPIC_ARN = ""


def handler(event, context):
    print(f'Received event: {event}')

    message = email.message_from_string(event['message'])

    if message.is_multipart():
        for part in message.get_payload():
            if part.get_content_type() == 'text/calendar':
                calendar = part.get_payload()


def publish_calendar(calendar):
    sns = boto3.client('sns')
    response = sns.publish(TargetArn=PUBLISH_TOPIC_ARN,
                           Message=f'{"calendar":"{calendar}"}')
