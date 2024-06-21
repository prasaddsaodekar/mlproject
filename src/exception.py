import sys
# from src.logger import *

def error_msg_detail(error,error_dtl:sys):
    _,_,exc_dtl = error_dtl.exc_info()
    file_name=exc_dtl.tb_frame.f_code.co_filename
    error_msg="Error occured in Python script name [{0}] line nbr [{1}] error msg [{2}]".format(file_name,exc_dtl.tb_lineno,str(error))
    return error_msg

class CustomException(Exception):
    def __init__(self,error_msg,error_dtl:sys):
        super().__init__(error_msg)
        self.error_msg=error_msg_detail(error_msg,error_dtl=error_dtl)
        
    def __str__(self):
        return self.error_msg