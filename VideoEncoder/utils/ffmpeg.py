import asyncio
import os
import subprocess
import time
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import ffmpeg
from .. import audio, encode_dir
from .. import preset as p
from .. import tune as t


def get_codec(filepath, channel='v:0'):
    output = subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', channel,
                                      '-show_entries', 'stream=codec_name,codec_tag_string', '-of',
                                      'default=nokey=1:noprint_wrappers=1', filepath])
    return output.decode('utf-8').split()

async def encode(filepath):
    path, extension = os.path.splitext(filepath)
    name = path.split('/')
    output_filepath = encode_dir + name[len(name)-1] + '.mkv'
    assert(output_filepath != filepath)
    if os.path.isfile(output_filepath):
        print(f'Warning! "{output_filepath}": file already exists')
    print(filepath)
    codec = '-c:v libx264 -pix_fmt yuv420p10le -x265-params profile=main10'
    crf = '-crf 23'
    preset = '-preset medium'
    video_opts = f'-tune {t} -map 0:v? -map_chapters 0 -map_metadata 0 -tag:v hvc1'
    subs_i = get_codec(filepath, channel='s:0')
    if subs_i == []:
        subtitles = ''
    else:
        subtitles = '-c:s copy -map 0:s'
    a_i = get_codec(filepath, channel='a:0')
    a = audio
    if a_i == []:
        audio_opts = ''
    else:
        audio_opts = '-map 0:a?'
        if a == 'aac':
            audio_opts += ' -c:a aac -b:a 128k'

    finish = '-threads 8'
    # Finally
    command = ['ffmpeg', '-y', '-i', filepath]
    command.extend((codec.split() + preset.split() + video_opts.split() +
                   crf.split() + subtitles.split() + audio_opts.split() + finish.split()))
    proc = await asyncio.create_subprocess_exec(*command, output_filepath, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    await proc.communicate()
    return output_filepath

def get_thumbnail(in_filename, path, ttl):
    out_filename = os.path.join(path, str(time.time()) + ".jpg")
    open(out_filename, 'a').close()
    try:
        (
            ffmpeg
            .input(in_filename, ss=ttl)
            .output(out_filename, vframes=1)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        return out_filename
    except ffmpeg.Error as e:
        return None

def get_duration(filepath):
    metadata = extractMetadata(createParser(filepath))
    if metadata.has("duration"):
        return metadata.get('duration').seconds
    else:
        return 0
