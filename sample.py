from ailabs_asr.streaming import StreamingClient

def on_processing_sentence(message):
  print(f'hello: {message["asr_sentence"]}')

def on_final_sentence(message):
  print(f'world: {message["asr_sentence"]}')
  
asr_client = StreamingClient(
  config_path='api.yaml',
  key='key-applied-from-devconsole')
asr_client.start_streaming_wav(
  pipeline='asr-zh-tw-std',
  # verbose=True,
  file='your-voice-file.wav',
  on_processing_sentence=on_processing_sentence,
  on_final_sentence=on_final_sentence)