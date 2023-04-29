import subprocess
import sys

subprocess.check_call(["pip", "install", "yt_dlp"])
subprocess.check_call(["pip", "install", "validators"])

import validators

print("""



















""")



if "-help" in sys.argv or "--help" in sys.argv:
    print("=================================")
    print("▐     List argument suporter    ▐")
    print("=================================")
    print("▐      Liste des argument 'Format")
    print("▐ -help        Affiche cette page")
    print("▐ -avi         télécharge en Format vidéo")
    print("▐ -mp4         télécharge en Format vidéo")
    print("▐ -mov         télécharge en Format vidéo")
    print("▐ -wmv         télécharge en Format vidéo")
    print("▐ -flv         télécharge en Format vidéo")
    print("▐ -mkv         télécharge en Format vidéo")
    print("▐ -webm         télécharge en Format vidéo")
    print("▐ -mpeg         télécharge en Format vidéo")
    print("▐ -vob         télécharge en Format vidéo")
    print("▐ -3gp         télécharge en Format vidéo")
    print("▐ -mp3         télécharge en Format audio")
    print("▐ -wav         télécharge en Format audio")
    print("▐ -flac         télécharge en Format audio")
    print("▐ -aac         télécharge en Format audio")
    print("▐ -ogg         télécharge en Format audio")
    print("▐ -wma         télécharge en Format audio")
    print("===========================================")
    print(' [DYTBC.exe] [Format] ["URL"] ["URL"]')
    exit("  Il est possible d'ajouter plusieur URL a la suite")

# Recuperation du nombre de URL en retirent 1 qui représente le Format
NB_url = len(sys.argv) - 1

# Vérifier si des arguments ont été passés
if NB_url == 0:
    print("Aucune URL n'a été spécifiée.")
    sys.exit()

# Si des arguments ont été passés, les ajouter à la liste urls
url = []
for i in range(2, NB_url+1):
    if validators.url(sys.argv[i]):
        url.append(sys.argv[i])
        print(f"URL Valide : [ {sys.argv[i]} ]")
    else:
        print("Les URLs ne sont pas corecte !")
        exit()



import yt_dlp


# URL de la vidéo à télécharger
# url = 'https://youtu.be/jA33bI-KkwE'

# Options de téléchargement
#options = {
#    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
#    'outtmpl': '%(title)s.',
#    'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe'
#}

if "-avi" in sys.argv[1]:
    options_avi = {
        'format': 'best[ext=avi]',
        'outtmpl': '%(title)s.avi',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe'
    }
    options = options_avi

elif "-mp4" in sys.argv[1]:
    options_mp4 = {
        'format': 'best[ext=mp4]',
        'outtmpl': '%(title)s.mp4',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe'
    }
    options = options_mp4

elif "-mov" in sys.argv[1]:
    options_mov = {
        'format': 'best[ext=mov]',
        'outtmpl': '%(title)s.mov',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe'
    }
    options = options_mov

elif "-wmv" in sys.argv[1]:
    options_wmv = {
        'format': 'best[ext=wmv]',
        'outtmpl': '%(title)s.wmv',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe'
    }
    options = options_wmv

elif "-flv" in sys.argv[1]:
    options_flv = {
        'format': 'best[ext=flv]',
        'outtmpl': '%(title)s.flv',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe'
    }
    options = options_flv

elif "-mkv" in sys.argv[1]:
    options_mkv = {
        'format': 'best[ext=mkv]',
        'outtmpl': '%(title)s.mkv',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe'
    }
    options = options_mkv

elif "-webm" in sys.argv[1]:
    options_webm = {
        'format': 'best[ext=webm]',
        'outtmpl': '%(title)s.webm',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe'
    }
    options = options_webm

elif "-mpeg" in sys.argv[1]:
    options_mpeg = {
        'format': 'best[ext=mpeg]',
        'outtmpl': '%(title)s.mpeg',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe'
    }
    options = options_mpeg

elif "-vob" in sys.argv[1]:
    options_vob = {
        'format': 'best[ext=vob]',
        'outtmpl': '%(title)s.vob',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe'
    }
    options = options_vob

elif "-3gp" in sys.argv[1]:
    options_3gp = {
        'format': 'best[ext=3gp]',
        'outtmpl': '%(title)s.3gp',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe'
    }
    options = options_3gp

elif "-mp3" in sys.argv[1]:
    options_mp3 = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.mp3',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    options = options_mp3

elif "-wav" in sys.argv[1]:
    options_wav = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.wav',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '320',
        }],
    }
    options = options_wav

elif "-flac" in sys.argv[1]:
    options_flac = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.flac',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '320',
        }],
    }
    options = options_flac

elif "-aac" in sys.argv[1]:
    options_aac = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.aac',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'aac',
            'preferredquality': '320',
        }],
    }
    options = options_aac

elif "-ogg" in sys.argv[1]:
    options_ogg = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.ogg',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'ogg',
            'preferredquality': '320',
        }],
    }
    options = options_ogg

elif "-wma" in sys.argv[1]:
    options_wma = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.wma',
        'ffmpeg_location': r'C:\Users\Last-Help\Desktop\Donlowd_YTB_content\ffmpeg-6.0-full_build\bin\ffmpeg.exe',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wma',
            'preferredquality': '192',
        }]
    }
    options = options_wma

else:
    print("Erreur Format inconnu !")
    exit()

#############################################

playlist_url = sys.argv[2]

# Création de l'objet yt_dlp pour gérer le téléchargement
ydl = yt_dlp.YoutubeDL(options)

# Vérification si l'URL donnée est une playlist
try:
    playlist_dict = ydl.extract_info(playlist_url, download=False, process=False)
    if 'entries' in playlist_dict:
        # URL est une playlist
        playlist_title = playlist_dict['title']
        url = [entry['webpage_url'] for entry in playlist_dict['entries']]
        # Créer une instance de l'objet Yt_dlp
        ydl = yt_dlp.YoutubeDL(options)
        # Téléchargement
        ydl.download(url)
        exit()
    else:
        # URL n'est pas une playlist
        print("L'URL donnée n'est pas une playlist.")
        # Créer une instance de l'objet Yt_dlp
        ydl = yt_dlp.YoutubeDL(options)
        # Téléchargement
        ydl.download(url)
        exit()

except Exception as e:
    print(f'Une erreur s\'est produite : {e}')

exit()

######################################
# Créer une instance de l'objet Yt_dlp
#ydl = yt_dlp.YoutubeDL(options)

# Lancer le téléchargement
#ydl.download(url)




