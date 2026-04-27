import platform

def play_background_music(file_path):

    if platform.system() == "Windows":  #Checks if the OS is Windows, if not won't play music 
        try:
            import winsound  # Not at top because it will crash  Mac/Linux

            winsound.PlaySound(file_path, winsound.SND_ASYNC | winsound.SND_LOOP)
        except Exception as e:
            print(f"Windows sound error: {e}")
    else:
        # Not on Windows? Just pass and do nothing.
        pass