import can
import time

# Cria o bus onde serão enviados os comandos
bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

#Codigo enviado com o id 0x188 com os bytes 0x01, 0x00, 0x00 que faz o pisca para a esquerda
turnLeftMsg = can.Message(arbitration_id=0x188, data=[0x01, 0x00, 0x00], is_extended_id=False)

#Dados enviados com o id 0x188 com os bytes 0x02, 0x00, 0x00 que faz o pisca para a direita
turnRightMsg = can.Message(arbitration_id=0x188, data=[0x02, 0x00, 0x00], is_extended_id=False)
#Dados enviados com o id 0x188 com os bytes 0x00, 0x00, 0x00 para desligar os piscas
noTurnMsg = can.Message(arbitration_id=0x188, data=[0x00, 0x00, 0x00], is_extended_id=False)
#Dados enviados com o id 0x244 onde os ultimos 2 bytes representam a velocidade no velocimetro
accMsg = can.Message(arbitration_id=0x244, data=[0x00, 0x00, 0x00, 0x38, 0x94], is_extended_id=False)
#Dados enviados com o id 0x198 para abrir a porta direita de trás e as outras fechadas
openDoor4Msg =  can.Message(arbitration_id=0x19B,data=[0x00, 0x00, 0x07],is_extended_id=False)
#Dados enviados com o id 0x198 para abrir a porta esquerda de trás e as outras fechadas
openDoor3Msg =  can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x0B], is_extended_id=False)
#Dados enviados com o id 0x198 para abrir a porta direita da frente e as outras fechadas
openDoor2Msg =  can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x0D], is_extended_id=False)
#Dados enviados com o id 0x198 para abrir a porta esquerda da frente e as outras fechadas
openDoor1Msg =  can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x0E], is_extended_id=False)
#Dados enviados com o id 0x198 para trancar todas as portas
closeAllDoorsMsg = can.Message( arbitration_id=0x19B, data=[0x00, 0x00, 0x0F], is_extended_id=False)
#Dados enviados com o id 0x198 para abrir todas as portas
openAllDoorsMsg = can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x00], is_extended_id=False)
#Dados enviados com o id 0x198 para abrir as duas portas da frente
open12DoorMsg = can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x0C], is_extended_id=False)
#Dados enviados com o id 0x198 para abrir as duas portas da frente e a esquerda de trás
open123DoorMsg = can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x08], is_extended_id=False)
#Dados enviados com o id 0x244 para colocar a velocidade do velocimetro a 0
stopMsg = can.Message(arbitration_id=0x244, data=[0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)

#enviar mensagem no CAN bus para ligar o pisca
def turn_message_bus(msg):
    num_msg = 0
    while num_msg < 10:
            bus.send(msg)
            time.sleep(0.1)
            bus.send(noTurnMsg)
            time.sleep(0.1)
            num_msg += 1

#enviar mensagem no CAN bus para abrir e fechar as portas
def open_close_door_bus(openDoor):
    num_msg = 0
    while num_msg < 10:
            bus.send(openDoor)
            time.sleep(0.2)
            bus.send(closeAllDoorsMsg)
            num_msg += 1
            time.sleep(0.1)

#enviar mensagem no CAN bus para aumentar velocidade
def accelerate_bus(accMsg):
    num_msg = 0
    while num_msg < 10:
        bus.send(accMsg)
        time.sleep(0.2)
        bus.send(stopMsg)
        time.sleep(0.2)
        num_msg += 1

#enviar várias mensagens para o CAN bus com várias instruções
def crazy_mode_bus():
    num_msg = 0
    while num_msg < 10:
        bus.send(openDoor1Msg)
        time.sleep(0.05)
        bus.send(open12DoorMsg)
        time.sleep(0.05)
        bus.send(open123DoorMsg)
        time.sleep(0.05)
        bus.send(openAllDoorsMsg)
        time.sleep(0.05)
        bus.send(open123DoorMsg)
        time.sleep(0.05)
        bus.send(open12DoorMsg)
        time.sleep(0.05)
        bus.send(openDoor1Msg)
        time.sleep(0.05)
        bus.send(stopMsg)
        time.sleep(0.05)
        bus.send(openAllDoorsMsg)
        time.sleep(0.05)
        bus.send(turnLeftMsg)
        time.sleep(0.05)
        bus.send(turnRightMsg)
        time.sleep(0.05)
        bus.send(accMsg)

        time.sleep(0.1)

        num_msg += 1
    bus.send(closeAllDoorsMsg)
    bus.send(stopMsg)
    bus.send(noTurnMsg)
    


def menu():

    while True:
        print("\nVehicle Control Menu")
        print("1. Turn Left")
        print("2. Turn Right")
        print("3. Accelerate")
        print("4. Open and Close Door 1")
        print("5. Open and Close Door 2")
        print("6. Open and Close Door 3")
        print("7. Open and Close Door 4")
        print("8. Send Random Commands")
        print("0. Stop")
        choice = input("\nEnter your choice (0-8): ")

        if choice == "1":
            turn_message_bus(turnLeftMsg)
        elif choice == "2":
            turn_message_bus(turnRightMsg)
        elif choice == "3":
            accelerate_bus(accMsg)
        elif choice == "4":
            open_close_door_bus(openDoor1Msg)
        elif choice == "5":
            open_close_door_bus(openDoor2Msg)
        elif choice == "6":
            open_close_door_bus(openDoor3Msg)
        elif choice == "7":
            open_close_door_bus(openDoor4Msg)
        elif choice == "8":
            crazy_mode_bus()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    menu()
