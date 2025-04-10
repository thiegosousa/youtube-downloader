# youtube-downloader
Baixar vídeos do youtube

# YouTube Downloader Pro

![Streamlit](https://img.shields.io/badge/Streamlit-1.44.1-red) ![yt-dlp](https://img.shields.io/badge/yt--dlp-2025.3.31-blue) ![License](https://img.shields.io/badge/license-MIT-green)

Um aplicativo web simples e poderoso construído com Streamlit para baixar vídeos do YouTube em diferentes resoluções (até 720p). Utiliza a biblioteca `yt-dlp` para processar e baixar os vídeos diretamente no navegador.

## Funcionalidades
- Insira um link do YouTube e veja informações como título, canal, duração e visualizações.
- Escolha entre resoluções disponíveis (720p, 480p, 360p, 240p).
- Baixe vídeos em formato MP4 com um clique.
- Interface amigável com design personalizado.

## Pré-requisitos
- Python 3.7 ou superior
- FFmpeg instalado (necessário para mesclar vídeo e áudio)

## Instalação Local

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/thiego/youtube-downloader.git
   cd youtube-downloader

    Instale as Dependências
    bash

pip install -r requirements.txt
Instale o FFmpeg

    Linux (Ubuntu/Debian):
    bash

sudo apt update
sudo apt install ffmpeg
Windows: Baixe em ffmpeg.org e adicione ao PATH.
macOS:
bash

    brew install ffmpeg

Execute o Aplicativo
bash

    streamlit run youtube_downloader.py
    O aplicativo abrirá em http://localhost:8501.

Uso

    Cole um link válido do YouTube no campo de texto (ex.: https://www.youtube.com/watch?v=dQw4w9WgXcQ).
    Selecione a resolução desejada.
    Clique em "Baixar Agora" e, após o processamento, clique em "Salvar Vídeo" para fazer o download.

Deploy no Streamlit Community Cloud

    Crie um Repositório no GitHub
        Faça upload dos arquivos youtube_downloader.py, requirements.txt e packages.txt.
    Estrutura do Repositório
    text

youtube-downloader/
├── youtube_downloader.py  # Código principal
├── requirements.txt       # Dependências Python
├── packages.txt           # Pacotes do sistema (FFmpeg)
├── README.md              # Este arquivo
Conteúdo dos Arquivos

    requirements.txt:
    text

streamlit
yt-dlp
packages.txt:
text

        ffmpeg
    Deploy
        Acesse streamlit.io/cloud.
        Conecte-se ao GitHub e selecione o repositório youtube-downloader.
        Defina youtube_downloader.py como o arquivo principal e clique em "Deploy".
        O aplicativo estará disponível em um URL público (ex.: https://youtube-downloader-xyz.streamlit.app).

Notas Importantes

    FFmpeg: Necessário para mesclar streams de vídeo e áudio. Certifique-se de que está instalado localmente ou incluído no packages.txt para o Streamlit Cloud.
    Limitações: Vídeos privados ou restritos por idade podem não funcionar sem autenticação adicional no yt-dlp.
    Direitos Autorais: Use este aplicativo apenas para conteúdo que você tem permissão para baixar.

Resolução de Problemas

    Erro "FFmpeg não instalado":
        Localmente: Instale o FFmpeg conforme as instruções acima.
        Streamlit Cloud: Verifique se packages.txt contém ffmpeg e redeploy o aplicativo.
    Vídeo não baixa:
        Confirme se o link é válido e o vídeo não é restrito.

Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests no repositório GitHub.
Licença

Este projeto está licenciado sob a .

Feito com ❤️ por [Thiego] usando Streamlit e yt-dlp.
