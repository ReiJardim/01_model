from models import session, Usuario
import streamlit_authenticator as stauth

senha_criptografada = stauth.Hasher(["741852963"]).generate()[0]
usuario = Usuario(nome="King", senha=senha_criptografada,
                  email="king.carlos.garden@gmail.com", admin=False)
session.add(usuario)
session.commit()
