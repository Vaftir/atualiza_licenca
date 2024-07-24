from controller.controller import Controller
if __name__ == "__main__":
    controller = Controller()
    if controller.run():
        print("Processo finalizado com sucesso")
    else:
        print("Erro ao executar o processo")