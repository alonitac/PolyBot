from yt_dlp import YoutubeDL


def search_download_youtube_video(video_name, download=True, num_results=1):
    """
    This function downloads the first num_results search results from Youtube
    :param video_name: string of the video name
    :param download: download video - True or False
    :param num_results: integer representing how many videos to download
    :return: list of paths to your downloaded video files
    """
    ydl_opts = {
        'max_filesize': 104857600
    }
    with YoutubeDL(ydl_opts) as ydl:
        """
        URL = ydl.extract_info(f"ytsearch{num_results}:{video_name}", download=False)['entries'][0]['webpage_url']
        return [ydl.prepare_filename(video) + "," + videos["webpage_url"] for video in videos]
        """
        try:
            videos = ydl.extract_info(f"ytsearch{num_results}:{video_name}", download=download)['entries']
            vdict = {}
            for video in videos:

                title = ydl.prepare_filename(video)
                vdict[title] = video['webpage_url']

        except Exception as e:
            print(f"error in search_download_youtube_video: {repr(e)}")

    return vdict
