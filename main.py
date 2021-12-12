from pytube import YouTube
import os


def main():
    while True:
        try:
            video = YouTube(input("URL:"))
            audio = video.streams.get_audio_only()
            print(audio)
            audio.download()

            break
        except:
            print("Hubo un error con tu URL, intentalo de nuevo.")


if __name__ == '__main__':
    main()
