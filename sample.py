from distutils.command.config import config
from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
# be aware of the path may be different from our developers and it could cause some error
sys.path.append(str(path_root))

from ailabs_asr.streaming import stream_file

stream_file(
  key='your-key-from-devconsole',
  pipeline='asr-zh-tw-std', # asr-zh-en-std, asr-zh-tw-std, asr-en-std or asr-jp-std
  input_wav='your-voice-file.wav',
  config_path='api.yaml',
  verbose=False
)