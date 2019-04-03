import sys, traceback
import asvmq

def logger(exctype,value,tb):
    #print ("My error information")
    #print ("Type : ",exctype)
    #print ("Value : ",value)
    #print ("Traceback : ",tb)
    string = ("Error type : %s , traceback : %s " % (exctype, traceback.print_tb(tb)))
    asvmq.log_fatal(string)
    sys.__excepthook__()

sys.excepthook = logger
