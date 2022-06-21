#Python 2.7.6
#RestfulClient.py

import sys
import requests
import os
from requests.auth import HTTPBasicAuth
import json
import time

#======================================= Global and Environment Variable ==============================
packageVersion=""
packageID=""

#======================================= Global and Environment Variable ==============================


#======================================= Play Area ==============================


#======================================= Play Area ==============================


class HTTPRequests:
#-------------------------- Validate Process STARTS-----------------------------
	def GetProcess(url,authUserName,authPassword):
		headers={'Accept': 'application/json'}
		myResponse = requests.get(url,headers=headers,auth=HTTPBasicAuth(authUserName, authPassword), verify=True)
		if(myResponse.ok):
			jData = json.loads(myResponse.content)
			print(jData)
		else:
			return myResponse.status_code

#-------------------------- Validate Process ENDS -------------------------------------------

#-------------------------- GET Call ------------'https://api.boomi.com/api/rest/v1/'+os.environ["BoomiAccountID"]+'/PackagedComponent/'-----------------------------
	def Get(url,authUserName,authPassword):
		headers={'Accept': 'application/json'}
		myResponse = requests.get(url,headers=headers,auth=HTTPBasicAuth(authUserName, authPassword), verify=True)
		if(myResponse.ok):
			jData = json.loads(myResponse.content)
			print(jData)
		else:
			myResponse.raise_for_status()
#-------------------------- GET Call -------------------------------------------

#-------------------------- POST Call for package Creation -------------------------------------------
	def PackageCreation(url,authUserName,authPassword,BoomiComponentID,PackageReleaseNote):
		headers = {'Accept': 'application/json'}
		myResponse = requests.post(url,headers=headers,auth=HTTPBasicAuth(authUserName, authPassword),data=Constructdata.ConstructPackageCreationXMLdata(BoomiComponentID,PackageReleaseNote),verify=True)
		print (myResponse.content)

		if(myResponse.ok):
			jData = json.loads(myResponse.content)
			if("packageId" in jData):
				packageID=jData["packageId"]
				os.environ["latest_packageID"]=packageID
			else:
				os.environ["latest_packageID"]="NULL"
			return(jData)
		else:
			myResponse.raise_for_status()
#-------------------------- POST Callfor package Creation -------------------------------------------

#-------------------------- POST Call for Deployment-------------------------------------------
	def Deployment(url,authUserName,authPassword,latestPackageID,BoomiENVID,DeploymentNote):
		headers = {'Accept': 'application/json'}
		myResponse = requests.post(url,headers=headers,auth=HTTPBasicAuth(authUserName, authPassword),data=Constructdata.ConstructDeploymentXMLdata(latestPackageID,BoomiENVID,DeploymentNote),verify=True)
		print (myResponse.content)

		if(myResponse.ok):
			jData = json.loads(myResponse.content)
			print(jData)
		else:
			myResponse.raise_for_status()
#-------------------------- POST Call for Deployment -------------------------------------------

#-------------------------- POST Call for Environment Extension Update-------------------------------------------
	def EnvironmentExtensionUpdate(url,authUserName,authPassword,xmldata):
		headers = {'Accept': 'application/json'}
		myResponse = requests.post(url,headers=headers,auth=HTTPBasicAuth(authUserName, authPassword),data=xmldata,verify=True)

		if(myResponse.ok):
			# print(myResponse.content)
			# t = ElementTree.XMLID(myResponse.content)
			# print(ElementTree.tostring(t[1]['51809218-8c4f-47d0-80f0-b89fb637088f']))
			jData = json.loads(myResponse.content)
			print(jData)
		else:
			myResponse.raise_for_status()
#-------------------------- POST Call for Environment Extension Update -------------------------------------------

#-------------------------- POST Call for Environment Extension Query-------------------------------------------
	def EnvironmentExtensionQuery(url,authUserName,authPassword,BoomiENVID):
		headers = {'Accept': 'application/json'}
		myResponse = requests.post(url,auth=HTTPBasicAuth(authUserName, authPassword),data=Constructdata.constructEnvExtQueryXMLdata(BoomiENVID),verify=True)

		if(myResponse.ok):
			print(myResponse.content)
			# # t = ElementTree.XMLID(myResponse.content)
			# # print(ElementTree.tostring(t[1]['51809218-8c4f-47d0-80f0-b89fb637088f']))
			# jData = json.loads(myResponse.content)
			# print(jData)
		else:
			myResponse.raise_for_status()
