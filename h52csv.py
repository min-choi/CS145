
# Import necessary libraries
import h5py
import numpy as np
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from hdf5_getters import *
from filepath_getters import *

# h5 = open_h5_file_read('TRBDYYN128F92F383F.h5')
# duration = get_num_songs(h5)
# print(duration)
# h5.close()

h5 = get_file_paths()

import csv

def get_song_data(h5filename):
    # Open the HDF5 file in read mode
    h5 = open_h5_file_read(h5filename)

    # Get the number of songs in the file
    num_songs = get_num_songs(h5)

    # Create a list to store the song data
    song_data = []

    # Iterate over each song in the file
    for songidx in range(num_songs):
        # Get the required fields for each song
        artist_familiarity = get_artist_familiarity(h5, songidx)
        artist_hotttnesss = get_artist_hotttnesss(h5, songidx)
        artist_id = get_artist_id(h5, songidx)
        artist_mbid = get_artist_mbid(h5, songidx)
        artist_playmeid = get_artist_playmeid(h5, songidx)
        artist_7digitalid = get_artist_7digitalid(h5, songidx)
        artist_latitude = get_artist_latitude(h5, songidx)
        artist_longitude = get_artist_longitude(h5, songidx)
        artist_location = get_artist_location(h5, songidx)
        artist_name = get_artist_name(h5, songidx)
        release = get_release(h5, songidx)
        release_7digitalid = get_release_7digitalid(h5, songidx)
        song_id = get_song_id(h5, songidx)
        song_hotttnesss = get_song_hotttnesss(h5, songidx)
        title = get_title(h5, songidx)
        track_7digitalid = get_track_7digitalid(h5, songidx)

        #more added like danceability etc.
        sample_rate = get_analysis_sample_rate(h5, songidx)
        danceability = get_danceability(h5, songidx)
        duration = get_duration(h5, songidx)
        end_of_fade_in = get_end_of_fade_in(h5, songidx),
        start_of_fade_in = get_start_of_fade_out(h5, songidx),
        energy = get_energy(h5, songidx),
        song_key = get_key(h5, songidx),
        key_confidence = get_key_confidence(h5, songidx),
        loudness = get_loudness(h5, songidx),
        mode = get_mode(h5, songidx),
        mode_confidence = get_mode_confidence(h5, songidx),
        tempo = get_tempo(h5, songidx),
        time_signature = get_time_signature(h5, songidx),
        time_sig_confidence = get_time_signature_confidence(h5, songidx)

        # Append the song data to the list
        song_data.append([artist_familiarity, artist_hotttnesss, artist_id, artist_mbid, artist_playmeid,
                          artist_7digitalid, artist_latitude, artist_longitude, artist_location, artist_name,
                          release, release_7digitalid, song_id, song_hotttnesss, title, track_7digitalid,
                          sample_rate, danceability, duration, end_of_fade_in, start_of_fade_in, 
                          energy, song_key, key_confidence, loudness, mode, mode_confidence, tempo, 
                          time_signature, time_sig_confidence
                          ])

    # Close the HDF5 file
    h5.close()

    return song_data

def convert_h5_to_csv(h5files, csvfilename):
    # Get the song data from the HDF5 file

    # Write the song data to a CSV file
    with open(csvfilename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['artist_familiarity', 'artist_hotttnesss', 'artist_id', 'artist_mbid', 'artist_playmeid',
                         'artist_7digitalid', 'artist_latitude', 'artist_longitude', 'artist_location', 'artist_name',
                         'release', 'release_7digitalid', 'song_id', 'song_hotttnesss', 'title', 'track_7digitalid',
                         'sample_rate', 'danceability', 'duration', 'end_of_fade_in', 'start_of_fade_in', 
                         'energy', 'song_key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 
                         'time_signature', 'time_sig_confidence'
                         ])
        for h5 in h5files:
            song_data = get_song_data(h5)
            writer.writerows(song_data)

# Example usage
convert_h5_to_csv(h5, 'output_new.csv')
