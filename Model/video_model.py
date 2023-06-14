from imports import *

IMAGE_HEIGHT , IMAGE_WIDTH = 64, 64
SEQUENCE_LENGTH = 20
CLASSES_LIST = ['Real', 'Fake']

def predict_on_video(video_file_path, output_file_path, SEQUENCE_LENGTH):
    video_reader = cv2.VideoCapture(video_file_path)
    original_video_width = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_video_height = int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))

    video_writer = cv2.VideoWriter(output_file_path, cv2.VideoWriter_fourcc('M', 'P', '4', 'V'),
                                   video_reader.get(cv2.CAP_PROP_FPS), (original_video_width, original_video_height))

    frames_queue = deque(maxlen=SEQUENCE_LENGTH)
    predicted_class_name = ''

    json_file = open('Model/video_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    LRCN_model = model_from_json(loaded_model_json)
    LRCN_model.load_weights('Model/video_model.h5')
    LRCN_model.compile(loss = 'categorical_crossentropy', optimizer = 'Adam', metrics = ["accuracy"])

    while video_reader.isOpened():
        ok, frame = video_reader.read()
        if not ok:
            break

        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
        normalized_frame = resized_frame / 255

        frames_queue.append(normalized_frame)

        if len(frames_queue) == SEQUENCE_LENGTH:
            predicted_labels_probabilities = LRCN_model.predict(np.expand_dims(frames_queue, axis=0))[0]

            predicted_label = np.argmax(predicted_labels_probabilities)
            predicted_class_name = CLASSES_LIST[predicted_label]

        cv2.putText(frame, predicted_class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        video_writer.write(frame)
    video_reader.release()
    video_writer.release()


def check_video():
    if os.path.exists('Model/video_model.h5') == False:
        url = 'https://drive.google.com/u/5/uc?id=1-07abNo6h7hN-o73elJ6VHmXO1LTlUuc&export=download'
        filename = 'Model/video_model.h5'
        urlretrieve(url, filename)
    if os.path.exists('Model/video_model.json') == False:
        url = 'https://drive.google.com/u/5/uc?id=1-1VpLV5VESh09Kr9tmnNzetJ4sDVC9bG&export=download'
        filename = 'Model/video_model.json'
        urlretrieve(url, filename)
    predict_on_video('../CheckVideo.mp4', '../Result.mp4', SEQUENCE_LENGTH)