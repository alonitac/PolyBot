# MyPlaylist PolyBot

**Telegram bot which will search YouTube content and manage playlist.**

This repo includes two microservicese, the Bot and the Worker services,
the Bot will search the content in YouTube according to the text that was typed and sends the content you choose to SQS,
the Worker will get the name of the file from the SQS and download it from YouTube and then store it in S3 bucket.
the S3 bucket will serve as a playlist.

The Bot manage the playlist according to the following commands:

    @list - list all files in Playlist and their size (S3 bucket).
    @playlist - list all files in Playlist and their URLs (S3 bucket).
    @addfile(x) - add the file you want to upload (run after the search).
    @addall - upload all files (run after the search).
    @delfile(x) - delete the chosen file (run after @list command).
    @delall - delete all files (run after @list command).

Regular text without the @ sign will be searched in YouTube. 