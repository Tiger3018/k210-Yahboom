# See <https://wiki.sipeed.com/soft/maixpy/zh/api_reference/media/audio.html>
from fpioa_manager import fm
from maix import I2S, GPIO
import audio

# register i2s(i2s0) pin
fm.register(31,fm.fpioa.I2S0_OUT_D1)
fm.register(32,fm.fpioa.I2S0_SCLK)
fm.register(30,fm.fpioa.I2S0_WS)
# register i2s micro pin
fm.register(34,fm.fpioa.I2S1_OUT_D1)
fm.register(35,fm.fpioa.I2S1_SCLK)
fm.register(33,fm.fpioa.I2S1_WS)


# init i2s(i2s0)
wav_dev = I2S(I2S.DEVICE_0)
microphone_dev = I2S(I2S.DEVICE_1)

# init audio
player = audio.Audio(path="audio/car.wav")
player.volume(80)

# read audio info
wav_info = player.play_process(wav_dev)
print("wav file head information: ", wav_info)
wav_dev.set_sample_rate(wav_info)
if not wav_info:
    raise Exception("==failed to decode wav file==")

# config i2s according to audio info
wav_dev.channel_config(wav_dev.CHANNEL_1, I2S.TRANSMITTER,resolution = I2S.RESOLUTION_16_BIT ,cycles = I2S.SCLK_CYCLES_32, align_mode = I2S.RIGHT_JUSTIFYING_MODE)


# loop to play audio
while True:
    ret = player.play()
    if ret == None:
        print("format error")
        break
    elif ret==0:
        print("end")
        break
player.finish()
