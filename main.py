import json
import ast
import time

# my_ip = '192.168.58.218'
# ip255 = "192.168.58.255"

my_ip = '192.168.29.244'
ip255 = "192.168.29.255"

resend_times = 5
switch_delay = 1


# delay between two consequtive commands
command_delay = 1
wait_time = 2
r111 = '{"cmd":"UPD","slave":"2021112013001604","token":"217c6523ca92adaecc0d","node":1,"val":"A","d_val":255}'
r121 = '{"cmd":"UPD","slave":"2021112013001604","token":"217c6523ca92adaecc0d","node":2,"val":"A","d_val":255}'
r131 = '{"cmd":"UPD","slave":"2021112013001604","token":"217c6523ca92adaecc0d","node":3,"val":"A","d_val":255}'
r141 = '{"cmd":"UPD","slave":"2021112013001604","token":"217c6523ca92adaecc0d","node":4,"val":"A","d_val":255}'

r110 = '{"cmd":"UPD","slave":"2021112013001604","token":"217c6523ca92adaecc0d","node":1,"val":"0","d_val":255}'
r120 = '{"cmd":"UPD","slave":"2021112013001604","token":"217c6523ca92adaecc0d","node":2,"val":"0","d_val":255}'
r130 = '{"cmd":"UPD","slave":"2021112013001604","token":"217c6523ca92adaecc0d","node":3,"val":"0","d_val":255}'
r140 = '{"cmd":"UPD","slave":"2021112013001604","token":"217c6523ca92adaecc0d","node":4,"val":"0","d_val":255}'

r211 = '{"cmd":"UPD","slave":"4000230121104145","token":"00decab5a18d785a4631","node":1,"val":"A","d_val":255}'
r221 = '{"cmd":"UPD","slave":"4000230121104145","token":"00decab5a18d785a4631","node":2,"val":"A","d_val":255}'
r231 = '{"cmd":"UPD","slave":"4000230121104145","token":"00decab5a18d785a4631","node":3,"val":"A","d_val":255}'
r241 = '{"cmd":"UPD","slave":"4000230121104145","token":"00decab5a18d785a4631","node":4,"val":"A","d_val":255}'

r210 = '{"cmd":"UPD","slave":"4000230121104145","token":"00decab5a18d785a4631","node":1,"val":"0","d_val":255}'
r220 = '{"cmd":"UPD","slave":"4000230121104145","token":"00decab5a18d785a4631","node":2,"val":"0","d_val":255}'
r230 = '{"cmd":"UPD","slave":"4000230121104145","token":"00decab5a18d785a4631","node":3,"val":"0","d_val":255}'
r240 = '{"cmd":"UPD","slave":"4000230121104145","token":"00decab5a18d785a4631","node":4,"val":"0","d_val":255}'

r311 = '{"cmd":"UPD","slave":"4111220819170326","token":"119d8974604c37230ffa","node":1,"val":"A","d_val":255}'
r321 = '{"cmd":"UPD","slave":"4111220819170326","token":"119d8974604c37230ffa","node":2,"val":"A","d_val":255}'
r331 = '{"cmd":"UPD","slave":"4111220819170326","token":"119d8974604c37230ffa","node":3,"val":"A","d_val":255}'
r341 = '{"cmd":"UPD","slave":"4111220819170326","token":"119d8974604c37230ffa","node":4,"val":"A","d_val":255}'

r310 = '{"cmd":"UPD","slave":"4111220819170326","token":"119d8974604c37230ffa","node":1,"val":"0","d_val":255}'
r320 = '{"cmd":"UPD","slave":"4111220819170326","token":"119d8974604c37230ffa","node":2,"val":"0","d_val":255}'
r330 = '{"cmd":"UPD","slave":"4111220819170326","token":"119d8974604c37230ffa","node":3,"val":"0","d_val":255}'
r340 = '{"cmd":"UPD","slave":"4111220819170326","token":"119d8974604c37230ffa","node":4,"val":"0","d_val":255}'

r411 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":1,"val":"A","d_val":255}'
r421 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":2,"val":"A","d_val":255}'
r431 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":3,"val":"A","d_val":255}'
r441 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":4,"val":"A","d_val":255}'
r451 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":5,"val":"A","d_val":255}'
r461 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":6,"val":"A","d_val":255}'
r471 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":7,"val":"A","d_val":255}'
r481 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":8,"val":"A","d_val":255}'

r410 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":1,"val":"0","d_val":255}'
r420 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":2,"val":"0","d_val":255}'
r430 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":3,"val":"0","d_val":255}'
r440 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":4,"val":"0","d_val":255}'
r450 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":5,"val":"0","d_val":255}'
r460 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":6,"val":"0","d_val":255}'
r470 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":7,"val":"0","d_val":255}'
r480 = '{"cmd":"UPD","slave":"2019033010163908","token":"14118c776f296300cccd","node":8,"val":"0","d_val":255}'

