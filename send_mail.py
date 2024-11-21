import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(name, contact_method, contact_info, selected_pack):
    sender_email = os.getenv("EMAIL_USER")
    receiver_email = "soporte@tecnomata.com"
    password = os.getenv("EMAIL_PASSWORD")

    subject = "Nuevo contacto desde el sitio Web"
    body = f"""
    Has recibido una nueva solicitud de contacto:

    Nombre: {name}
    Método de Contacto: {contact_method}
    Información de Contacto: {contact_info}
    Paquete Seleccionado: {selected_pack}
    """

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # Conexión SMTP
        with smtplib.SMTP_SSL("smtp.hostinger.com", 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
            print("Correo enviado correctamente")
    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación SMTP. Verifica las credenciales.")
    except smtplib.SMTPException as e:
        print(f"Error general de SMTP: {e}")
    except Exception as e:
        print(f"Error desconocido: {e}")
