import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'chat', self.channel_name
        )
        self.accept()

        self.send(text_data=json.dumps({
            'user': self.scope['user'].email,
            'message': 'I joined this channel'
        }))

    def disconnect(self, close_code: int):
        async_to_sync(self.channel_layer.group_discard)(
            'chat', self.channel_name
        )

    def receive(self, text_data: dict):
        text_data_json = json.loads(text_data)

        async_to_sync(self.channel_layer.group_send)(
            'chat', {
                'type': 'chat.message',
                'message': text_data_json['message']
            }
        )

    def chat_message(self, event: dict):
        message = event['message']

        self.send(text_data=json.dumps({
            'user': self.scope['user'].email,
            'message': message
        }))
