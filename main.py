from pytube import YouTube
from pathlib import Path


def main():
    while True:
        try:
            video = YouTube(input("URL: "))
            downloads_path = str(Path.home() / "Downloads")
            audio = video.streams.get_audio_only()
            audio.download(output_path=downloads_path)

            break
        except:
            print("Hubo un error con tu URL, intentalo de nuevo.")


if __name__ == '__main__':
    main()
