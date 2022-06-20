from youtube_dl import YoutubeDL


def search_download_youtube_video(video_name, num_results=1, cached_dict={}):
    """
    This function downloads the first num_results search results from YouTube
    :param video_name: string of the video name
    :param num_results: integer representing how many videos to download
    :param cached_dict: dict representing cached video files eg'{video id:telegram file id} that was downloaded before
    :return: tuple (str: paths to your downloaded video files, str: YouTube video id )
    """

    with YoutubeDL() as ydl:
        videos = ydl.extract_info(f"ytsearch{num_results}:{video_name}", download=False)['entries']
        # Download file only if YouTube video id doesn't exist in given dict
        if videos[0]["id"] not in cached_dict:
            videos = ydl.extract_info(f"ytsearch{num_results}:{video_name}", download=True)['entries']
        return ydl.prepare_filename(videos[0]), videos[0]["id"]