#-------------------------- POST Call for  Environment Extension Query -------------------------------------------

class Constructdata:
#-------------------------- ConstructXMLdata Call -------------------------------------------
	def ConstructPackageCreationXMLdata(BoomiComponentID,PackageReleaseNote):
		ResultData='<bns:PackagedComponent xmlns:bns="http://api.platform.boomi.com/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><bns:componentId>'+BoomiComponentID+'</bns:componentId><bns:packageVersion></bns:packageVersion><bns:notes>'+PackageReleaseNote+'</bns:notes></bns:PackagedComponent>'
		return (ResultData)
	def ConstructDeploymentXMLdata(latestPackageID,BoomiENVID,DeploymentNote):
		ResultData='<bns:DeployedPackage xmlns:bns="http://api.platform.boomi.com/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/"><bns:environmentId>'+BoomiENVID+'</bns:environmentId><bns:packageId>'+latestPackageID+'</bns:packageId><bns:notes>'+DeploymentNote+'</bns:notes><bns:listenerStatus>PAUSED</bns:listenerStatus></bns:DeployedPackage>'
		return (ResultData)
	def constructEnvExtXMLdata():
		ResultData='<bns:EnvironmentExtensions xmlns:bns="http://api.platform.boomi.com/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="51809218-8c4f-47d0-80f0-b89fb637088f" extensionGroupId="" environmentId="51809218-8c4f-47d0-80f0-b89fb637088f"><bns:connections><bns:connection name="Processing Folder Connection" id="81b07fdf-af58-4bcb-8ba4-0ef5e2008552"><bns:field componentOverride="false" usesEncryption="false" encryptedValueSet="false" id="directory"/></bns:connection></bns:connections><bns:processProperties><bns:ProcessProperty name="New Process Property" id="5ce901b9-faaf-4747-872b-80e787bb449b"><bns:ProcessPropertyValue encryptedValueSet="false" value="Sample" key="b51d937e-13d6-41d3-9248-d66bf054d3e8" label="Process Property #1"/><bns:ProcessPropertyValue encryptedValueSet="false" value="Sample2" key="819567ff-ccdd-4aed-b7e3-074cac07c6dc" label="Process Property #2"/>	</bns:ProcessProperty></bns:processProperties><bns:properties><bns:property value="Test" name="Test For Env Ext"/><bns:property value="Test from python and env 1 ext" name="TestProperty1"/></bns:properties></bns:EnvironmentExtensions>'

		return (ResultData)
	def constructEnvExtQueryXMLdata(BoomiENVID):
		ResultData='<QueryConfig xmlns="http://api.platform.boomi.com/"><QueryFilter><expression operator="and" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="GroupingExpression"><nestedExpression operator="EQUALS" property="environmentId" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="SimpleExpression"><argument>'+BoomiENVID+'</argument></nestedExpression></expression></QueryFilter></QueryConfig>'
		return (ResultData)
#-------------------------- ConstructXMLdata Call -------------------------------------------




#================== Simple Script++++++++++++++++++++++++++
#-------------------------- Credentials Load STARTS-------------------------------------------

BoomiUserName=os.environ["BoomiUsername"]
BoomiPassword=os.environ["BoomiPassword"]


#-------------------------- Credentials Load ENDS-------------------------------------------


