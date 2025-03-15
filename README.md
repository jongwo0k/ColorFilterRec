# ColorFilterRec
Real-time video recorder with color filtering (Grayscale &amp; RGB Inversion) using OpenCV

OpenCV를 사용한 실시간 영상 필터 및 녹화 프로그램

# 주요 기능
video_file 변수에 스트리밍 프로토콜 주소를 입력해 실시간 스트리밍 (0 입력 시 webcam 재생 , fps : 30)

SPACE로 영상 녹화 및 저장
- XVID 코덱으로 저장 위치에 recorded_video.avi 저장 (덮어쓰기를 원하지 않을 시 out = cv.VideoWriter()에 저장할 파일 이름 수정)
- 녹화중 좌측 상단 REC 표시 (저장된 영상엔 표시되지 않음)

g(G)로 grayscale 필터 효과 적용
- 대문자, 소문자 모두 가능
- 다시 누르면 필터 효과 해제

i(I)로 색 반전 필터 효과 적용
- 대문자, 소문자 모두 가능
- 다시 누르면 필터 효과 해제

Grayscale 필터와 Inversion 필터 상태에서 상호 전환 가능

필터를 켠 상태로 녹화 또는 녹화 중 필터 효과 적용 및 해제 가능

ESC로 프로그램 종료

# example video 출처
https://www.data.go.kr/data/15063717/fileData.do 천안시_교통정보 CCTV
