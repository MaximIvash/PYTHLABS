import cv2

def play_video_with_info(video_file):
    cap = cv2.VideoCapture(video_file)

    if not cap.isOpened():
        print("Ошибка: Не удается открыть видеофайл.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    video_name = video_file.split('/')[-1]

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.putText(frame, f'Имя файла: {video_name}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, f'FPS: {fps:.2f}', (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Video Player', frame)

        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_file = input("Введите путь к видеофайлу: ")
    play_video_with_info(video_file)