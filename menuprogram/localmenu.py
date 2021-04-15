import os
while True:
    print()
    print("press 1 for docker related process")
    print("enter EXIT for end this program")
    print()
    x=(input("Enter your choice:"))
    print()
    if x=="1":
        while True:
            print()
            print("press 1 for check available images")
            print("press 2 for launch container")
            print("press 3 for removing all container in single time")
            print("press 4 for checking all the running and stopped container")
            print("press 5 for remove specific container")
            print("enter EXIT for end docker related process")
            print()
            ch=(input("Enter your choice: "))
            if ch=="1":
                os.system("docker images")
            elif ch=="2":
                print("Container will launched in detached mode")
                print()
                cname=input("enter container name: ")
                iname=input("enter image name: ")
                ver=input("enter your image version: ")
                os.system("docker run -dit --name {0} {1}:{2}".format(cname,iname,ver))
            elif ch=="3":
                os.system("docker rm -f $(docker ps -a -q)")
            elif ch=="4":
                os.system("docker ps -a")
            elif ch=="5":
                print("available container are")
                os.system("docker ps -a")
                cid=input("Enter container id: ")
                os.system("docker rm -f {0}".format(cid))
            else:
                print()
                print("docker process EXITED successfully")
                break
    else:
        print("Program successfully closed")
        break
