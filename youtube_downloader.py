import streamlit as st
from yt_dlp import YoutubeDL
import re
from io import BytesIO

# Configurações de página
st.set_page_config(
    page_title="YT Downloader Pro",
    page_icon="🎬",
    layout="centered",
)

# CSS personalizado
st.markdown("""
    <style>
    .header {
        border-bottom: 2px solid #FF4B4B;
        padding-bottom: 15px;
        margin-bottom: 30px;
    }
    .stTextInput input {
        border-radius: 20px !important;
        padding: 12px !important;
    }
    .stSelectbox [data-baseweb=select] {
        border-radius: 15px !important;
    }
    </style>
""", unsafe_allow_html=True)

def sanitize_filename(filename):
    """Remove caracteres inválidos para nome de arquivo"""
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def get_video_info(url):
    """Obtém informações do vídeo usando yt-dlp"""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info, None
    except Exception as e:
        return None, f"Erro ao obter informações: {str(e)}"

def download_video(url, resolution):
    """Faz o download do vídeo na resolução especificada"""
    ydl_opts = {
        'format': f'bestvideo[height<={resolution[:-1]}]+bestaudio/best[height<={resolution[:-1]}]',
        'merge_output_format': 'mp4',
        'quiet': True,
        'no_warnings': True,
        'outtmpl': '%(title)s.%(ext)s',  # Nome temporário, será ajustado depois
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            # Lê o arquivo baixado para um buffer
            filename = ydl.prepare_filename(info)
            with open(filename, 'rb') as f:
                buffer = BytesIO(f.read())
            # Remove o arquivo temporário
            import os
            os.remove(filename)
            buffer.seek(0)
            return buffer, None, info
    except Exception as e:
        return None, f"Erro ao baixar: {str(e)}", None

# Interface principal
st.markdown('<h1 class="header">📥 YouTube Video Downloader Pro</h1>', unsafe_allow_html=True)

url = st.text_input("Cole o link do YouTube aqui:", placeholder="https://youtube.com/watch?v=...")

if url:
    try:
        with st.spinner("🔍 Analisando o vídeo..."):
            info, error = get_video_info(url)
            if not info:
                st.error(error)
            else:
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(info.get('thumbnail'), use_container_width=True)
                
                with col2:
                    st.subheader(sanitize_filename(info.get('title', 'Vídeo sem título')))
                    st.caption(f"""
                    **Canal:** {info.get('uploader', 'Desconhecido')}  
                    **Duração:** {info.get('duration', 0) // 60}:{info.get('duration', 0) % 60:02d}  
                    **Visualizações:** {info.get('view_count', 0):,}
                    """)
                
                # Resoluções disponíveis (limitadas a 720p para compatibilidade com stream progressivo)
                resolutions = ['720p', '480p', '360p', '240p']
                selected_res = st.selectbox("Selecione a resolução:", resolutions)
                
                if st.button("⬇️ Baixar Agora", type="primary"):
                    with st.spinner(f"Baixando em {selected_res}..."):
                        video_buffer, error, info = download_video(url, selected_res)
                        if video_buffer:
                            st.success("✅ Download concluído!")
                            st.download_button(
                                label="Salvar Vídeo",
                                data=video_buffer,
                                file_name=f"{sanitize_filename(info.get('title', 'video')[:45])} ({selected_res}).mp4",
                                mime="video/mp4",
                                key="download_button"
                            )
                        else:
                            st.error(f"❌ {error}")
                            
    except Exception as e:
        st.error(f"""
        **Erro ao processar o vídeo:**  
        {str(e)}  
        
        *Soluções possíveis:*  
        1. Verifique se o link está correto  
        2. Confirme se o vídeo não é privado/restrito por idade  
        3. Tente novamente mais tarde
        """)

st.markdown("---")
st.info("""
**Notas importantes:**  
• Vídeos restritos por idade podem exigir autenticação adicional  
• Respeite os direitos autorais  
• Requer yt-dlp: `pip install yt-dlp`
""")