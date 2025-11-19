import requests , os , psutil , sys , jwt , pickle , json , binascii , time , urllib3 , base64 , datetime , re , socket , threading , ssl , pytz , aiohttp
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import * ; from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import random
import asyncio

# Comprehensive patch for protobuf compatibility issues
import google.protobuf
from google.protobuf.internal import api_implementation

# Create a dummy runtime_version module if not present
if not hasattr(google.protobuf, 'runtime_version'):
    import types
    dummy_runtime_mod = types.ModuleType('runtime_version')
    def dummy_validate(*args, **kwargs):
        pass
    dummy_runtime_mod.ValidateProtobufRuntimeVersion = dummy_validate
    google.protobuf.runtime_version = dummy_runtime_mod

# Patch ValidateProtobufRuntimeVersion in the module
_runtime_version_mod = google.protobuf.runtime_version
if not hasattr(_runtime_version_mod, 'ValidateProtobufRuntimeVersion'):
    def dummy_validate(*args, **kwargs):
        pass
    _runtime_version_mod.ValidateProtobufRuntimeVersion = dummy_validate

# Also patch any direct references in google.protobuf
if not hasattr(google.protobuf, 'runtime_version'):
    google.protobuf.runtime_version = _runtime_version_mod

# Now import Pb2 after patch
from Pb2 import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2
from cfonts import render, say

#EMOTES BY PRIME CODEX ( JEXAR )

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

# VariabLes dyli 
#------------------------------------------#
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
#------------------------------------------#

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB50"}

# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)

async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload
    
async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200: return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.114.1"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
     
async def cHTypE(H):
    if not H: return 'Squid'
    elif H == 1: return 'CLan'
    elif H == 2: return 'PrivaTe'
    
async def SEndMsG(H , message , Uid , chat_id , key , iv):
    TypE = await cHTypE(H)
    if TypE == 'Squid': msg_packet = await xSEndMsgsQ(message , chat_id , key , iv)
    elif TypE == 'CLan': msg_packet = await xSEndMsg(message , 1 , chat_id , chat_id , key , iv)
    elif TypE == 'PrivaTe': msg_packet = await xSEndMsg(message , 2 , Uid , Uid , key , iv)
    return msg_packet

async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):
    if TypE == 'ChaT' and ChaT: whisper_writer.write(PacKeT) ; await whisper_writer.drain()
    elif TypE == 'OnLine': online_writer.write(PacKeT) ; await online_writer.drain()
    else: return 'UnsoPorTed TypE ! >> ErrrroR (:():)' 
           
async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer , spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , XX , uid , Spy,data2, Chat_Leave
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            while True:
                data2 = await reader.read(9999)
                if not data2: break
                
                if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                    try:
                        print(data2.hex()[10:])
                        packet = await DeCode_PackEt(data2.hex()[10:])
                        print(packet)
                        packet = json.loads(packet)
                        OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe , key,iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)


                        message = f'[B][C]{get_random_color()}\n- Welcome To Emote Bot ! \n\n{get_random_color()}- Commands : /help se dekho \n\n[00FF00]Dev : @GODJEXAR\n\nEmote kaise use karo: @a APNA_UID EMOTE_ID'
                        P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)

                    except Exception as e:
                        print(f"Error in squad join: {e}")
                        if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                            try:
                                print(data2.hex()[10:])
                                packet = await DeCode_PackEt(data2.hex()[10:])
                                print(packet)
                                packet = json.loads(packet)
                                OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                                JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)


                                message = f'[B][C]{get_random_color()}\n- Welcome To Emote Bot ! \n\n{get_random_color()}- Commands : /help se dekho \n\n[00FF00]Dev : @GODJEXAR\n\nEmote kaise use karo: @a APNA_UID EMOTE_ID'
                                P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                            except Exception as e2:
                                print(f"Second error: {e2}")
                                pass

            online_writer.close() ; await online_writer.wait_closed() ; online_writer = None

        except Exception as e: print(f"- ErroR With {ip}:{port} - {e}") ; online_writer = None
        await asyncio.sleep(reconnect_delay)
                            
