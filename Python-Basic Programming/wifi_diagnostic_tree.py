# This program leads a person through the steps of fixing a bad Wi-Fi connection
# Inform if you have Wi-fi connection problem
print("Are you having problem with your Wifi connection?")
Wifi_Connection = str(input(""))
if ((Wifi_Connection != 'Yes') and (Wifi_Connection != 'No')
        and (Wifi_Connection != 'no') and (Wifi_Connection != 'yes')):
    print("Error: We can't identify your problem if you don't type in either Yes or No. "
          "Please proceed and try again")
else:
    if (Wifi_Connection == 'No') or (Wifi_Connection == 'no'):
        print("There is no problem with your Wifi connection right now")
    else:
        # If the user types "No", leads a person to fix the Wi-fi problem
        if (Wifi_Connection == 'Yes') or (Wifi_Connection == 'yes'):
            print("Reboot the router and try to connect")
            print("Did that fix the problem?")
            Wifi_Connection = str(input(""))
            if ((Wifi_Connection != 'Yes') and (Wifi_Connection != 'No')
                    and (Wifi_Connection != 'no') and (Wifi_Connection != 'yes')):
                print("Error: We can't identify your problem if you don't type in either Yes or No. "
                      "Please proceed and try again")
            else:
                if (Wifi_Connection == 'Yes') or (Wifi_Connection == 'yes'):
                    print("You are good to go!")
                # Notice the program ends as soon as a solution is found to the problem
                elif (Wifi_Connection == 'No') or (Wifi_Connection == 'no'):
                    print("Make sure the cables between the router and modem are plugged in firmly")
                    print("Did that fix the problem?")
                    Wifi_Connection = str(input(""))
                    if ((Wifi_Connection != 'Yes') and (Wifi_Connection != 'No')
                            and (Wifi_Connection != 'no') and (Wifi_Connection != 'yes')):
                        print("Error: We can't identify your problem if you don't type in either Yes or No. "
                              "Please proceed and try again")
                    else:
                        if (Wifi_Connection == 'Yes') or (Wifi_Connection == 'yes'):
                            print("Good! Everything is fine now")
                        elif (Wifi_Connection == 'No') or (Wifi_Connection == 'no'):
                            print("Move a router to a new location and try to connect")
                            print("Did that fix the problem?")
                            Wifi_Connection = str(input(""))
                            if ((Wifi_Connection != 'Yes') and (Wifi_Connection != 'No')
                                    and (Wifi_Connection != 'no') and (Wifi_Connection != 'yes')):
                                print("Error: We can't identify your problem if you don't type in either Yes or No. "
                                      "Please proceed and try again")
                            else:
                                if (Wifi_Connection == 'Yes') or (Wifi_Connection == 'yes'):
                                    print("Finally! Problem solved")
                                elif (Wifi_Connection == 'No') or (Wifi_Connection == 'no'):
                                    print("Get a new router")
                # The program will eventually stop at the point when the user types 'Yes'




