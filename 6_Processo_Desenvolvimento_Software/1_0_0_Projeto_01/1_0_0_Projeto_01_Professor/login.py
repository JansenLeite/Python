import mod_msg
import mod_inputs

USUARIO =  "jansen"
SENHA = "12345"

def valida_usuario(user):
    while True:
        usuario = mod_inputs.recebe_str("Digite o seu usuário: ")
        if len(usuario) >= 5:
            if user == usuario:
                break
            else:
                print("Usuário incorreto!\n")
        else:
            print("O usuário deve conter ao menos 5 caracteres!")
    return usuario

def valida_senha(senha1):
    while True:
        senha = mod_inputs.recebe_senha("Digite sua senha: ")
        if senha == senha1:
            break
        else:
            print("Senha inválida!\n")
    return senha

def main():
    mod_msg.msg_login_ini()
    usuario_validado = valida_usuario(USUARIO)
    senha_validada = valida_senha(SENHA)

    print("Sucesso! O usuário é:", usuario_validado)
    print("A senha é:", senha_validada)

    