from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

video_ids = {"Tools to Bolster Your Mood & Mental Health":"CJIXbibQ0jI",
             "Dr. Paul Conti: Tools and Protocols for Mental Health":"yOJvm_ri_hk",
             "Dr. Paul Conti: How to Build and Maintain Healthy Relationships":"eMqWH3LYiII",
             "How to Use Music to Boost Motivation, Mood & Improve Learning":"eMqWH3LYiII",
             "How to Breathe Correctly for Optimal Health, Mood, Learning & Performance":"x4m_PdFbu-s",
             "Dr. Chris Palmer: Diet & Nutrition for Mental Health":"xjEFo3a1AnI",
             "Nicotine’s Effects on the Brain & Body & How to Quit Smoking or Vaping":"uXs-zPc63kM",
             "The Science & Process of Healing from Grief":"dzOvi0Aa2EA",
             "Understanding & Conquering Depression":"Xu1FMCxoEFc",
             "Maximizing Productivity, Physical & Mental Health with Daily Tools":"aXvDEmo6uS4",
             "Essentials: Master Your Sleep & Be More Alert When Awake":"lIo9FcrljDk",
             "Optimal Protocols for Studying & Learning":"ddq8JIMhz7c",
             "Tools to Enhance Working Memory & Attention":"CQlTmOFM4Qs",
             "A Science-Supported Journaling Protocol to Improve Mental & Physical Health":"wAZn9dF3XTo",
             "Tools for Optimizing Sleep & Sleep-Wake Timing":"h2aWYjSA1Jc",
             "Dr. Stacy Sims: Female-Specific Exercise & Nutrition for Health, Performance & Longevity":"pZX8ikmWvEU",
             "The Science of Emotions & Relationships":"qdk7XuBgSjw",
             "How to Increase Motivation & Drive":"OLQRAMZi--c"
             } 
for video_name, video_id in video_ids.items():
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([entry["text"] for entry in transcript])
        filename = video_name + ".txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(full_text)
        print(f"Saved transcript for {video_name}")
    except NoTranscriptFound:
        print(f"No transcript found for {video_name} ({video_id})")
    except TranscriptsDisabled:
        print(f"Transcripts are disabled for {video_name} ({video_id})")
    except Exception as e:
        print(f"An error occurred for {video_name} ({video_id}): {e}")
print("done with all of them")


