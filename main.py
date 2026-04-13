from datetime import datetime, timedelta
from etl.extract import extract_recent_playlist
from etl.transform import transform
from etl.load import load
from llm.spotifyAnalitics import *
import sys


if __name__ == "__main__":
    date_t = datetime.today() - timedelta(days=1)

    print("🚀 Starting pipeline ETL...")
    print(f"📅 Processing data from: {date_t.strftime('%Y-%m-%d %H:%M:%S')}\n")

    #Extract
    print("📥 STEP 1: EXTRACT")

    data_raw = extract_recent_playlist(date_t)
    if data_raw is None:
        print("\n❌ Error: Data extraction failed. The program will exit.")
        print("   Potential causes:")
        print("   - Connection problems with the Spotify API")
        print("   - Access token expired or invalid.")
        print("   - Query param error")
        sys.exit(1)  # The script exit with error code 1

    if not data_raw or not data_raw.get('items'):
        print("\n⚠️ Warning: No data available for this date")
        print("   The program will exit as there is no data to process.")
        sys.exit(0)  # Success exit with zero records processed

    print(f"✅ Extracted {len(data_raw['items'])} registers\n")

    #Transform
    print("📥 STEP 2: TRANSFORM")
    print("🔄 Transforming data...")
    try:
        clean_df = transform(data_raw)
        print(f"✅ Transformed {len(clean_df)} registers\n")
        print(clean_df.to_string(
            index=False,
            max_colwidth=250,
            justify='center'
        ))
    except Exception as e:
        print(f"❌ Data transformation failed: {e}")
        sys.exit(1)

    # Load
    print("\n💾 STEP 3: LOAD")
    try:
        success = load(clean_df)
    except Exception as e:
        print(f"❌ Data load error: {e}")
        sys.exit(1)

    if not success:
        print("❌ Data loading to the database has failed")
        sys.exit(1)

    print("\n🎉 Pipeline ETL completed successfully ✅")
    print(f"📊 Total records: {len(clean_df)}\n")

    print("🤖 STEP 4 LLM: GENERATE AN ANALYSIS OF THE PLAYLIST")
    mood = analyze_mood(clean_df)
    print(f"\n😊 Analyze mood:\n{mood}")

    description = generate_general_description(clean_df)
    print(f"\n😊 General description:\n{description}")

    playlist_name = suggest_playlist_name(clean_df)
    print(f"\n💿 Suggest playlist name:\n{playlist_name}")

    obsessions = identify_obsessions(clean_df)
    print(f"\n🤪 Obsessions:\n{obsessions}")
