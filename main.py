import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from PIL import Image, ImageTk
import webbrowser

def open_trailer(trailer_url):
    """Abre o trailer no navegador."""
    webbrowser.open(trailer_url)

def open_poster_large(image_path):
    """Abre a imagem do pôster em tamanho maior em uma nova janela."""
    top = tk.Toplevel()
    top.title("Pôster em Tamanho Maior")
    top.configure(bg="black")

    try:
        # Abre a imagem e a exibe em tamanho maior
        image = Image.open(image_path)
        poster_large = ImageTk.PhotoImage(image)
        poster_label = ttk.Label(top, image=poster_large, style="Custom.TLabel")
        poster_label.image = poster_large  # Referência para evitar garbage collection
        poster_label.pack(padx=20, pady=20)
    except Exception as e:
        print(f"Erro ao abrir pôster em tamanho maior: {e}")

def create_movie_frame(parent, movie_data, style):
    """Cria um frame para exibir os detalhes de um filme."""
    frame = ttk.Frame(parent, style="Custom.TFrame", padding=10)

    try:
        # Pôster do filme
        image = Image.open(movie_data['poster'])
        image = image.resize((120, 160))  # Ajusta o tamanho da imagem
        poster = ImageTk.PhotoImage(image)
        poster_label = ttk.Label(frame, image=poster, style="Custom.TLabel")
        poster_label.image = poster  # Referência para evitar garbage collection
        poster_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky="nsew")

        # Vincula o clique do pôster para abrir a imagem em tamanho maior
        poster_label.bind("<Button-1>", lambda e: open_poster_large(movie_data['poster']))

        # Título do filme
        title_label = ttk.Label(frame, text=movie_data['titulo'], style="Custom.TLabel", font=('Times New Roman', 20))
        title_label.grid(row=0, column=1, sticky='w')

        # Sinopse do filme
        synopsis_label = ttk.Label(frame, text="Sinopse:", style="Custom.TLabel", font=('Times New Roman', 14))
        synopsis_label.grid(row=1, column=1, sticky='w')

        synopsis_text = ttk.Label(frame, text=movie_data['sinopse'], style="Custom.TLabel", wraplength=300, justify='left', font=('Arial', 10))
        synopsis_text.grid(row=2, column=1, sticky='w')

        # Atores do filme
        actors_label = ttk.Label(frame, text="Atores:", style="Custom.TLabel", font=('Times New Roman', 14))
        actors_label.grid(row=3, column=1, sticky='w')

        actors_text = ttk.Label(frame, text=', '.join(movie_data['atores']), style="Custom.TLabel", wraplength=300, justify='left', font=('Arial', 10))
        actors_text.grid(row=4, column=1, sticky='w')

        # Botão do trailer com estilo personalizado
        trailer_button_style = "TrailerButton.TButton"
        style.configure(trailer_button_style,
        foreground="black",
        background="white",
        font=('Times New Roman', 10))
        # Botão do trailer
        trailer_button = ttk.Button(frame, text="Trailer", style=trailer_button_style, command=lambda: open_trailer(movie_data['trailer_url']))
        trailer_button.grid(row=5, column=1, pady=2, sticky='w')

        # Ajusta as dimensões internas do frame
        frame.grid_columnconfigure(1, weight=1, minsize=200)  # Ajuste da largura
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_rowconfigure(3, weight=1)

    except Exception as e:
        print(f"Erro ao criar frame para {movie_data['titulo']}: {e}")

    return frame


