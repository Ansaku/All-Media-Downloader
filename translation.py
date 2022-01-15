class Translation(object):
    START_TEXT = """Hai {},
Anda dapat mengunggah File|Video Ke Telegram dengan tautan langsung, Menggunakan bot ini!
Situs Dukungan <a href="https://ytdl-org.github.io/youtube-dl/supportedsites.html">HERE</a>
/help untuk lebih jelasnya!"""
    FORMAT_SELECTION = "Pilih format yang diinginkan: <a href='{}'>ukuran file mungkin perkiraan</a> \nJika Anda ingin mengatur thumbnail kustom, kirim foto sebelum atau dengan cepat setelah mengetuk salah satu tombol di bawah ini.\nKamu dapat memakai /deletethumbnail untuk menghapus thumbnail yang dibuat secara otomatis."
    SET_CUSTOM_USERNAME_PASSWORD = """Jika Anda ingin mengunduh video premium, berikan dalam format berikut:
URL | filename | username | password"""
    DOWNLOAD_START = "📥Mengunduh..."
    UPLOAD_START = "📤Mengunggah..."
    RCHD_TG_API_LIMIT = "Diunduh di {} detik.\nUkuran File Terdeteksi: {}\nMaaf. Tapi, saya tidak dapat mengunggah file yang lebih besar dari 2GB karena keterbatasan Telegram API."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Terima kasih telah menggunakan saya \n\n<b>Join @ansakubotchannel Untuk Bot Lebih Berguna Seperti Saya </b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Diunduh di {} detik.\nDiunggah di {} detik.\n\n@ansakubotchannel"
    SAVED_CUSTOM_THUMB_NAIL = "Kustom video / file thumbnail disimpan. Gambar ini akan digunakan dalam video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Thumbnail khusus berhasil dihapus."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    ABOUT_MSG = """ Something About Me :
    
   ☞My Name  : All Media Downloader

   ☞Updates  : @ansakubotchannel    

   ☞Language : Python3

   ☞Library  : <a href="https://docs.pyrogram.org/">Pyrogram 1.0.7</a>"""
    HELP_USER = """Silakan Ikuti langkah-langkah ini!
    
1. Kirim url (contoh.domain/File.mp4 | Nama File Baru.mp4).
2. Kirim Gambar Sebagai Gambar Kecil Khusus (Opsional).
3. Pilih tombol.
   SVideo - Berikan File sebagai video dengan Tangkapan Layar
   DFile  - Berikan File (video) sebagai file dengan Tangkapan Layar
   Video  - Berikan File sebagai video tanpa Tangkapan Layar
   File   - Berikan File tanpa Tangkapan Layar

Jika bot tidak merespon, Tanya Di Sini @AnkiSatya"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Membalas /generatecustomthumbnail ke album media, untuk menghasilkan gambar kecil khusus"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Album Media hanya boleh berisi dua foto. Silakan kirim ulang album media, lalu coba lagi, atau kirim hanya dua foto dalam satu album."
Kamu dapat memakai /rename perintah setelah menerima file untuk mengganti namanya dengan dukungan thumbnail khusus.
"""
    CANCEL_STR = "Proses Dibatalkan"
    ZIP_UPLOADED_STR = "Diunggah {} file di {} detik"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
