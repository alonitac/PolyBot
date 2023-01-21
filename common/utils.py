from yt_dlp import YoutubeDL


def search_download_youtube_video(video_name, download=True, num_results=1):
    """
    This function downloads the first num_results search results from Youtube
    :param video_name: string of the video name
    :param download: download video - True or False
    :param num_results: integer representing how many videos to download
    :return: list of paths to your downloaded video files
    """
    104857600
    """
    ydl_opts = {
        'max_filesize': 209715200
    }
    """
    with YoutubeDL() as ydl:
        """
        URL = ydl.extract_info(f"ytsearch{num_results}:{video_name}", download=False)['entries'][0]['webpage_url']
        return [ydl.prepare_filename(video) + "," + videos["webpage_url"] for video in videos]
        """
        try:

            print(f"Video Name to download {video_name}")
            videos = ydl.extract_info(f"ytsearch{num_results}:{video_name}", download=download)['entries']
            maxsize = 104857600
            vdict = {}
            i = 0
            print(f"Start download is {download}")
            for video in videos:

                isize = video['filesize_approx']
                print(f"Video = {video['title']} Size = {isize}")

                if download is False:
                    print(f"download is False")
                    if isize < maxsize:
                        title = ydl.prepare_filename(video)
                        vdict[title] = video['webpage_url']
                        i += 1
                        if i == 3:
                            break
                else:
                    print(f"download is True")
                    title = ydl.prepare_filename(video)
                    vdict[title] = video['webpage_url']
                    i += 1
                    if i == num_results:
                        break
        except Exception as e:
            print(f"error in search_download_youtube_video: {repr(e)}")

    return vdict
