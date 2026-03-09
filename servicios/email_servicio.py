



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



#  CONFIGURACIÓN — editá solo estos tres valores

SMTP_USER    = "martinlopez211201@gmail.com"   # Tu Gmail
SMTP_PASS    = "dyuhwisxlbcqdkas"      # App Password de 16 caracteres (sin espacios)
SMTP_ENABLED = True                    # False para deshabilitar sin borrar credenciales



SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT   = 587


class EmailServicio:
    
    #Servicio de envío de correos electrónicos via Gmail SMTP.
    #Uso desde run_gui.py  →  email_servicio = EmailServicio.desde_env()
    #Uso desde pantallas   →  ok, msg = self.ventana.email_servicio.enviar_texto(...)
    
    def __init__(self, username: str = "", password: str = "", enabled: bool = False):
        self.username = username
        self.password = password
        self.enabled  = enabled

    @staticmethod
    def desde_env() -> "EmailServicio":
        
        #Crea la instancia leyendo las constantes definidas arriba.
        #Es el método que llama run_gui.py.
        
        return EmailServicio(
            username = SMTP_USER,
            password = SMTP_PASS,
            enabled  = SMTP_ENABLED,
        )


    # Verificación de configuración

    def configurado(self) -> bool:
        
        #Devuelve True si el servicio está habilitado y tiene credenciales reales cargadas.
        #Las pantallas llaman a este método antes de intentar enviar.
        
        return (
            self.enabled
            and bool(self.username.strip())
            and bool(self.password.strip())
            and self.username != "tu_correo@gmail.com"  # placeholder → aún no configurado
        )


    # Envío en texto plano

    def enviar_texto(self, para: str, asunto: str, cuerpo: str) -> tuple[bool, str]:
        
        #Envía un correo en texto plano.
        #Retorna (True, "Correo enviado") o (False, "descripción del error").
        
        if not self.configurado():
            return False, "El servicio de email no está configurado."

        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = asunto
            msg["From"]    = self.username
            msg["To"]      = para
            msg.attach(MIMEText(cuerpo, "plain"))

            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.ehlo()
                server.starttls()
                server.login(self.username, self.password)
                server.sendmail(self.username, para, msg.as_string())

            return True, "Correo enviado correctamente."

        except smtplib.SMTPAuthenticationError:
            return False, (
                "Error de autenticación.\n"
                "Verificá que el email y la App Password sean correctos."
            )
        except smtplib.SMTPRecipientsRefused:
            return False, f"El correo destino '{para}' fue rechazado por el servidor."
        except Exception as e:
            return False, f"Error al enviar el correo: {str(e)}"


    # Envío HTML (opcional, para correos con estilo)

    def enviar_html(self, para: str, asunto: str, cuerpo_html: str) -> tuple[bool, str]:
        
        #Igual que enviar_texto pero renderiza HTML.
        
        if not self.configurado():
            return False, "El servicio de email no está configurado."

        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = asunto
            msg["From"]    = self.username
            msg["To"]      = para
            msg.attach(MIMEText(cuerpo_html, "html"))

            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.ehlo()
                server.starttls()
                server.login(self.username, self.password)
                server.sendmail(self.username, para, msg.as_string())

            return True, "Correo enviado correctamente."

        except smtplib.SMTPAuthenticationError:
            return False, (
                "Error de autenticación.\n"
                "Verificá que el email y la App Password sean correctos."
            )
        except smtplib.SMTPRecipientsRefused:
            return False, f"El correo destino '{para}' fue rechazado por el servidor."
        except Exception as e:
            return False, f"Error al enviar el correo: {str(e)}"