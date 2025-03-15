import cv2 as cv

# 불러오기
video_file = "rtsp://210.99.70.120:1935/live/cctv001.stream" # 천안시 교통정보 cctv (RTSP) // 0 = webcam
video = cv.VideoCapture(video_file)

# 불러오기 실패
assert video.isOpened(), 'Cannot read the given video, ' + video_file

# 변수 초기화
isRecord = False
out = None
filter_mode = None

# 재생 루프
while True:
    valid, img = video.read() # video의 한 frame (image)
    if not valid:
        break

    # 원본 복사
    filtered_img = img.copy()
    
    # Grayscale 효과
    if filter_mode == 103 or filter_mode == 71:  # g or G
        filtered_img = cv.cvtColor(filtered_img, cv.COLOR_BGR2GRAY)
    # 색 반전 효과
    elif filter_mode == 105 or filter_mode == 73:  # i or I
        filtered_img = 255 - filtered_img

    # 저장할 파일에 필터 효과 포함
    if isRecord and out is not None:
        if len(filtered_img.shape) == 2:  # Grayscale은 채널 2개
            filtered_img = cv.cvtColor(filtered_img, cv.COLOR_GRAY2BGR)
        out.write(filtered_img)

    # 녹화중 표시 + 저장된 파일에선 보이지 않음
    display_img = filtered_img.copy()
    if isRecord:
        cv.putText(display_img, "REC", (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # 필터 적용된 이미지 출력
    cv.imshow('ColorFilterRec', display_img)

    # 키 입력
    key = cv.waitKey(30) # 30 frame으로 통일

    # 종료
    if key == 27: # ESC
        break

    # 녹화 시작 및 중지(자동 저장)
    if key == 32: # SPACE
        if isRecord:
            isRecord = False
            out.release()
            out = None
        else:
            isRecord = True
            fourcc = cv.VideoWriter_fourcc(*'XVID')  # XVID 코덱
            out = cv.VideoWriter('recorded_video.avi', fourcc, 30, (img.shape[1], img.shape[0]))

    # g(G), i(I)로 mode on 이후 같은 키를 다시 눌러서 필터 효과 해제
    if key == 71 or key == 103:
        filter_mode = None if filter_mode == 103 else 103
    elif key == 73 or key == 105:
        filter_mode = None if filter_mode == 105 else 105

# 종료 시 리소스 해제
video.release()
if out is not None:
    out.release()
cv.destroyAllWindows()