import justpy as jp

# The way you can find any type of styling - quasar style, https://quasar.dev/style

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analasys of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course reviews analysys")

    return wp

jp.justpy(app)
