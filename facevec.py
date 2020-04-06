import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./data/shape_predictor_68_face_landmarks.dat')
face_model = dlib.face_recognition_model_v1('./data/dlib_face_recognition_resnet_model_v1.dat')