ip1 = "192.168.29.29"
ip2 = "192.168.29.237"
ip3 = "192.168.29.174"
ip4 = "192.168.29.27"


command_list = [r141]
ip_list = [ip255]

command_counter = len(command_list)
# #REGULARINPUT END
received_cmd_list_json = []


def terachadupd(sts, device_ip, recursion_count=0):
    if recursion_count == resend_times:
        return
    import socket

    from datetime import datetime

    now = datetime.now()
    sts_json = ast.literal_eval(sts)
    PORT = 13001

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((my_ip, 13000))

    udp_socket.settimeout(wait_time)

    # encode the message as bytes
    message = sts
    message_bytes = message.encode()

    # send the message to the server
    udp_socket.sendto(message_bytes, (device_ip, PORT))

    current_time_sent = now.time()
    print("Sent message:    ", 'Time', current_time_sent, " ", sts)

    while True:
        try:
            # wait for a response from the server

            message, address = udp_socket.recvfrom(4096)

            # decode the response
            message_string = message.decode()
            message_string_json = json.loads(message_string)

            while str(sts_json["slave"]) != str(message_string_json["slave"]):
                # wait for a response from the server
                message, address = udp_socket.recvfrom(4096)

                # decode the response
                message_string = message.decode()
                message_string_json = json.loads(message_string)

            # print the response
            now1 = datetime.now()
            current_time_received = now1.time()
            print("Received message:", 'Time', current_time_received, " ", message_string)
            print("From address:    ", address)
            udp_socket.close()
            break

        except socket.timeout:
            # if the socket times out, increment the number of attempts and send another UDP request

            print("Socket timed out. Retrying...")
            udp_socket.close()
            terachadupd(sts, device_ip, recursion_count + 1)

            print("Socket timed out too many times. Moving to next Command if there are any....")
            break

        except Exception as e:
            print(e)
            break


def terachadmst2(sts, device_ip, recursion_count=0):
    local_list = []
    if recursion_count == resend_times:
        return
    import socket
    import json
    from datetime import datetime

    now = datetime.now()
    PORT = 13001
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((my_ip, 13000))
    udp_socket.settimeout(wait_time)
    message = sts
    message_bytes = message.encode()
    udp_socket.sendto(message_bytes, (device_ip, PORT))
    current_time_sent = now.time()
    print("Sent message:    ", 'Time', current_time_sent, " ", sts)

    while True:
        try:
            while 1:

                message, address = udp_socket.recvfrom(4096)
                message_string = message.decode()
                message_string_json = json.loads(message_string)

                if str(message_string_json["cmd"]) == "MST":
                    local_list.append(message_string)
                    now1 = datetime.now()
                    current_time_received = now1.time()
                    print("Received message:", 'Time', current_time_received, " ", message_string)
                    print("From address:    ", address)


        except Exception as e:
            print(e)
            if e == "timed out":
                if local_list == []:
                    print("Socket timed out. Retrying...")
                    udp_socket.close()
                    terachadmst2(sts, device_ip, recursion_count + 1)
                    print("Socket timed out too many times. Moving to next Command if there are any....")
            return local_list


# def terachad(sts, device_ip):
#     local_list = []
#     import socket
#     import json
#     from datetime import datetime
#
#     now = datetime.now()
#     sts_json = json.loads(sts)
#     PORT = 13001
#
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     udp_socket.bind((my_ip, 13000))
#
#     udp_socket.settimeout(wait_time)
#
#     # encode the message as bytes
#     message = sts
#     message_bytes = message.encode()
#
#     # send the message to the server
#     udp_socket.sendto(message_bytes, (device_ip, PORT))
#
#     current_time_sent = now.time()
#     print("Sent message:    ", 'Time', current_time_sent, " ", sts)
#
#     while True:
#         try:
#
#             message, address = udp_socket.recvfrom(4096)
#             message_string = message.decode()
#             message_string_json = json.loads(message_string)
#             local_list.append(message_string_json)
#
#             while 1:
#
#                 # wait for a response from the server
#                 message, address = udp_socket.recvfrom(4096)
#
#                 # decode the response
#                 message_string = message.decode()
#                 message_string_json = json.loads(message_string)
#                 if message_string_json["cmd"] != "MST":
#                     continue
#                 local_list.append(message_string_json)
#
#                 # print the response
#                 now1 = datetime.now()
#                 current_time_received = now1.time()
#
#                 # printing Dictionaries
#                 # assert isinstance(sts_json, object)
#                 # print("dict send:       ", sts_json)
#                 # print("dict received:   ", message_string_json)
#
#                 # printing Received message along with receiver's details (IP Address and Port Number)
#                 print("Received message:", 'Time', current_time_received, " ", message_string)
#                 print("From address:    ", address)
#
#             udp_socket.close()
#             break
#         except Exception as e:
#             print(e)
#             print(local_list)
#             udp_socket.close()
#             return local_list


