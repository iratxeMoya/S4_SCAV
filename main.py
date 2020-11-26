import os
from menu import mainMenu, codecMenu, menuIPs

def streamingVideo(IP, port, videoFile):

    os.system('ffmpeg -re -i {} -vcodec copy -acodec copy -f mpegts "udp://{}:{}"'.format(videoFile, IP, port))

def changeCodec(codec, videoFile):

    if codec != 'libvpx':
        os.system("ffmpeg -i {} -c:v {} video_in_{}.mp4".format(videoFile, codec, codec))
    else:
        os.system("ffmpeg -i {} -c:v {} -c:a libvorbis video_in_{}.webm".format(videoFile, codec, codec))

def createMosaic(video1, video2, video3, video4):

    os.system('ffmpeg -i {} -i {} -i {} -i {} -filter_complex "nullsrc=size=640x480 [base]; [0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; [2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; [3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; [base][upperleft] overlay=shortest=1 [tmp1]; [tmp1][upperright] overlay=shortest=1:x=320 [tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" -c:v libx264 mosaicVideo.mp4'.format(video1, video2, video3, video4))

if __name__ == "__main__":

    menu = mainMenu()
    option = menu['Action menu']
    video = menu['video file']

    if option == "Change codec":

        codec = codecMenu()['Codec menu']

        if codec == 'VP8':
            changeCodec('libvpx', video)
        elif codec == 'VP9':
            changeCodec('libvpx-vp9', video)
        elif codec == 'H265':
            changeCodec('libx265', video)
        elif codec == 'AV1':
            changeCodec('libaom-av1', video)

    elif option == "Create mosaic":

        videos = video.split(" ")

        if len(videos) != 4:
            print("Please, introduce 4 videos")
        else:
            createMosaic(videos[0], videos[1], videos[2], videos[3])

    elif option == "Streaming":

        IPmenu = menuIPs()

        streamingVideo(IPmenu['IP'], IPmenu['port'], video)
