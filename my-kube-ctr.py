#!/usr/local/bin/python3
# Define the actions for each arg1 we want to offer.

import os, sys
import json

#.................
def startMinikube():
  print("\Starting...\n"+argcmd)
  os.system('minikube start')


def encryptAndConvertToBase64():
  print("\Enter your SID or FID to setup kaniko and docker secrets on the given kube namespace:")
  argcreds = input()
  while argcreds != '-q':
    if argcreds != '':
      print("\Options given\n"+argcmd)
      os.system('ls *.py')

def getKubeResource(argcmd):
  print("\Options given\n"+argcmd)
  os.system('kubectl get'+' '+argcmd)

def createKubeNamespace(argnsp):
  print("\Options given\n"+argnsp)
  os.system('kubectl create namespace'+' '+argnsp)
  encryptAndConvertToBase64()

def createKubeSecrets(argscts):
  print("\Options given\n"+argscts)
  encryptAndConvertToBase64()

def deleteKubeNamespace(argnsp):
  print("\Options given\n"+argnsp)
  os.system('kubectl delete namespace'+' '+argnsp)

#...............

def getResources(cmds):
  for cmd in [cmds]:
    print(cmd)
    getKubeResource(cmd)

def setupKubeSpace(nsps):
  for nsp in [nsps]:
    print(nsp)
    createKubeNamespace(nsp)

def setupKubeSecrets(scts):
  for sct in [scts]:
    print(sct)
    createKubeSecrets(sct)

def cleanupKubeSpace(nsps):
  for nsp in [nsps]:
    print(nsp)
    deleteKubeNamespace(nsp)

#...............
# Set an initial value for arg1 other than the value for 'quit'.
arg1 = ''


minicmd = "minikube status -o json "
returned_value = os.system(minicmd)  # returns the code 0 if minikube running

if returned_value != 0:
  os.system('minikube start')
else:
  print("\nMinikube instance is running\n")


# Start a loop that runs until the user enters the value for 'quit'.
while arg1 != 'q':
  # Give all the arg1s in a series of print statements.
  print("\n[get] Enter get to get kube resources.")
  print("[setup] Enter setup to setup kube resources.")
  print("[deploy] Enter deploy to deploy your container image on local minikube platform.")
  print("[redeploy] Enter redeploy to re-deploy your conainter images on local minikube platform.")
  print("[q] Enter q to quit.")

    # Ask for the user's arg1.
  arg1  = input("\nWhat would you like to do? ")

#...............
        # Respond to the user's arg1.
  if arg1 == 'get':
    arg2  = input("\nEnter the resource name like pods, services and so on? ")
    if arg2 != "":
      getResources(arg2)
  elif arg1 == 'setup':
    print("Enter Namesapce all, ns, sts.")
    myoption = input()
    if myoption == 'all':
      setupKubeSpace(myoption)
    else:
      print("No valid input")
  elif arg1 == 'deploy':
    climb_mountin()
  elif arg1 == 'redeploy':
    climb_mountin()
  elif arg1 == '':
    print("\nThanks for using the script. See you later.\n")
  else:
    print("\nI don't understand that arg1, please try again.\n")

#...............
print("Thanks again, bye now.")
#...............
