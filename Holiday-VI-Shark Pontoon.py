def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
    if dolphin == True:
        sharkSpeed = sharkSpeed/2
        if sharkDistance/sharkSpeed > pontoonDistance/youSpeed:
            return "Alive!"
        else:
            return "Shark Bait!"
    else:
        if pontoonDistance/youSpeed < sharkDistance/sharkSpeed:
            return "Alive!"
        else:
            return "Shark Bait!"