class WorkSpace:
	def ValidateComponents():
		arr=[]
		with open('./temp/json_config.json') as data:
			op=json.loads(data.read())
		for val in op["components"]:
			call_get = HTTPRequests.GetProcess("https://api.boomi.com/api/rest/v1/"+op["BoomiAccountID"]+"/Process/"+val["id"],BoomiUserName,BoomiPassword)

			if(call_get==400):
				arr.append(val["id"])
			time.sleep(1)
		if not arr:
			print("\nComponents are Available Boomi\n")
		else:
			print("Following Components from the configuration files are not available in Boomi \n")
			print('\n'.join(arr))
			sys.exit(-1)
	#-------------------------- Deployment Call STARTS -------------------------------------------
	def DeployBoomi():
		with open('./temp/json_config.json') as data:
			op=json.loads(data.read())
		data ={}
		data["BoomiAccountID"] = op["BoomiAccountID"]
		data["BoomiENVID"] = op["BoomiENVID"]
		data["packages"]=[]
		for val in op["components"]:
			print("\n============================= Packaging STARTS =================================\n")
			print('Deployment of "'+val["name"]+'" with Component ID "'+val["id"]+'" is started and Package Release note is "'+val["note"]+'"')
			print("\n------------------------Packaging : "+val["name"]+" ----------------------------------------")
			call_get_pkg = HTTPRequests.PackageCreation('https://api.boomi.com/api/rest/v1/'+op["BoomiAccountID"]+'/PackagedComponent/',BoomiUserName,BoomiPassword,val["id"],val["note"])
			print("\n============================= Packaging ENDS =================================\n")
			data["packages"].append({"Demo":"false","QA":"true","notes":call_get_pkg['notes'],"pkg_created_at":call_get_pkg['createdDate'],"pkg_id":call_get_pkg['packageId'],"pkg_name":val['name'],"packageVersion":call_get_pkg['packageVersion']})
			time.sleep(0.5)
		with open('./pkg_config.json', 'w') as outfile:  
			json.dump(data, outfile, indent=4, separators=(',', ': '), sort_keys=True)
		with open('./pkg_config.json') as data:
			opa=json.loads(data.read())
		for v in opa["packages"]:
			print("\n=============================== Deployment Starts ===============================\n")
			print("\n------------------------Deploying Pkg: "+v["pkg_name"]+" -------------------------------")
			call_get = HTTPRequests.Deployment('https://api.boomi.com/api/rest/v1/'+opa["BoomiAccountID"]+'/DeployedPackage',BoomiUserName,BoomiPassword,v["pkg_id"],opa["BoomiENVID"],v["notes"])
			print("\n=============================== Deployment ENDS ===============================\n")

		#-------------------------- Deployment Call ENDS -------------------------------------------



#-------------------------- Update EnvExt Call STARTS -------------------------------------------
	def EnvExtBoomi():
		xmldata=''
		with open('./temp/EnvExtConfig.json') as envdata:
			evext=json.loads(envdata.read())

		xmldata=xmldata+'<bns:EnvironmentExtensions xmlns:bns="http://api.platform.boomi.com/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="'+evext["BoomiENVID"]+'" extensionGroupId="" environmentId="'+evext["BoomiENVID"]+'"><bns:connections>'

		for v in evext["connections"]:
			xmldata=xmldata+'<bns:connection name="'+v["name"]+'" id="'+v["id"]+'">'
			for w in v["field"]:
				if w["id"]=="password":
					xmldata=xmldata+'<bns:field componentOverride="false" usesEncryption="true" encryptedValueSet="true" id="'+w["id"]+'" value="'+w["value"]+'"/>'	
				else:
					xmldata=xmldata+'<bns:field usesEncryption="false" componentOverride="false" encryptedValueSet="false" id="'+w["id"]+'" value="'+w["value"]+'"/>'
			xmldata=xmldata+'</bns:connection>'
		xmldata=xmldata+'</bns:connections>'
		xmldata=xmldata+'<bns:processProperties>'
		for i in evext["processProperties"]:
			xmldata=xmldata+'<bns:ProcessProperty id="'+i["id"]+'" name="'+i["name"]+'">'
			for j in i["ProcessPropertyValue"]:
				xmldata=xmldata+'<bns:ProcessPropertyValue label="'+j["label"]+'" key="'+j["key"]+'" value="'+j["value"]+'" encryptedValueSet="false"/>'
			xmldata=xmldata+'</bns:ProcessProperty>'
		xmldata=xmldata+'</bns:processProperties>'	

		xmldata=xmldata+'<bns:properties>'
		for i in evext["properties"]:
			xmldata=xmldata+'<bns:property name="'+i["name"]+'" value="'+i["value"]+'" encryptedValueSet="false"/>'
		xmldata=xmldata+'</bns:properties>'
		xmldata=xmldata+'</bns:EnvironmentExtensions>'

		print("\n=============================  Environment Extensions STARTS =================================\n")
		print(xmldata)
		call_get = HTTPRequests.EnvironmentExtensionUpdate('https://api.boomi.com/api/rest/v1/'+evext["BoomiAccountID"]+'/EnvironmentExtensions/'+evext["BoomiENVID"]+'/update',BoomiUserName,BoomiPassword,xmldata)
		print("\n----------------------------------------------------------------\n")
		print("=============================== Environment Extensions ENDS===============================")


#============================== Caller STARTS =============================================
call_Validation = WorkSpace.ValidateComponents()
call_Boomi_Component = WorkSpace.DeployBoomi()
call_EnvExt = WorkSpace.EnvExtBoomi()
#============================== Caller ENDS=============================================