async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(region, 'TCP CHAT')

    global spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , online_writer , chat_id , XX , uid , Spy,data2, Chat_Leave
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - TarGeT BoT in CLan ! ')
                print(f' - Clan Uid > {clan_id}')
                print(f' - BoT ConnEcTed WiTh CLan ChaT SuccEssFuLy ! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                    except Exception as e:
                        print(f"Decode error: {e}")
                        response = None


                    if response:
                        if inPuTMsG.startswith(("/5")):
                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                message = f"[B][C]{get_random_color()}\n\nAccept karo invite jaldi\n\n"
                                P = await SEndMsG(response.Data.chat_type , message , uid , chat_id , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                                PAc = await OpEnSq(key , iv,region)
                                await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                                C = await cHSq(5, uid ,key, iv,region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                                V = await SEnd_InV(5 , uid , key , iv,region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                                E = await ExiT(None , key , iv)
                                await asyncio.sleep(3)
                                await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                                # Professional reply
                                reply_msg = f"[B][C]{get_random_color()}\nInvite bhej diya successfully!\n"
                                reply_P = await SEndMsG(response.Data.chat_type , reply_msg , uid , chat_id , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , reply_P)
                            except Exception as e:
                                print(f"Error in /5: {e}")
                                print('msg in squad')



                        if inPuTMsG.startswith('/x/'):
                            CodE = inPuTMsG.split('/x/')[1]
                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                EM = await GenJoinSquadsPacket(CodE , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , EM)
                                # Professional reply
                                reply_msg = f"[B][C]{get_random_color()}\nSquad join karne ki koshish ki successfully!\n"
                                reply_P = await SEndMsG(response.Data.chat_type , reply_msg , uid , chat_id , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , reply_P)

                            except Exception as e:
                                print(f"Error in /x/: {e}")
                                print('msg in squad')

                        if inPuTMsG.startswith('leave'):
                            leave = await ExiT(uid,key,iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , leave)
                            # Professional reply
                            reply_msg = f"[B][C]{get_random_color()}\nLeave kar diya successfully!\n"
                            reply_P = await SEndMsG(response.Data.chat_type , reply_msg , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , reply_P)

                        if inPuTMsG.strip().startswith('/s'):
                            EM = await FS(key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , EM)
                            # Professional reply
                            reply_msg = f"[B][C]{get_random_color()}\nCommand /s chalaya successfully!\n"
                            reply_P = await SEndMsG(response.Data.chat_type , reply_msg , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , reply_P)

                        if inPuTMsG.strip().startswith('@a'):

                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                message = f"[B][C]{get_random_color()}\n\nSirf Squad mein kaam karta hai ye!\n\n"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                            except Exception as e:
                                print(f"Error in @a private: {e}")
                                print('msg in squad')

                                parts = inPuTMsG.strip().split()
                                print(response.Data.chat_type, uid, chat_id)
                                message = f'[B][C]{get_random_color()}\nActive Target -> {xMsGFixinG(uid)}\n'

                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)

                                uid2 = uid3 = uid4 = uid5 = None
                                s = False

                                try:
                                    uid = int(parts[1])
                                    uid2 = int(parts[2])
                                    uid3 = int(parts[3])
                                    uid4 = int(parts[4])
                                    uid5 = int(parts[5])
                                    idT = int(parts[5])

                                except ValueError as ve:
                                    print("ValueError:", ve)
                                    s = True

                                except Exception:
                                    idT = len(parts) - 1
                                    idT = int(parts[idT])
                                    print(idT)
                                    print(uid)

                                if not s:
                                    try:
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                                        H = await Emote_k(uid, idT, key, iv,region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)

                                        if uid2:
                                            H = await Emote_k(uid2, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid3:
                                            H = await Emote_k(uid3, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid4:
                                            H = await Emote_k(uid4, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid5:
                                            H = await Emote_k(uid5, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        
                                        # Professional reply
                                        reply_msg = f"[B][C]{get_random_color()}\nEmote bhej diya successfully!\n"
                                        reply_P = await SEndMsG(response.Data.chat_type , reply_msg , uid , chat_id , key , iv)
                                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , reply_P)

                                    except Exception as e:
                                        print(f"Error in emote sending: {e}")
                                        pass


                        if inPuTMsG in ("hi" , "hello" , "fen" , "salam"):
                            uid = response.Data.uid
                            chat_id = response.Data.Chat_ID
                            message = 'Hello main hu Dev AnixXH\nTelegram : @GODJEXAR'
                            P = await SEndMsG(response.Data.chat_type , message , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                            # Professional reply
                            reply_msg = f"[B][C]{get_random_color()}\nGreeting bhej diya successfully!\n"
                            reply_P = await SEndMsG(response.Data.chat_type , reply_msg , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , reply_P)

                        if inPuTMsG.startswith('/help'):
                            help_msg = f"[B][C]{get_random_color()}\n\nSaare Commands:\n\n/help - [ffffff]Ye command saare commands aur unke kaam batata hai\n\n@a UID1 UID2 ... EMOTE_ID - [ffffff]Squad mein emote bhejta hai (Sirf squad mein kaam karta hai)\n\n/like UID - [ffffff]Player ko like bhejta hai (Private ya team chat mein)\n\n/5 - [ffffff]Invite bhejta hai\n\n/x/ CODE - [ffffff]Squad code se join karta hai\n\nleave - [ffffff]Leave karta hai\n\n/s - [ffffff]Kuch special action\n\nhi/hello/fen/salam - [ffffff]Greeting bhejta hai\n\n[00FF00]Dev : @GODJEXAR\n"
                            help_P = await SEndMsG(response.Data.chat_type , help_msg , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , help_P)

                        if inPuTMsG.startswith('/like'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C]{get_random_color()}\n\nUID daalo sahi se! Jaise /like 123456789\n"
                                error_P = await SEndMsG(response.Data.chat_type , error_msg , uid , chat_id , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , error_P)
                                continue
                            target_uid = parts[1]
                            # Processing message
                            proc_msg = f"[B][C]{get_random_color()}\n\nLike process kar raha hu...\n"
                            proc_P = await SEndMsG(response.Data.chat_type , proc_msg , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , proc_P)
                            # Call API
                            api_url = f"https://anixh-like.vercel.app/like?server_name=ind&uid={target_uid}&key=ANIXH"
                            try:
                                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as session:
                                    async with session.get(api_url) as api_resp:
                                        print(f"API Status: {api_resp.status}")
                                        if api_resp.status == 200:
                                            api_data = await api_resp.json()
                                            print(f"API Data: {api_data}")
                                            if api_data.get('status') == 1:
                                                success_msg = f"[B][C]{get_random_color()}\nLike bhej diya successfully \n\nName : {api_data.get('PlayerNickname', 'N/A')}\nUID: {api_data.get('UID', target_uid)}\nRegion: ind\nBefore Like: {api_data.get('LikesbeforeCommand', 'N/A')}\nCurrent Like: {api_data.get('LikesafterCommand', 'N/A')}\nLikes Sent: {api_data.get('LikesGivenByAPI', 'N/A')}\n\nCredit : @GODJEXAR\n"
                                                success_P = await SEndMsG(response.Data.chat_type , success_msg , uid , chat_id , key , iv)
                                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , success_P)
                                            elif api_data.get('status') == 2:
                                                fail_msg = f"[B][C]{get_random_color()}\nLike nahi bheja gaya\n\nName: {api_data.get('PlayerNickname', 'N/A')}\nUID: {target_uid}\nRegion: ind\nLikes Now: {api_data.get('LikesNow', 'N/A')}\nMessage: {api_data.get('message', 'Max likes reached')}\n\nCredit : @GODJEXAR\n"
                                                fail_P = await SEndMsG(response.Data.chat_type , fail_msg , uid , chat_id , key , iv)
                                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , fail_P)
                                            else:
                                                error_msg = f"[B][C]{get_random_color()}\nUnknown response from API!\n"
                                                error_P = await SEndMsG(response.Data.chat_type , error_msg , uid , chat_id , key , iv)
                                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , error_P)
                                        else:
                                            error_msg = f"[B][C]{get_random_color()}\nAPI error: {api_resp.status}, try baad mein!\n"
                                            error_P = await SEndMsG(response.Data.chat_type , error_msg , uid , chat_id , key , iv)
                                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , error_P)
                            except Exception as api_e:
                                print(f"API Exception: {api_e}")
                                error_msg = f"[B][C]{get_random_color()}\nAPI call fail hua: {str(api_e)}\n"
                                error_P = await SEndMsG(response.Data.chat_type , error_msg , uid , chat_id , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , error_P)

                        response = None
                            
            whisper_writer.close() ; await whisper_writer.wait_closed() ; whisper_writer = None
                    
                    	
                    	
        except Exception as e: print(f"ErroR {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)

async def MaiiiinE():
    Uid , Pw = '4224399083','160A6B231BB6C605DA2C7783719E6266D9BDC9A4CDB56A0765EBE440241A909F'
    

    open_id , access_token = await GeNeRaTeAccEss(Uid , Pw)
    if not open_id or not access_token: print("ErroR - InvaLid AccounT") ; return None
    
    PyL = await EncRypTMajoRLoGin(open_id , access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE: print("TarGeT AccounT => BannEd / NoT ReGisTeReD ! ") ; return None
    
    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    UrL = MajoRLoGinauTh.url
    print(UrL)
    region = MajoRLoGinauTh.region

    ToKen = MajoRLoGinauTh.token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp
    
    LoGinDaTa = await GetLoginData(UrL , PyL , ToKen)
    if not LoGinDaTa: print("ErroR - GeTinG PorTs From LoGin DaTa !") ; return None
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    OnLineiP , OnLineporT = OnLinePorTs.split(":")
    ChaTiP , ChaTporT = ChaTPorTs.split(":")
    acc_name = LoGinDaTaUncRypTinG.AccountName
    #print(acc_name)
    print(ToKen)
    equie_emote(ToKen,UrL)
    AutHToKen = await xAuThSTarTuP(int(TarGeT) , ToKen , int(timestamp) , key , iv)
    ready_event = asyncio.Event()
    
    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT , AutHToKen , key , iv , LoGinDaTaUncRypTinG , ready_event ,region))
     
    await ready_event.wait()
    await asyncio.sleep(1)
    task2 = asyncio.create_task(TcPOnLine(OnLineiP , OnLineporT , key , iv , AutHToKen))
    os.system('clear')
    print(render('ANIXHH', colors=['white', 'green'], align='center'))
    print('')
    #print(' - ReGioN => {region}'.format(region))
    print(f" - BoT STarTinG And OnLine on TarGet : {TarGeT} | BOT NAME : {acc_name}\n")
    print(f" - BoT sTaTus > GooD | OnLinE ! (:")    
    await asyncio.gather(task1 , task2)
    
async def StarTinG():
    while True:
        try: await asyncio.wait_for(MaiiiinE() , timeout = 7 * 60 * 60)
        except asyncio.TimeoutError: print("Token ExpiRed ! , ResTartinG")
        except Exception as e: print(f"ErroR TcP - {e} => ResTarTinG ...")

if __name__ == '__main__':
    asyncio.run(StarTinG())