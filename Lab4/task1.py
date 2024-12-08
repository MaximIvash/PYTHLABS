from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_video_segment(input_file, start_time, end_time, output_file):
    with VideoFileClip(input_file) as video:
        video_segment = video.subclipped(start_time, end_time)
        video_segment.write_videofile(output_file, codec='libx264')

if __name__ == "__main__":
    input_file = input("Введите имя входного файла (с расширением): ")
    start_time = float(input("Введите время начала фрагмента (в секундах): "))
    end_time = float(input("Введите время окончания фрагмента (в секундах): "))
    output_file = input("Введите имя выходного файла (с расширением): ")

    extract_video_segment(input_file, start_time, end_time, output_file)