def terachadlin2(sts, device_ip, recursion_count=0):
    if recursion_count == resend_times:
        return
    import socket
    import json
    from datetime import datetime

    now = datetime.now()

    PORT = 13001

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((my_ip, 13000))

    udp_socket.settimeout(wait_time)

    # encode the message as bytes
    message = sts
    message_bytes = message.encode()

    # send the message to the server
    udp_socket.sendto(message_bytes, (device_ip, PORT))

    current_time_sent = now.time()
    print("Sent message:    ", 'Time', current_time_sent, " ", sts)

    while True:
        try:
            # wait for a response from the server
            message, address = udp_socket.recvfrom(4096)

            # decode the response
            message_string = message.decode()
            message_string_json = json.loads(message_string)

            while str(message_string_json["cmd"]) != "LIN":
                # wait for a response from the server
                message, address = udp_socket.recvfrom(4096)

                # decode the response
                message_string = message.decode()
                message_string_json = json.loads(message_string)

            # print the response
            now1 = datetime.now()
            current_time_received = now1.time()

            # printing Dictionaries
            # assert isinstance(sts_json, object)
            # print("dict send:       ", sts_json)
            # print("dict received:   ", message_string_json)

            # printing Received message along with receiver's details (IP Address and Port Number)
            print("Received message:", 'Time', current_time_received, " ", message_string)
            print("From address:    ", address)

            udp_socket.close()

            return message_string


        except socket.timeout:
            # if the socket times out, increment the number of attempts and send another UDP request            print("Socket timed out. Retrying...")

            print("Socket timed out. Retrying...")
            udp_socket.close()
            terachadlin2(sts, device_ip, recursion_count + 1)

            print("Socket timed out too many times. Moving to next Command if there are any....")
            break

        except Exception as e:
            print(e)
            break


print(f"{command_counter} commands recorded and Program is STARTING...")

mst = '{"cmd":"MST"}'
lin = '{"cmd":"LIN", "user":"Admin", "pin":"1234", "device_id":97251414}'

mst_local_list = terachadmst2(mst, ip255)
print("MST LOCAL LIST: ",mst_local_list)
print(len(mst_local_list) ," ELEMENTS"
                           "")
m_name =  input("Enter the m_name: ")

for i in range(len(mst_local_list)):
    if m_name == ast.literal_eval(mst_local_list[i])["m_name"]:
        required_mst_feedback_string =  mst_local_list[i]

print(required_mst_feedback_string)

# Remember to unhash the following
lin_json = ast.literal_eval(lin)
# dev = ast.literal_eval(mst_local_list[0])['device_id']
lin_json["device_id"] = ast.literal_eval(required_mst_feedback_string)['device_id']
lin = str(lin_json)

print("LIN sent")

lin_received_msg = str(terachadlin2(lin, ip255))

print("LIN STR", lin_received_msg)

lin_received_msg_json = ast.literal_eval(lin_received_msg)

print("LIN JSON ", lin_received_msg_json)

print('- ' * 100)




upd = '{"cmd":"UPD","slave":"6211221004161946","token":"119a85715d48433f3b27","node":1,"val":"A","d_val":255}'
upd_json = json.loads(upd)
upd_json["slave"] = lin_received_msg_json["slave"]
upd_json["token"] = lin_received_msg_json["token"]
upd_json["val"] = "0"

if lin_received_msg_json["hw_ver"] == "2.2.0":
    nodes = 2
elif lin_received_msg_json["hw_ver"] == "8.2.0":
    nodes = 6
elif lin_received_msg_json["hw_ver"] == "4.2.0" or lin_received_msg_json["hw_ver"] == "4.1.2":
    nodes = 4
else:
    print("Hardware version not supported"
          "But still trying assuming your device has 2 Nodes")
    nodes = 2

for i in range(nodes):
    upd_json["node"] = int(i + 1)
    upd = str(upd_json)
    terachadupd(upd, ip255)
    time.sleep(float(switch_delay))

upd_json["val"] = "A"
time.sleep(float(1))

for i in range(nodes):
    upd_json["node"] = int(i + 1)
    upd = str(upd_json)
    terachadupd(upd, ip255)
    time.sleep(float(switch_delay))

# upd_json["val"] = "0"
# time.sleep(float(1))
#
# for i in range(nodes):
#     upd_json["node"] = int(i + 1)
#     upd = str(upd_json)
#     terachadupd(upd, ip255)
#     time.sleep(float(switch_delay))

print("UPD successfully deployed...")
