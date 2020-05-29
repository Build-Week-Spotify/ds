import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objects as go

def visualize_audio_similarities(df, cs_username, cs_api_key, similar_song_ids):
    songs = []
    artists = []

    for i in similar_song_ids[::-3]:
        artists.append(i)

    artist_cleaned = []

    for i in artists:
        res = str(i)[1:-1]
        artist_cleaned.append(res)

    for i in similar_song_ids[1::3]:
        songs.append(i)

    """
    """
    vals = [36, 72, 108, 144, 180, 216, 252, 288, 324, 360]
    theta = [23, 59, 95, 131, 167, 203, 239, 275, 311, 347]
    k = 4
    k2 = 8
    k3 = 12
    k4 = 16
    k5 = 20
    k6 = 24
    theta2 = [x + k for x in theta]
    theta3 = [x + k2 for x in theta]
    theta4 = [x + k3 for x in theta]
    theta5 = [x + k4 for x in theta]
    theta6 = [x + k5 for x in theta]
    theta7 = [x + k6 for x in theta]
    width = 7
    fig = go.Figure()
    fig.add_trace(go.Barpolar(
        r=df.iloc[0],
        theta=theta2,
        width=width,
        marker_color='red',
        marker_line_color="black",
        marker_line_width=2,
        opacity=0.9,
        name='Searched Song',
        hovertext=df.iloc[12],
        hoverinfo="text",
    ))

    fig.add_trace(go.Barpolar(
        r=df.iloc[2],
        theta=theta3,
        width=width,
        marker_color='gray',
        marker_line_color="black",
        marker_line_width=2,
        opacity=0.9,
        name=(f"{songs[0]} by {artist_cleaned[0]}"),
        hovertext=df.iloc[7],
        hoverinfo="text",
    ))

    fig.add_trace(go.Barpolar(
        r=df.iloc[3],
        theta=theta4,
        width=width,
        marker_color='violet',
        marker_line_color="black",
        marker_line_width=2,
        opacity=0.9,
        name=(f"{songs[1]} by {artist_cleaned[1]}"),
        hovertext=df.iloc[8],
        hoverinfo="text",
    ))

    fig.add_trace(go.Barpolar(
        r=df.iloc[4],
        theta=theta5,
        width=width,
        marker_color='purple',
        marker_line_color="black",
        marker_line_width=2,
        opacity=0.9,
        name=(f"{songs[2]} by {artist_cleaned[2]}"),
        hovertext=df.iloc[9],
        hoverinfo="text",
    ))

    fig.add_trace(go.Barpolar(
        r=df.iloc[5],
        theta=theta6,
        width=width,
        marker_color='blue',
        marker_line_color="black",
        marker_line_width=2,
        opacity=0.9,
        name=(f"{songs[3]} by {artist_cleaned[3]}"),
        hovertext=df.iloc[10],
        hoverinfo="text",
    ))

    fig.add_trace(go.Barpolar(
        r=df.iloc[6],
        theta=theta7,
        width=width,
        marker_color='orange',
        marker_line_color="black",
        marker_line_width=2,
        opacity=0.9,
        name=(f"{songs[4]} by {artist_cleaned[4]}"),
        hovertext=df.iloc[11],
        hoverinfo="text",
    ))

    fig.update_layout(
        template='none',
        width=800,
        height=800,
        hoverlabel=dict(
            namelength=-1,
            bgcolor="white",
            bordercolor='black',
            font_size=16,
            font_family="Rockwell",
        ),
        polar=dict(
            radialaxis=dict(range=[df[0:7].values.min(), df[0:7].values.max() + .1], showticklabels=False,
                            ticks=''),
            angularaxis=dict(showticklabels=True, tickmode='array', tickvals=vals, ticktext=df.columns, ticks=''),
        ),
        title={
            'text': "<b>Comparing Audio Features</b>",
            'y': 0.95,
            'x': 0.51,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20}},
        legend={
            'y': -0.33,
            'x': 0.49,
            'xanchor': 'center',
            'yanchor': 'bottom'},
    )

    chart_studio.tools.set_credentials_file(username=cs_username, api_key=cs_api_key)
    embed_var = py.plot(fig, filename = 'pleasedonotbreakkk', auto_open=True, fileopt='new')
    return embed_var