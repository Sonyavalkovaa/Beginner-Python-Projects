from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stop_playing = int(input("press 0 when you want to stop the music playing"))
    if stop_playing == 0:
      source.paused = True
      return 
    else: 
      continue 
  
while True: 
  # clear the screen
  os.system("clear")
  print("MUSIC IPOD PLAYER")
  time.sleep(1)
  print()
  print("press 1 to play the tunes")
  time.sleep(1)
  print("press 0 when you want to stop the tune playing")
  time.sleep(1)
  user= int(input())
  if user == 1: 
    print("Tune starting to play now!")
    os.system("clear")
    play()
  elif user == 0: 
    exit()
  else: 
    continue 