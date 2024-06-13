import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pydub import AudioSegment

# Define your app instance
app = Client("EQURO_BOT")

def convert_video_to_text(video_path):
    # Placeholder function, replace with actual implementation
    return "Extracted text from the video"

@app.on_message(filters.command("vtxt") & filters.reply)
def convert_video_to_text_cmd(client, message: Message):
    # Download the replied video
    video_path = message.reply_to_message.download("video.mp4")

    # Convert the video to text (replace with actual function implementation)
    text_result = convert_video_to_text(video_path)

    # Write the text to a file
    with open("file.txt", "w", encoding="utf-8") as file:
        file.write(text_result)

    # Reply with the text file
    message.reply_document("file.txt")

    # Cleanup
    os.remove(video_path)
    os.remove("file.txt")

@app.on_message(filters.command("remove", prefixes="/") & filters.reply)
def remove_media(client, message: Message):
    # Fetching the replied message
    replied_message = message.reply_to_message

    if replied_message.video:
        # If the replied message is a video, remove either the audio or the video depending on the command
        if len(message.command) > 1:
            command = message.command[1].lower()
            file_path = client.download_media(replied_message.video)

            if command == "audio":
                # Remove audio
                os.system(f"ffmpeg -i {file_path} -c copy -an output.mp4")
                client.send_video(message.chat.id, "output.mp4")
                os.remove("output.mp4")
            elif command == "video":
                # Remove video
                audio = AudioSegment.from_file(file_path)
                audio = audio.set_channels(1)
                audio.export("output.mp3", format="mp3")
                client.send_audio(message.chat.id, "output.mp3")
                os.remove("output.mp3")
            else:
                client.send_message(message.chat.id, "Invalid command. Please use either /remove audio or /remove video.")
            
            # Cleanup
            os.remove(file_path)
        else:
            client.send_message(message.chat.id, "Please specify whether to remove audio or video using /remove audio or /remove video.")
    else:
        client.send_message(message.chat.id, "The replied message is not a video.")

# Start the bot
app.run()
