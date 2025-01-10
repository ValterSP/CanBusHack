import can
import time

# Set up the virtual CAN interface
bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

# Create the messages to send
turnLeftMsg = can.Message(arbitration_id=0x188, data=[0x01, 0x00, 0x00], is_extended_id=False)

turnRightMsg = can.Message(arbitration_id=0x188, data=[0x02, 0x00, 0x00], is_extended_id=False)

noTurnMsg = can.Message(arbitration_id=0x188, data=[0x00, 0x00, 0x00], is_extended_id=False)

accMsg = can.Message(arbitration_id=0x244, data=[0x00, 0x00, 0x00, 0x38, 0x94], is_extended_id=False)

openDoor4Msg =  can.Message(arbitration_id=0x19B,data=[0x00, 0x00, 0x07],is_extended_id=False)

openDoor3Msg =  can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x0B], is_extended_id=False)

openDoor2Msg =  can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x0D], is_extended_id=False)

openDoor1Msg =  can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x0E], is_extended_id=False)

closeAllDoorsMsg = can.Message( arbitration_id=0x19B, data=[0x00, 0x00, 0x0F], is_extended_id=False)

openAllDoorsMsg = can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x00], is_extended_id=False)

open12DoorMsg = can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x0C], is_extended_id=False)

open123DoorMsg = can.Message(arbitration_id=0x19B, data=[0x00, 0x00, 0x08], is_extended_id=False)

stopMsg = can.Message(arbitration_id=0x244, data=[0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)

def turn_message_bus(msg):
    num_msg = 0
    while num_msg < 10:
            bus.send(msg)
            time.sleep(0.1)
            bus.send(noTurnMsg)
            time.sleep(0.1)
            num_msg += 1

def open_close_door_bus(openDoor):
    num_msg = 0
    while num_msg < 10:
            bus.send(openDoor)
            time.sleep(0.2)
            bus.send(closeAllDoorsMsg)
            num_msg += 1
            time.sleep(0.1)


def increment_data(msg, increment_value=1):
    msg.data = [(byte + increment_value) % 256 for byte in msg.data]
    return msg

def accelerate_bus(accMsg):
    num_msg = 0
    while num_msg < 10:
        bus.send(accMsg)
        time.sleep(0.2)
        bus.send(stopMsg)
        time.sleep(0.2)
        num_msg += 1

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
