import smtplib

def test_smtp_connection():
    try:
        with smtplib.SMTP_SSL("smtp.hostinger.com", 465) as server:
            server.login("ventas@tecnomata.com", "Vg30dett4life.")
            print("Conexión SMTP exitosa.")
    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación SMTP. Verifica las credenciales.")
    except Exception as e:
        print(f"Error de conexión SMTP: {e}")

test_smtp_connection()
