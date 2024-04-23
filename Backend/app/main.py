import uvicorn
from fastapi import FastAPI
from gpiozero import Buzzer
from time import sleep
from fastapi.middleware.cors import CORSMiddleware
from wakeonlan import send_magic_packet
import os

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/wakeuppc1")
async def WakeUPPC1():
    send_magic_packet('00.23.24.EA.0C.73')
    return "Wake on LAN Magic packet sent.."

@app.get("/getcputemp")
async def GetCPUTemp():
    return os.popen("vcgencmd measure_temp").read().split("=")[1].split("\n")[0]

@app.get("/playbuzzer")
async def PingBuzzer():
   buzzer = Buzzer(17)
   buzzer.on()
   sleep(0.2)
   buzzer.off()
   sleep(0.1)
   buzzer.on()
   sleep(0.2)
   buzzer.off()
   sleep(0.1)
   buzzer.on()
   sleep(0.2)
   buzzer.off()
   sleep(1)
   return "Playing Buzzer on RaspberryPiHome"
if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
