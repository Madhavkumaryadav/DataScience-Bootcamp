import logging as lg 
lg.basicConfig(filename="OOPs.log",level=lg.ERROR)

class Data:
  def __init__(self,fileName,fileType,data,size):
    self.fileName=fileName 
    self.fileType=fileType 
    self.data=data
    self.size=size

  def file_open(self):
    try:
      with open(self.fileName+self.fileType,'w') as f:
        f.write(self.data)
    except Exception as e:
      self.logging(e)
  
  def file_read(self):
    try:
      with open(self.fileName + self.fileType , 'r') as f:
        f.read()
    except FileNotFoundError as e:
      self.logging(e)
    except Exception as e:
      self.logging(e)

  def file_append(self,data):
    try:
      with open(self.fileName + self.fileType , 'a' ) as f:
        f.write(data)
    except FileNotFoundError as e:
      self.logging(e)
    except Exception as e:
      self.logging(e)
  
  def logging(self,log):
    return lg.error(log)
    


d=Data('d','.txt','hello this is level 2 by madhav created  ',2)

d.file_open()
d.file_append("Adding the new line ")