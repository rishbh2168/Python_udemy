device_status = "active"
temperature = 38

if device_status == "active":
    if temperature >35:
        print("Warn: high temp")
    else:
        print("temp is normal")
else:
    print("device is offline")