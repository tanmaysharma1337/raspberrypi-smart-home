function PlayBuzzer()
{
    fetch("http://192.168.1.69:8000/playbuzzer",{
        headers : {
            "Access-Control-Request-Private-Network": true
        }
    })
}

function WakeUpPC1()
{
    fetch("http://192.168.1.69:8000/wakeuppc1",{
        headers : {
            "Access-Control-Request-Private-Network": true
        }
    })
}

function NotificationBarContent()
{
    fetch("http://192.168.1.69:8000/getcputemp",{
        headers : {
            "Access-Control-Request-Private-Network": true
        }
    }).then((response) => response.json()).then((json)=>{
        document.getElementById("notibar").innerHTML =`
        Hardware Temprature - `+ json
        
    })
}
NotificationBarContent()