from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def extract_frames(input_file, start_time, end_time, output_folder, step=10):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with VideoFileClip(input_file) as video:
        video_segment = video.subclipped(start_time, end_time)

        total_frames = int(video_segment.fps * video_segment.duration)
        for i in range(0, total_frames, step):
            frame = video_segment.get_frame(i / video_segment.fps)

            frame_filename = os.path.join(output_folder, f"frame_{i // step:04d}.jpg")
            video_segment.save_frame(frame_filename, t=i / video_segment.fps)
            print(f"Кадр сохранен: {frame_filename}")

if __name__ == "__main__":
    input_file = input("Введите имя входного файла (с расширением): ")
    start_time = float(input("Введите время начала фрагмента (в секундах): "))
    end_time = float(input("Введите время окончания фрагмента (в секундах): "))
    output_folder = input("Введите путь для записи кадров: ")
    step = int(input("Введите шаг извлечения кадров (по умолчанию 10): ") or 10)

    extract_frames(input_file, start_time, end_time, output_folder, step)