from time import sleep
from abc import ABC, abstractmethod
from typing import Dict


class Video:
    def __init__(self, _id: str) -> None:
        self._id = _id


class YoutubeDownloaderLib(ABC):
    @abstractmethod
    def download(self, id_: str) -> Video:
        pass


class YoutubeDownloaderService(YoutubeDownloaderLib):
    def download(self, id_: str) -> Video:
        print(f"Downloading {id_} started...")
        sleep(2)
        print(f"Downloading {id_} completed!")
        return Video(id_)


class YoutubeCacheProxy(YoutubeDownloaderLib):
    _cache: Dict[str, Video] = {}

    def __init__(self, service: YoutubeDownloaderLib) -> None:
        self._service = service

    def download(self, id_: str) -> Video:
        if id_ not in self._cache:
            self._cache[id_] = super().download(id_)
        else:
            print(f"Loading {id_} from cache!")
        return self._cache[id_]

    def reset(self):
        self._cache.clear()


class YoutubeDownloader:
    def __init__(self, lib: YoutubeDownloaderLib) -> None:
        self._lib = lib

    def download_video(self, id_: str):
        self._lib.download(id_)


if __name__ == "__main__":
    naive_downloader = YoutubeDownloader(YoutubeDownloaderService())
    naive_downloader.download_video("1")
    naive_downloader.download_video("2")
    naive_downloader.download_video("1")
    naive_downloader.download_video("2")

    smart_downloader = YoutubeDownloader(YoutubeCacheProxy(YoutubeDownloaderService()))
    smart_downloader.download_video("1")
    smart_downloader.download_video("2")
    smart_downloader.download_video("1")
    smart_downloader.download_video("2")
