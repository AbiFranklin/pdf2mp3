import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('giffraffeBook.pdf', 'rb'))
speaker = pyttsx3.init()
final_text=""

for page_num in range(3, 15):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    final_text += clean_text

speaker.save_to_file(final_text, "story.mp3")
speaker.runAndWait()

speaker.stop()

