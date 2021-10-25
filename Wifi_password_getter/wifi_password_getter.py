import subprocess

class WifiPasswordGetterLINUX:
    """
    A Script for Linux, that will find and display all the profiles of the
    wifis that you have connected to and then display the password if selected.
    """

    def __init__(self):
        profiles = self.get_wifi_profiles()
        choice = self.show_options(profiles)
        if choice == "exit":
            return
        password = self.display_password(profiles[choice - 1])
        strip_password = password.split("=", 1)[1]
        print("\nWifi Name: " + profiles[choice - 1] +
                   '\nPassword: ' + strip_password)

    def get_wifi_profiles(self):
        """
        Returns the names of the connected wifis.
        """
        out = subprocess.Popen(["ls",
                                "/etc/NetworkManager/system-connections/"],
                               universal_newlines=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
        (res, stderr) = out.communicate()
        data = res.split('\n')
        return data

    def show_options(self, arr):
        """
        Displays the names of the connected wifis and returns the number of the selected.
        Parameters
        ----------
        arr: list
            The list with the wifi names.
        """
        count = 1
        for x in range(len(arr) - 1):
            option = arr[x]
            print(str(count) + ": " + option)
            count = count + 1
        print(str(count) + ": Exit")
        choice = self.get_choice("Please select a number or Exit: ",
                                 count, count)
        if choice == -1:
            return "exit"
        else:
            return choice

    def get_choice(self, input_text, max_valid_value, terminator):
        """
        Returns the number of the selected wifi.
        Parameters
        ----------
        input_text: str
            The text to be printed when asking for input.
        max_valid_value: int
            The max valid value for the choices.
        terminator: int
            The value to terminate the procedure.
        """
        while True:
            try:
                inserted_value = int(input(input_text))
                if inserted_value == terminator:
                    return -1
                elif inserted_value <= max_valid_value:
                    return inserted_value
                else:
                    print(
                        "Invalid input! Enter a number from the"
                        "choices provided.")
            except ValueError:
                print(
                    "Invalid input! Enter a number from the choices provided.")
            print("")

    def display_password(self, ssid):
        """
        Returns the password of the selected wifi.
        Parameters
        ----------
        ssid: str
            The name of the selected wifi.
        """
        path = "/etc/NetworkManager/system-connections/"
        display = subprocess.Popen([f"sudo grep -r '^psk=' {path}{ssid}"],
                                   shell=True, universal_newlines=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        (new_res, stderr) = display.communicate()
        return new_res

WifiPasswordGetterLINUX()