#main class for executing MALT behaviours through the MALT API Wrapper
import malt_apiWrapper as malt
from ftp_client import MALTFTPClient


ip= "192.168.115.177"

#
# print("\nTest Settings:")
# print(malt.get_testSettings(ip,index=1))
#
# print("\n Calibration Settings:")
# print(malt.get_calibrationSettings(ip,channel="testPA"))
#
# print("\n Option Settings:")
# print(malt.get_optionSettings(ip))
#
# print("\n Setting Calibration in MALT:")
# print(malt.set_calibration(ip,{
#     "calibration":[
# 					{"channel":"testPA","settings":{"offset":27.0}},
# 					{"channel":"diffPA","settings":{"gradient":1.5,"offset":-4.0}}
# 				]
# }))
#
# print("\n Calibration Settings:")
# print(malt.get_calibrationSettings(ip,channel="testPA"))
#
# print("\n Setting options in MALT:")
# print(malt.set_options(ip,{
#     "options":{"logLevel":3,"startenable":True}
# }))
#
# print("\n Setting Test Config:")
# print(malt.set_testSettings(ip,{
#     "testconfig":[
#                         {"index":3,"settings":{"idString":"Cylinder Head Cover","filltime":6200,"measuretime":1500}}
#                     ]
# }))
#
# print("\nIs test running?")
# print(malt.is_test_running(ip))
#
# print("\nStatus Lights:")
# print(malt.get_status_lights(ip))
#
# print("\nResult Code:")
# print(malt.get_result_code(ip))
#
# print("\nLast Data:")
# print(malt.get_last_data(ip))
#
# print("\nFull Configuration:")
# print(malt.configure(ip, {
#     "options":{"logLevel":3,"startenable":True},
# 	"calibration":[
# 			    {"channel":"testPA","settings":{"offset":15.0}},
# 			    {"channel":"diffPA","settings":{"gradient":1.5,"offset":-4.0}}
# 				],
# 	"testconfig":[
# 				{"index":2,"settings":{"idString":"Pump","filltime":5000,"measuretime":1000}},
# 				{"index":3,"settings":{"idString":"Cylinder Head Cover","filltime":12000,"measuretime":1500}},
# 				{"index":4,"settings":{"idString":"Valve","testpressure":2000}}
# 				]
# }))
#
print("Starting test")
print (malt.start_test(ip,1))
#
# print ("Reset MALT")
# print(malt.reset(ip))


#Connecting to MALT FTP server
# ftp = MALTFTPClient("192.168.115.177")
#
# print("\n Current Directory:")
# print(ftp.get_current_dir())
#
# print("\n Listing:")
# for line  in ftp.list_dir():
# 	print(line)
#
# print("\n File Names Only:")
# print(ftp.list_names())
#
# # Optional: change to a folder
# print("\n🔀 Changing Directory:")
# print(ftp.change_dir("Y202410"))
#
# print("\n Listing:")
# for line  in ftp.list_dir():
# 	print(line)
#
# # Download multiple selected files
# print("\n⬇ Downloading files:")
# selected = ["20241003.CSV", "20241017.CSV"]
# for msg in ftp.download_selected(selected, "./Downloads"):
#     print(msg)
#
# # Delete a file
# print("\n Delete a file:")
# print(ftp.delete_file("old.txt"))
#
# # Delete multiple
# print("\n Deleting selected files:")
# files_to_delete = ["old1.txt","old2.txt"]
# for msg in ftp.delete_selected(files_to_delete):
# 	print(msg)
#
# ftp.close()







