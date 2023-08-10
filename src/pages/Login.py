import streamlit as st
import streamlit_authenticator as stauth
import yaml
from streamlit.components.v1 import html


def nav_page(page_name, timeout_secs=3):
    st.markdown("<a href='/'>home</a>", unsafe_allow_html=True)
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                links[0].click()
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)


with open('config.yaml') as coverFile:
    config = yaml.load(coverFile, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

css = f'''
        <style>
        *{{
            box-sizing: "border-box"
        }}
        header {{visibility: hidden;}}
        span.css-10trblm{{

        }}
        img[alt="logo"]{{
            width: 50px;
            height: 50px;
             (.9);
            }}
        .block-container{{
            padding-top:0px;
            margin-top:0px;

        }}
        button[role="tab"]>div>p{{
            font-size:1.4rem;
            margin-bottom: 1rem;
        }}
        button[role="tab"]{{
            background: none;
        }}
        .row-widget.stButton,.row-widget.stDownloadButton{{
            display:flex;
            justify-content:center;
        }}
        div[data-baseweb="tab-highlight"]{{
        }}
        div[data-testid="stVerticalBlock"]{{


        }}
        div[role="tablist"]{{
            padding-top:0rem;
            margin: 10px 0px;
        }}
        div[data-testid="stCaptionContainer"]{{
            font-size:1.1rem;
        }}
        </style>
        '''
st.title(
    "![logo](https://cdn-icons-png.flaticon.com/512/29/29184.png) Binary Steganography", anchor="binary-steganography")
st.caption("Steganography is the technique of hiding secret data within an ordinary, non-secret, file or message in order to avoid detection this tool hides your secret data in a exe/elf executable file ")
st.markdown(css, unsafe_allow_html=True)

name, authentication_status, username = authenticator.login(
    'Login', 'main')
if authentication_status:
    nav_page("/")
elif authentication_status == False:
    st.error('Username/password is incorrect', icon="⁉️")
elif authentication_status == None:
    st.warning('Login to continue', icon="⚠️")
