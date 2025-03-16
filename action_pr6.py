import text_to_speech_pr6
import speech_to_text_p6
import datetime
import webbrowser

def action(data):
    user_data=data.lower()

    if "what is your name" in user_data:
        text_to_speech_pr6.text_to_speech("My name is AI Bot")
        return "My name is AI Bot"
    elif "hello" in user_data or "hye" in user_data:
        text_to_speech_pr6.text_to_speech("Hi how can i help you")
        return "Hi how can i help you"
    elif "good morning"  in user_data:
        text_to_speech_pr6.text_to_speech("Good morning sir ")
        return "Good morning sir "
    elif "play music"  in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech_pr6.text_to_speech("ready for you")
        return "spotify ready for you"
    elif "open leetcode"  in user_data:
        webbrowser.open("https://leetcode.com/problemset/")
        text_to_speech_pr6.text_to_speech("ready for you")
        return "leetcode ready for you"
    elif "open netflix"  in user_data:
        webbrowser.open("https://www.netflix.com/browse")
        text_to_speech_pr6.text_to_speech("ready for you")
        return "netflix ready for you"
    elif "open youtube"  in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech_pr6.text_to_speech("ready for you")
        return "youtube ready for you"
    elif "open google"  in user_data:
        webbrowser.open("https://www.google.co.in/")
        text_to_speech_pr6.text_to_speech("ready for you")
        return "google ready for you"
    elif "open chatgpt"  in user_data:
        webbrowser.open("https://chatgpt.com/?model=auto")
        text_to_speech_pr6.text_to_speech("ready for you")
        return "chatgpt ready for you"
    elif"time now" in user_data:
        current_time=datetime.datetime.now()
        time=(str)(current_time)+"hour:",(str)(current_time.minute)+"minute"
        text_to_speech_pr6.text_to_speech(time)
    else:
        text_to_speech_pr6.text_to_speech("I'm not able to understand")