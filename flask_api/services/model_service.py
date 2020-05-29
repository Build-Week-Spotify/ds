from flask_api.services.spotify_service import spotify_api
from joblib import load
import pandas as pd

def model(artist_name, track_name, pg_curs):
    sp = spotify_api()

    result = sp.search(
        q=f'artist: {artist_name} track: {track_name}')  # send request to spotify api searching for artist name and track posted to the route.
    result = result['tracks']['items']

    track_id = result[0]['id']
    track_name = result[0]['name']
    artist_name = result[0]['artists'][0]['name']

    features = sp.audio_features(track_id)
    features = features[0]

    ##reorder the features to match expected input for the model
    features = {'acousticness': features["acousticness"], 'danceability': features["danceability"],
                'energy': features['energy'], 'instrumentalness': features['instrumentalness'], 'key': features['key'],
                'liveness': features['liveness'], 'loudness': features['loudness'],
                'speechiness': features['speechiness'],
                'tempo': features['tempo'], 'valence': features['valence']}

    features_df = pd.DataFrame(features, index=[0])

    scaler = load('scaler.joblib')  # load pickled scaler
    audio_feats_scaled = scaler.transform(features_df)

    model = load('test_model.joblib')  # load pickled nearest neighbors
    prediction = model.kneighbors(audio_feats_scaled)

    similar_songs_index = prediction[1][0][:].tolist()

    recommendations_list = []
    artist_list = []
    title_list = []
    similar_song_ids = []
    similar_songs_features = []

    for i, value in enumerate(similar_songs_index):
        query = f'''SELECT * FROM tracks WHERE index={value}'''
        pg_curs.execute(query)
        result = pg_curs.fetchall()

        song_id = result[0][7]

        artist = result[0][2]
        title = result[0][13]

        if i != 0:  # don't run on first iteration
            if title in title_list:
                if artist in artist_list:  # if both title and artist already exist as a prediction, this is a duplicate, lets skip it.
                    continue
        if artist == f"['{artist_name}']" and title == track_name:
            continue

        list_of_feats = [result[0][1], result[0][3], result[0][5], result[0][8], result[0][9], result[0][10],
                         # retrieve audio features from the fetched query
                         result[0][11], result[0][16], result[0][17], result[0][18]]
        similar_songs_features.append(list_of_feats)

        artist_list.append(artist)
        title_list.append(title)

        # For Kyle's chart function.
        similar_song_ids.append(song_id)
        similar_song_ids.append(title)
        similar_song_ids.append(artist)

        spotify_result = sp.search(q=f'artist: {artist} track: {title}')

        album_name = spotify_result['tracks']['items'][0]['album']['name']
        album_result = spotify_result['tracks']['items'][0]['album']['images'][0]['url']

        recommendations_list.append({"title": title, "album_name": album_name, "artist": artist,
                                     "album_art": album_result, "song_id": song_id})

        if len(recommendations_list) > 4:
            break

    column_names = features_df.columns.tolist()  # retrieve column names and ordering from manually defined near the start of the route

    audio_feats_scaled_df = pd.DataFrame(audio_feats_scaled, columns=column_names)
    audio_feats_df = pd.DataFrame(features_df, columns=column_names)

    similar_feats_scaled = scaler.transform(similar_songs_features)
    similar_feats_scaled_df = pd.DataFrame(similar_feats_scaled, columns=column_names)
    similar_song_features_unscaled = pd.DataFrame(similar_songs_features, columns=column_names)

    similar_feats_averaged = []

    for col in column_names:
        avg = similar_feats_scaled_df[col].mean()
        similar_feats_averaged.append(avg)

    similar_feats_averaged_df = pd.DataFrame([similar_feats_averaged], columns=column_names)

    visual_df = pd.concat(
        [audio_feats_scaled_df, similar_feats_averaged_df, similar_feats_scaled_df, similar_song_features_unscaled,
         audio_feats_df], ignore_index=True)

    return visual_df, similar_song_ids, recommendations_list