#!/usr/bin/env python3
# coding:utf-8


# Import
import os  # pour naviguer
import mutagen  # pour longueur fichier son
from pydub import AudioSegment  # pour split fichier son
from mutagen.mp3 import MP3  # pour gérer le format MP3
from pathlib import Path

# Fonction split_audio


def split_audio_file(episode, duree_segment_ms, dossier_sons_bruts, dossier_sons_split):
    # Ouvrir fichier
    song = AudioSegment.from_mp3(dossier_sons_bruts / episode)

    # Connaitre durée fichier
    audio = MP3(dossier_sons_bruts / episode)
    audio_info = audio.info
    longeurEnMs = int(audio_info.length) * 1000

    # Boucle découpage
    episodeSansExt, _ = os.path.splitext(episode)
    n = 0
    i = 0

    while i < longeurEnMs:
        n += 1
        nom_fichier = episodeSansExt + f"Part{n}.mp3"
        segment = song[i : i + duree_segment_ms]

        segment.export(dossier_sons_split / nom_fichier, format="mp3")
        i += duree_segment_ms


if __name__ == "__main__":

    episode = "mr_x_1999_01_02.mp3"
    dossier_sons_bruts = Path("./Test/")
    dossier_sons_split = Path("./Test/Split")
    duree_segment_ms = 5000

    split_audio_file(episode, duree_segment_ms, dossier_sons_bruts, dossier_sons_split)

print("hello")
