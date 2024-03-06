from guizero import App, TextBox, Drawing

def draw_meme():
  meme.clear()
  meme.image(0, 0, "kitten.png")
  meme.text(20, 20, top_text.value)
  meme.text(20, 320, bottom_text.value)

app = App("meme")

top_text = TextBox(app, "top text")
bottom_text = TextBox(app, "bottom text")

meme = Drawing(app, width = "fill", height = "fill")

draw_meme()

app.display()