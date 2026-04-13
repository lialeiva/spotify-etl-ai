from connection.openAIConnection import openai_connection

client = openai_connection()

def get_llm_response(prompt):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-5.2",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        description = response.choices[0].message.content.strip()

        return description
    except Exception as e:
        print(f"❌ Failed to generate description: {e}")
        return None


def generate_general_description(df):
    prompt = f"Generate a natural language description about musical tastes based on this playlist:\n{df[['artist', 'track']].head(10).to_string(index=False)}"
    return get_llm_response(prompt)


def analyze_mood(df):
    """Analyzes the mood of the playlist"""
    prompt = f"""
    Based on these recently played songs, describe the overall mood and emotions:
    Top songs:
    {df[['artist', 'track']].head(10).to_string(index=False)}
    3-4 sentences.
    """
    return get_llm_response(prompt)


def get_recommendations(df):
    """Generates recommendations based on a playlist."""
    top_artists = df['artist'].value_counts().head(5).to_dict()

    prompt = f"""
    Based on these top artists I listen to: {', '.join(top_artists.keys())}
    Recommend 5 similar artists I might enjoy.
    For each artist, explain why you recommend them.
    """
    return get_llm_response(prompt)


def create_playlist_summary(df):
    """Generates a full summary of the playlist."""
    total_songs = len(df)
    unique_artists = df['artist'].nunique()
    top_artist = df['artist'].value_counts().index[0]

    prompt = f"""
    Create a engaging summary of my Spotify listening:
    - Total songs: {total_songs}
    - Unique artists: {unique_artists}
    - Most played artist: {top_artist}
    Write a creative, fun summary (max 100 words).
    """
    return get_llm_response(prompt)


def suggest_playlist_name(df):
    """Sugiere nombres creativos para la playlist"""
    prompt = f"""
    Based on these songs:
    {df[['artist', 'track']].head(15).to_string(index=False)}

    Suggest 5 creative names for a Spotify playlist containing these songs.
    Names should be clever, catchy, and reflect the music style.
    """
    return get_llm_response(prompt)


def identify_obsessions(df):
    """Identify over-listened artists or songs."""
    top_song = df['track'].value_counts().head(1)

    song_name = list(top_song.keys())[0]
    play_count = list(top_song.values)[0]

    prompt = f"""
    I've played "{song_name}" {play_count} times recently.

    What does this say about me? Am I obsessed, going through something, 
    or just really loving this song? Answer with humor (max 100 words).
    """
    return get_llm_response(prompt)