from subprocess import getstatusoutput
import shutil, os

current_startup_binary_folder = f"{os.getcwd()}\\message"
destination_startup_binary_folder = ""
os_installation_path = os.getenv("SystemDrive")
print(f"OS Installation drive is {os_installation_path}")

def copy_startup_task_binary_folder():
    """
    This function should copy the folder containing the binary of the startup window that shows the new user that their access to this PC is restricted.

    this function takes no arguments.
    """
    global current_startup_binary_folder, destination_startup_binary_folder
    try:
        os.mkdir(destination_startup_binary_folder)
    except Exception as exception_makingdir:
        print(exception_makingdir)
        raise SystemExit(10) # unable to copy startup task binary files.

    try:
        shutil.copytree(current_startup_binary_folder, destination_startup_binary_folder, dirs_exist_ok=True)
    except Exception as exception_copying_data:
        print(exception_copying_data)
        raise SystemExit(10) # unable to copy startup task binary files.
    

    return None

def LogOutMainUser():
    """
    Logs out the main user (closes the current session) to prevent unauthorized access from unauthorized users.
    """
    console_output = getstatusoutput("shutdown /l")
    output = str(console_output[1])
    exit_code = int(console_output[0])
    print(output + "\nprocess exited with error code :" + str(exit_code))
    return None

def restrict_volume_access(volume_letter):
    pass



def CreateTemporaryUser(username):
    """
    Create a Temporary User for Temporary Access to the computer.

    username must be a string.
    """
    global current_startup_binary_folder, destination_startup_binary_folder, os_installation_path
    temp_username = str(username)
    destination_startup_binary_folder = f"{os_installation_path}\\Users\\Public\\message"
    console_output = getstatusoutput(f'net user /add "{temp_username}"')
    output = str(console_output[1])
    exit_code = int(console_output[0])
    print(output + "\nprocess exited with error code :" + str(exit_code))
    # after user is created, let's make sure it has no password assigned to it.
    console_output = getstatusoutput(f'net user "{temp_username}" /PASSWORDREQ:NO')
    output = str(console_output[1])
    exit_code = int(console_output[0])
    print(output + "\nprocess exited with error code :" + str(exit_code))
    # making sure the user expires after never.
    console_output = getstatusoutput(f'net user "{temp_username}" /EXPIRES:NEVER')
    output = str(console_output[1])
    exit_code = int(console_output[0])
    print(output + "\nprocess exited with error code :" + str(exit_code))
    # adding a comment indicating that this user has been created by StrangerOnMyPC.
    console_output = getstatusoutput(f'net user "{temp_username}" /COMMENT:"User created by the tool StrangerOnMyPC by Insertx2k Dev (Mr.X)"')
    output = str(console_output[1])
    exit_code = int(console_output[0])
    print(output + "\nprocess exited with error code :" + str(exit_code))
    # making sure the user is not able to change their password.
    console_output = getstatusoutput(f'net user "{temp_username}" /PASSWORDCHG:NO')
    output = str(console_output[1])
    exit_code = int(console_output[0])
    print(output + "\nprocess exited with error code :" + str(exit_code))
    # changing the user's official public name.
    console_output = getstatusoutput(f'net user "{temp_username}" /FULLNAME:"Guest on This PC"')
    output = str(console_output[1])
    exit_code = int(console_output[0])
    print(output + "\nprocess exited with error code :" + str(exit_code))
    # adding the newely created user to the Users group.
    console_output = getstatusoutput(f'NET LOCALGROUP /ADD Users {temp_username}')
    output = str(console_output[1])
    exit_code = int(console_output[0])
    print(output + "\nprocess exited with error code :" + str(exit_code))
    # making sure the newely created user is not on the Administrators group.
    console_output = getstatusoutput(f'NET LOCALGROUP /DELETE Administrators {temp_username}')
    output = str(console_output[1])
    exit_code = int(console_output[0])
    print(output + "\nprocess exited with error code :" + str(exit_code))
    # now let's create a startup task for the window that shows up that the user is in a restricted profile.
    copy_startup_task_binary_folder()

    return None


class TemporaryUser:
    def __init__(self, username):
        self.username = str(username)
        return None
    
    def delete(self):
        """
        Deletes the temporary user profile (alongwith it's home files).
        """
        console_output = getstatusoutput(f'net user /delete {self.username}')
        output = str(console_output[1])
        exit_code = int(console_output[0])
        print(output + "\nprocess exited with error code :" + str(exit_code))
        # now let's delete it's files.
        console_output = getstatusoutput(f'RMDIR /S /Q "%systemdrive%\\Users\\{self.username}"')
        output = str(console_output[1])
        exit_code = int(console_output[0])
        print(output + "\nprocess exited with error code :" + str(exit_code))
        return None
    
    def rename(self, new_name):
        """
        Changes the publicly visible name of the user.
        """
        self.new_name = str(new_name)
        print("WARNING: THE NEW NAME MUST NOT CONTAIN ANY SORT OF SPACES TO AVOID ERRORS.")
        # making sure the new name has no spaces in it.
        if ' ' in self.new_name:
            print("ERROR: YOU CAN'T USE SPACES IN USER NAMES.")
            return 5
        else: # new name has no spaces in it.
            console_output = getstatusoutput(f'net user {self.username} /FULLNAME:"{self.new_name}"')
            output = str(console_output[1])
            exit_code = int(console_output[0])
        print(output + "\nprocess exited with error code :" + str(exit_code))
    
    def change_description(self, new_description):
        pass








    
    



if __name__ == '__main__':
    CreateTemporaryUser(12)
    # user = TemporaryUser(12)
    # user.delete()
    raise SystemExit(0)