import mod_inputs

def msg_login():
    print("#################################")
    print("<<<<<<<< LOGIN DO SISTEMA >>>>>>>")
    print("#################################\n")

def recebe_usuario():
    usuario = mod_inputs.inp_str("Digite seu usuário de acesso: ")
    return usuario

def recebe_senha():
    senha = mod_inputs.inp_str("Digite sua senha de acesso: ")
    return senha

def valida_usuario(usuario, senha):
    cad_usuario = "jansen"
    cad_senha = "123"

    if cad_usuario == usuario and cad_senha == senha:
        acesso = False
    else:
        print("Usuário ou senha incorretos... Por favor, tente novamente!")
        acesso = True
    return acesso

def main():
    msg_login()
    autentica = True
    while autentica:
        usuario = recebe_usuario()
        senha = recebe_senha()
        autentica = valida_usuario(usuario, senha)

if __name__ == "__main__":
    main()

