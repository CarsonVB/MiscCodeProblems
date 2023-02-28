from PIL import Image, ImageDraw, ImageFont, GifImagePlugin, ImageSequence
GifImagePlugin.LOADING_STRATEGY = GifImagePlugin.LoadingStrategy.RGB_ALWAYS

im = Image.open('input.gif')
print(im.format, im.size, im.mode)

frames = []
capt_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. supercalifragilisticexpialidocious Vestibulum cursus metus sem, quis aliquam elit blandit quis.'
capt_text = capt_text.split()
print(capt_text)

frames_it = ImageSequence.Iterator(im)
img_width, img_height = frames_it[0].size
dynamic_size = False
for frame in frames_it:
    w, h = frame.size
    if img_width < w:
        dynamic_size = True
        break
    elif img_height < h:
        dynamic_size = True
        break


def captionify(font, frame_width, capt_text):
    ext = Image.new('RGBA', (0, 0), 'white')
    draw = ImageDraw.Draw(ext)
    caption = ''
    lines = []
    for word in capt_text:
        bbox = draw.multiline_textbbox((0, 0), text=word, font=font)
        w = bbox[2] - bbox[0]
        if w > frame_width:
            temp_word = caption
            for i in range(len(word)):
                temp_word += word[i]
                bbox = draw.multiline_textbbox((0, 0), text=temp_word, font=font)
                w = bbox[2] - bbox[0]
                if w > frame_width:
                    caption = temp_word[:-1]
                    temp_word = word[i]
                    lines.append(caption)
                    caption = ''
            caption = temp_word
            continue
        caption += word + ' '
        bbox = draw.multiline_textbbox((0, 0), text=caption, font=font)
        w = bbox[2] - bbox[0]
        if w > frame_width:
            caption = caption[0:(len(caption) - len(word) - 2)]
            lines.append(caption)
            caption = word + ' '
    lines.append(caption)
    caption = '\n'.join(lines)
    return caption


if not dynamic_size:
    font = ImageFont.truetype('futuraEB.ttf', size=int(img_height / 9))
    caption = captionify(font, img_width, capt_text)
    ext = Image.new('RGBA', (0, 0), 'white')
    draw = ImageDraw.Draw(ext)
    bbox = draw.multiline_textbbox((0, 0), text=caption, font=font)
    h = bbox[3] - bbox[1]
    w = bbox[2] - bbox[0]
    padding = h + int(img_height * 0.05)
    for frame in ImageSequence.Iterator(im):
        print(frame.info['duration'])
        ext = Image.new('RGBA', (img_width, int(img_height) + padding), 'white')
        draw = ImageDraw.Draw(ext)
        draw.text(((img_width - w) / 2, 0), caption, font=font, fill='black', align='center')
        ext.paste(frame, (0, img_height + padding - img_height, img_width, img_height + padding))
        frames.append(ext)
else:
    for frame in ImageSequence.Iterator(im):
        frame_width, frame_height = frame.size
        font = ImageFont.truetype('futuraEB.ttf', size=int(frame_height / 9))
        caption = captionify(font, frame_width, capt_text)
        bbox = draw.multiline_textbbox((0, 0), text=caption, font=font)
        h = bbox[3] - bbox[1]
        w = bbox[2] - bbox[0]
        padding = h + int(frame_height * 0.05)
        ext = Image.new('RGBA', (frame_width, int(frame_height) + padding), 'white')
        ext.paste(frame, (0, int(frame_height) + padding - frame_height, frame_width, int(frame_height) + padding))
        draw = ImageDraw.Draw(ext)
        draw.text(((frame_width - w) / 2, 0), caption, font=font, fill='black', align='center')

        frames.append(ext)


frames[0].save('output.gif', save_all=True, append_images=frames[1:], duration=10, loop=0)
