import socket
import time
import picamera
import threading

stopStream = False

class Test(threading.Thread):
    def __ini__(self):
        threading.Thread.__init__(self)
        

    def run(self):
        print("start")
        try:
            with picamera.PiCamera() as camera:
                camera.resolution = (320, 240)
                camera.rotation = 180
                camera.framerate = 38

                server_socket = socket.socket()
                server_socket.bind(('0.0.0.0', 8034))
                server_socket.listen(0)
                connection = server_socket.accept()[0].makefile('wb')
                
                time.sleep(2)
                # Start recording, sending the output to the connection for 60
                # seconds, then stop
                camera.start_recording(connection, format='h264')
                while(True):
                    print("streammmm")
                    time.sleep(5)
                    #stopStream = True
                    print(self.stopStream)
                    if(stopStream == True):
                        camera.stop_recording()
                        break
        except e:
            print(e)
        finally:
            connection.close()
            server_socket.close()
            
    def stop(self):
        print("Stop")
        self.stopStream = True