def main():
    movies = [
        {
            'titulo': "As Crônicas de Nárnia",
            'poster': "cronicas.jpeg",  # Verifique o caminho da imagem
            'sinopse': "Durante a Segunda Guerra Mundial, quatro irmãos (Lucy, Edmund, Susan e Peter Pevensie) são enviados para o interior da Inglaterra para se protegerem dos bombardeios em Londres. Lá, na casa de um professor, eles descobrem um guarda-roupa mágico que os transporta para o mundo encantado de Nárnia. Nárnia está sob o domínio da Feiticeira Branca, que impôs um inverno eterno sobre a terra. Com a ajuda do leão Aslam, os irmãos lideram uma batalha para libertar Nárnia do domínio da feiticeira e trazer de volta a paz e o verão ao reino.",
            'atores': ["Georgie Henley", "Skandar Keynes", "Anna Popplewell", "William Moseley", "Tilda Swinton", "Liam Neeson."],
            'trailer_url': "https://youtu.be/usEkWtuNn-w"
        },
        {
            'titulo': "Interstellar",
            'poster': "interstellar.png",  # Verifique o caminho da imagem
            'sinopse': "Em um futuro próximo, a Terra está enfrentando uma crise alimentar global e um ambiente devastado por tempestades de poeira. Cooper, um ex-piloto e engenheiro da NASA, se vê envolvido em uma missão espacial destinada a salvar a humanidade. Ele é recrutado para liderar uma expedição através de um buraco de minhoca, que foi descoberto por uma força misteriosa, com o objetivo de encontrar um novo planeta habitável.Interstellar explora temas como o amor, o tempo, a relatividade e a sobrevivência humana, com visuais deslumbrantes e uma narrativa profunda e emocionante.",
            'atores': ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain."],
            'trailer_url': "https://www.youtube.com/watch?v=zSWdZVtXT7E"
        },
        {
            'titulo': "Wicked",
            'poster': "img_3.jpg",
            'sinopse': "Wicked é uma adaptação do romance de Gregory Maguire, que oferece uma reinterpretação da história clássica de O Mágico de Oz. A trama se concentra na amizade entre duas bruxas, Elphaba e Glinda, antes dos eventos conhecidos no mundo de Oz. Elphaba, que nasce com pele verde e é rejeitada pela sociedade, se torna a Bruxa Má do Oeste. Já Glinda, a popular e charmosa Bruxa Boa do Norte, começa como uma jovem superficial e ingênua, mas ao longo da história, as duas passam a desenvolver uma amizade inesperada.",
            'atores': ["Cynthia Erivo", "Ariana Grande", "Jonathan Bailey","Michelle Yeoh","Jeff Goldblum." ],
            'trailer_url': "https://youtu.be/T4h72s490HU"
        },
        {
            'titulo': "O Rei do Show",
            'poster': "img_4.jpg",  # Verifique o caminho da imagem
            'sinopse': "O Rei do Show é um musical inspirado na história real de P.T. Barnum, um empresário visionário que fundou o primeiro circo de variedades do mundo, o Barnum & Bailey Circus. O filme segue a jornada de Barnum, interpretado por Hugh Jackman, que, depois de passar por dificuldades financeiras e sociais, decide criar um espetáculo único, reunindo pessoas consideradas fora dos padrões da sociedade, como anões, pessoas com deficiências e outras figuras excêntricas.",
            'atores': ["Hugh Jackman", "Zac Efron", "Zendaya."],
            'trailer_url': "https://youtu.be/r5R6CVp_JzU?si=TCfelG99dIghm7f8"
        },
        {
            'titulo': "Frozen",
            'poster': "img_5.jpg",
            'sinopse': "Frozen conta a história de duas irmãs, Elsa e Anna, que vivem no reino de Arendelle. Elsa possui poderes mágicos que lhe permitem controlar o gelo e a neve, mas, ao longo de sua infância, ela luta para controlar esses poderes, o que acaba gerando uma série de eventos inesperados.",
            'atores': ["Idina Menzel ", "Kristen Bell", "Josh Gad ", "Jonathan Groff."],
            'trailer_url': "https://youtu.be/FLzfXQSPBOg?si=IQuYyvOEcgSR6NEt"
        },
        {
            'titulo': "Harry Potter e a Pedra Filosofal",
            'poster': "img_7.jpg",
            'sinopse': "Harry Potter e a Pedra Filosofal é o primeiro filme da série baseada nos livros de J.K. Rowling. A história segue Harry Potter, um garoto de 11 anos que descobre ser um bruxo ao receber uma carta de admissão para estudar na Escola de Magia e Bruxaria de Hogwarts. Criado por seus tios que o tratam mal, Harry sempre se sentiu fora de lugar, mas ao chegar a Hogwarts, descobre um mundo mágico e suas origens.",
            'atores': ["Daniel Radcliffe", "Rupert Grint", "Emma Watson", "Richard Harris ", "Alan Rickman."],
            'trailer_url': "https://youtu.be/9fIObnIGMlI"
        },
    ]

    # Configuração da janela principal
    root = tk.Tk()
    root.title("Filmes e Trailers")
    root.wm_iconbitmap('claquete.ico')
    root.configure(bg="black")

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Title.TLabel", font=("Times New Roman", 40, "bold"), background="black", foreground="pink")

    # Título dentro da janela
    title_label = ttk.Label(root, text="Filmes e Trailers", style="Title.TLabel")
    title_label.pack(pady=10)  


    # Estilo personalizado
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Custom.TFrame", background="black")
    style.configure("Custom.TLabel", background="black", foreground="white")

    # Frame principal para os filmes
    main_frame = ttk.Frame(root, padding=10, style="Custom.TFrame")
    main_frame.pack(fill="both", expand=True)

    # Exibe os filmes em um grid
    row, col = 0, 0
    for movie in movies:
        movie_frame = create_movie_frame(main_frame, movie, style)
        movie_frame.grid(row=row, column=col, padx=10, pady=10)

        col += 1
        if col == 3:
            col = 0
            row += 1

    root.mainloop()


if __name__ == "__main__":
    main()
