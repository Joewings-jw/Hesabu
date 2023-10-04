import moviepy.editor as mpe

def convert_video_to_gif(video_file_path, output_file_path):
    videoClip = mpe.VideoFileClip(video_file_path)
    videoClip.write_gif(output_file_path)


if __name__ == '__main__':
    pass



